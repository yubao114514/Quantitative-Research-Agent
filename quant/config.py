import json
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def load_app_config() -> dict:
    with open(ROOT / "config" / "app_config.json", "r", encoding="utf-8") as file:
        return json.load(file)


@lru_cache(maxsize=1)
def load_paper_library() -> list[dict]:
    with open(ROOT / "config" / "papers.json", "r", encoding="utf-8") as file:
        return json.load(file)
