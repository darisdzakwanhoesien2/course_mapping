# def list_to_csv(value):
#     if isinstance(value, list):
#         return ", ".join(value)
#     return value or ""
def list_to_csv(value):
    if isinstance(value, list):
        return ", ".join(
            v.get("filename", v) if isinstance(v, dict) else str(v)
            for v in value
        )
    return value or ""

def csv_to_list(value):
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]
