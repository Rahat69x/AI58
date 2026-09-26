"""Text-to-Speech Service: Audio cue compilation and client synthesis instructions."""

from typing import Dict, Any, List

class TextToSpeechService:
    """Provides TTS parameters, voice selection, and speech synthesis payloads."""

    AVAILABLE_VOICES = [
        {"id": "nova-voice", "name": "Nova", "gender": "Female", "accent": "Neutral / Global"},
        {"id": "echo-voice", "name": "Echo", "gender": "Male", "accent": "Neutral / Professional"},
        {"id": "zen-voice", "name": "Zen", "gender": "Calm", "accent": "Relaxed / Meditation"},
        {"id": "atlas-voice", "name": "Atlas", "gender": "Authoritative", "accent": "Technical Coach"},
    ]

    def synthesize_spec(self, text: str, voice: str = "nova-voice", rate: float = 1.0, pitch: float = 1.0) -> Dict[str, Any]:
        """Generates speech synthesis configuration for Web Speech API and backend streaming."""
        return {
            "text": text,
            "voice": voice,
            "rate": max(0.5, min(2.0, rate)),
            "pitch": max(0.5, min(1.5, pitch)),
            "character_count": len(text),
            "estimated_duration_seconds": round(len(text.split()) / (2.5 * rate), 2),
            "status": "ready_for_synthesis",
        }

    def get_voices(self) -> List[Dict[str, Any]]:
        return self.AVAILABLE_VOICES

text_to_speech_service = TextToSpeechService()
