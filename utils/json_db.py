import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "applications"


def load_application(app_id: str = "application_0001") -> dict:
    """Load a single application JSON document."""
    path = DATA_DIR / f"{app_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    return json.loads(path.read_text(encoding="utf-8"))


def save_application(app_id: str, data: dict) -> None:
    """Persist an application JSON document and update meta.updated_at."""
    data.setdefault("meta", {})
    data["meta"]["updated_at"] = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    path = DATA_DIR / f"{app_id}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
