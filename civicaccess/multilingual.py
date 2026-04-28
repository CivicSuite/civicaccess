"""Multilingual variant helpers for CivicAccess v0.1.1."""

from __future__ import annotations

from dataclasses import dataclass

from civicaccess.access_review import DISCLAIMER


@dataclass(frozen=True)
class LanguageVariant:
    language: str
    text: str
    review_required: bool
    disclaimer: str = DISCLAIMER


SAMPLE_VARIANTS = {
    "es": "Muestra: comunÃ­quese con la ciudad para recibir ayuda con este aviso.",
    "vi": "Máº«u: liÃªn há»‡ vá»›i thÃ nh phá»‘ Ä‘á»ƒ Ä‘Æ°á»£c trá»£ giÃºp vá» thÃ´ng bÃ¡o nÃ y.",
}


def create_language_variant(*, text: str, language: str) -> LanguageVariant:
    """Return an explicitly sample multilingual variant."""

    normalized = language.strip().casefold()
    sample = SAMPLE_VARIANTS.get(
        normalized,
        f"Sample variant placeholder for {language}: {text.strip()}",
    )
    return LanguageVariant(language=language, text=sample, review_required=True)
