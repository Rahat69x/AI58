"""SQLAlchemy ORM Entities for AI58."""

from datetime import datetime, timezone
import json
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    full_name = Column(String(128), default="")
    role = Column(String(32), default="engineer")
    preferences_json = Column(Text, default="{}")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    runs = relationship("ProjectRun", back_populates="user", cascade="all, delete-orphan")
    favorites = relationship("UserFavorite", back_populates="user", cascade="all, delete-orphan")
    saved_outputs = relationship("SavedOutput", back_populates="user", cascade="all, delete-orphan")
    checklists = relationship("ProjectChecklist", back_populates="user", cascade="all, delete-orphan")

    @property
    def preferences(self):
        try:
            return json.loads(self.preferences_json) if self.preferences_json else {}
        except Exception:
            return {}

    @preferences.setter
    def preferences(self, value):
        self.preferences_json = json.dumps(value)


class ProjectRun(Base):
    __tablename__ = "project_runs"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    input_payload_json = Column(Text, default="{}")
    output_payload_json = Column(Text, default="{}")
    execution_time_ms = Column(Float, default=0.0)
    status = Column(String(32), default="success")  # success, error, running
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)

    user = relationship("User", back_populates="runs")

    @property
    def input_payload(self):
        try:
            return json.loads(self.input_payload_json) if self.input_payload_json else {}
        except Exception:
            return {}

    @property
    def output_payload(self):
        try:
            return json.loads(self.output_payload_json) if self.output_payload_json else {}
        except Exception:
            return {}


class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    project_id = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="favorites")


class SavedOutput(Base):
    __tablename__ = "saved_outputs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    project_id = Column(Integer, nullable=False, index=True)
    title = Column(String(256), nullable=False)
    notes = Column(Text, default="")
    payload_json = Column(Text, default="{}")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="saved_outputs")

    @property
    def payload(self):
        try:
            return json.loads(self.payload_json) if self.payload_json else {}
        except Exception:
            return {}


class ProjectChecklist(Base):
    __tablename__ = "project_checklists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    project_id = Column(Integer, nullable=False, index=True)
    scaffold = Column(Boolean, default=True)
    ui = Column(Boolean, default=True)
    backend = Column(Boolean, default=True)
    ai_integration = Column(Boolean, default=True)
    database = Column(Boolean, default=True)
    testing = Column(Boolean, default=True)
    documentation = Column(Boolean, default=True)
    deployment = Column(Boolean, default=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="checklists")
