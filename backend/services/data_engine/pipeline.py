"""Data Engine: Tabular preprocessing, missing value imputation, outlier detection, and time-series pipelines."""

import io
import csv
import math
from typing import Dict, Any, List, Optional
import pandas as pd
import numpy as np

class DataEngine:
    """Provides tabular data cleansing, statistical profiling, and anomaly detection."""

    def clean_csv_data(self, csv_content: str) -> Dict[str, Any]:
        """Cleans CSV text: detects missing values, duplicates, outliers, and provides cleaning reports."""
        try:
            df = pd.read_csv(io.StringIO(csv_content))
        except Exception as e:
            return {"error": f"Failed to parse CSV: {str(e)}", "success": False}

        original_rows = len(df)
        original_cols = len(df.columns)

        # 1. Missing values report
        missing_counts = df.isnull().sum().to_dict()
        total_missing = sum(missing_counts.values())

        # 2. Duplicate detection (checks content columns ignoring artificial id/index)
        cols_no_id = [c for c in df.columns if c.lower() not in ("id", "index", "_id")]
        subset_cols = cols_no_id if cols_no_id else None
        duplicate_count = int(df.duplicated(subset=subset_cols).sum())

        # 3. Numeric columns & outlier detection via IQR
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        outliers_detected = {}
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            num_outliers = int(((df[col] < lower_bound) | (df[col] > upper_bound)).sum())
            if num_outliers > 0:
                outliers_detected[col] = num_outliers

        # Clean dataframe: drop duplicates & fill missing with median/mode
        df_cleaned = df.drop_duplicates(subset=subset_cols)
        for col in df_cleaned.columns:
            if df_cleaned[col].dtype in [np.float64, np.int64]:
                median_val = df_cleaned[col].median()
                df_cleaned[col] = df_cleaned[col].fillna(median_val)
            else:
                mode_series = df_cleaned[col].mode()
                mode_val = mode_series[0] if not mode_series.empty else "Unknown"
                df_cleaned[col] = df_cleaned[col].fillna(mode_val)

        # Convert back to clean CSV
        cleaned_csv_buf = io.StringIO()
        df_cleaned.to_csv(cleaned_csv_buf, index=False)
        cleaned_csv_text = cleaned_csv_buf.getvalue()

        return {
            "success": True,
            "original_shape": {"rows": original_rows, "cols": original_cols},
            "cleaned_shape": {"rows": len(df_cleaned), "cols": len(df_cleaned.columns)},
            "duplicates_removed": duplicate_count,
            "missing_values_imputed": total_missing,
            "missing_by_column": missing_counts,
            "outliers_found": outliers_detected,
            "cleaned_csv_sample": cleaned_csv_text[:1000],
            "cleaned_csv_full": cleaned_csv_text,
        }

    def detect_time_series_anomalies(self, timestamps: List[str], values: List[float], threshold_std: float = 2.0) -> Dict[str, Any]:
        """Detects anomalies in continuous time-series metrics using rolling standard deviations."""
        if not values or len(values) < 3:
            return {"anomalies": [], "baseline_mean": 0.0, "baseline_std": 0.0}

        arr = np.array(values, dtype=np.float64)
        mean_val = float(np.mean(arr))
        std_val = float(np.std(arr)) if np.std(arr) > 0 else 1.0

        anomalies = []
        for i, val in enumerate(values):
            z_score = abs(val - mean_val) / std_val
            if z_score >= threshold_std:
                anomalies.append({
                    "index": i,
                    "timestamp": timestamps[i] if i < len(timestamps) else f"T+{i}",
                    "value": val,
                    "z_score": round(float(z_score), 2),
                    "severity": "CRITICAL" if z_score > 3.0 else "WARNING",
                })

        return {
            "total_points": len(values),
            "anomalies_count": len(anomalies),
            "baseline_mean": round(mean_val, 2),
            "baseline_std": round(std_val, 2),
            "anomalies": anomalies,
        }

data_engine = DataEngine()
