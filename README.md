# course_mapping

Streamlit app for a JSON-based Recognition of Prior Learning (RPL) / credit transfer workflow.

## Quickstart

- Install deps: `pip install -r requirements.txt` (or your environment equivalent)
- Run: `streamlit run app.py`

## Data layout

- Application JSON: `data/applications/application_0001.json`
- Reference data: `data/reference/`

## Notes

- `utils/json_db.py` updates `meta.updated_at` on save (UTC, `Z`-suffixed).
- If the JSON contains an existing guidance discussion date, `ui/guidance_form.py` will use it as the default in the date picker.
