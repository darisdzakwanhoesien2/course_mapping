import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "applications"

def load_application(app_id="application_0001"):
    path = DATA_DIR / f"{app_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    return json.loads(path.read_text(encoding="utf-8"))

def save_application(app_id, data):
    data["meta"]["updated_at"] = datetime.utcnow().isoformat()
    path = DATA_DIR / f"{app_id}.json"
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


# import json
# from pathlib import Path

# def load_application(app_id):
#     path = Path(f"data/applications/{app_id}.json")
#     return json.loads(path.read_text(encoding="utf-8"))

# def save_application(app_id, data):
#     path = Path(f"data/applications/{app_id}.json")
#     path.write_text(
#         json.dumps(data, indent=2, ensure_ascii=False),
#         encoding="utf-8"
#     )