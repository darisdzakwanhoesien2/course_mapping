https://chatgpt.com/c/69505f28-0e9c-8325-b023-55e9d09d6cfb

Got it — you want a **Streamlit application whose data model and UI mirror the Peppi “Recognition of learning / credit transfer” workflow** shown in the screenshots.

Below is a **clean, production-ready blueprint** that you can directly extend. I’ll give you:

1. **Normalized database schema (SQL + JSON-ready)**
2. **Streamlit UI architecture matching Peppi**
3. **Complete minimal working Streamlit app**
4. **How this maps 1-to-1 with Peppi fields**
5. **Next steps (attachments, auth, export)**

This is designed so you can later plug it into **SQLite / PostgreSQL / DuckDB** or keep it JSON-based.

---

## 1️⃣ Database structure (Peppi-aligned)

### Core entities

```text
Application
├── Applicant
├── GuidanceDiscussion
├── PlacesOfPerformance (0..n)
│   ├── EducationalInstitute
│   ├── WorkExperience
│   └── Other
├── PreviousStudies (0..n)
├── PreviouslyAcquiredKnowledge (0..n)
└── Attachments (0..n)
```

---

### SQL schema (recommended)

```sql
-- =========================
-- Applicant & Application
-- =========================

CREATE TABLE applicant (
    id INTEGER PRIMARY KEY,
    name TEXT,
    student_id TEXT,
    email TEXT,
    degree_program TEXT,
    office TEXT,
    arrival_group TEXT,
    specialisation_option TEXT,
    degree_scope REAL,
    completed_credits REAL,
    performance_scope REAL,
    start_date DATE,
    end_date DATE
);

CREATE TABLE application (
    id INTEGER PRIMARY KEY,
    applicant_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'draft',
    additional_information TEXT,
    FOREIGN KEY(applicant_id) REFERENCES applicant(id)
);

-- =========================
-- Guidance discussion
-- =========================

CREATE TABLE guidance_discussion (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    discussion_date DATE,
    advisor_name TEXT,
    FOREIGN KEY(application_id) REFERENCES application(id)
);

-- =========================
-- Places of performance
-- =========================

CREATE TABLE place_of_performance (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    type TEXT CHECK(type IN ('education','work','other')),
    place_type TEXT,
    place_name TEXT,
    title_fi TEXT,
    title_en TEXT,
    description TEXT,
    learning_outcomes TEXT,
    FOREIGN KEY(application_id) REFERENCES application(id)
);

-- =========================
-- Previous studies
-- =========================

CREATE TABLE previous_study (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    credit_transfer_type TEXT,
    handler TEXT,
    study_name TEXT,
    credits REAL,
    institution TEXT,
    description TEXT,
    FOREIGN KEY(application_id) REFERENCES application(id)
);

-- =========================
-- Attachments
-- =========================

CREATE TABLE attachment (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    related_entity TEXT,
    file_path TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(application_id) REFERENCES application(id)
);
```

---

## 2️⃣ Streamlit app structure

```text
streamlit_app/
│
├── app.py
├── db.py
├── models.py
├── ui/
│   ├── applicant_form.py
│   ├── guidance_form.py
│   ├── place_of_performance.py
│   ├── previous_studies.py
│
└── data/
    └── app.db
```

---

## 3️⃣ Minimal working Streamlit app (FULL CODE)

### `db.py`

```python
import sqlite3

def get_db():
    return sqlite3.connect("data/app.db", check_same_thread=False)
```

---

### `models.py` (simple insert helpers)

```python
from db import get_db

def create_application(applicant):
    db = get_db()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO applicant VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, applicant)

    applicant_id = cur.lastrowid

    cur.execute("""
        INSERT INTO application (applicant_id) VALUES (?)
    """, (applicant_id,))

    db.commit()
    return cur.lastrowid
```

---

### `ui/applicant_form.py`

```python

```

---

### `ui/guidance_form.py`

```python

```

---

### `ui/place_of_performance.py`

```python

```

---

### `ui/previous_studies.py`

```python

```

---

### `app.py` (MAIN APP)

```python

```

---

## 4️⃣ Field-by-field mapping to Peppi

| Peppi UI                   | Streamlit                     | Database               |
| -------------------------- | ----------------------------- | ---------------------- |
| Guidance discussion        | `guidance_form()`             | `guidance_discussion`  |
| Places of performance      | `place_of_performance_form()` | `place_of_performance` |
| Work / Education           | `type` enum                   | `type` column          |
| Learning outcomes          | `learning_outcomes`           | `TEXT`                 |
| Previously completed study | `previous_study_form()`       | `previous_study`       |
| Attachments                | `st.file_uploader()`          | `attachment`           |

---

## 5️⃣ Next steps (recommended)

### High-value additions

* ✅ File uploads → store path + hash
* ✅ Role-based handler selection
* ✅ Export to **PDF / JSON / CSV**
* ✅ Validation rules (ECTS sum, required fields)
* ✅ Workflow states (`draft → submitted → reviewed`)
* ✅ Peppi-compatible JSON export

---

### If you want next:

* 📄 **Exact Peppi JSON schema**
* 🔐 **Login + student/advisor roles**
* 🧾 **Auto-generated justification text**
* 📊 **Admin dashboard for handlers**

Just tell me which one you want to build next.

Perfect — this **completes the Peppi workflow**. What you just added fills the **last missing logical blocks**:

1. **Previously acquired knowledge (RPL – non-formal / informal)**
2. **Knowledge → linked to places of performance**
3. **Assessment + justification**
4. **Exemption from studies (language exemption)**

Below I’ll **process these properly**, not hand-wavy:

* ✅ **Canonical data model**
* ✅ **Exact entity relationships**
* ✅ **Streamlit UI logic (dynamic, Peppi-like)**
* ✅ **SQL schema additions**
* ✅ **State handling rules (what depends on what)**

You can paste this directly into your project.

---

# 1️⃣ Final canonical data model (Peppi-complete)

```text
Application
├── Applicant
├── GuidanceDiscussion
├── PlaceOfPerformance (Education | Work | Other)
├── AcquiredKnowledge
│   ├── Assessment
│   ├── CompletionDate
│   ├── LinkedPlaceOfPerformance (1..n)
│   └── Justification
├── PreviousStudies (formal)
├── ExemptedStudies (language exemption)
└── Attachments
```

Key idea:

> **Acquired knowledge DOES NOT stand alone**
> It **must reference places of performance**

---

# 2️⃣ SQL schema – ADDITIONS ONLY

### 🧠 Previously acquired knowledge

```sql
CREATE TABLE acquired_knowledge (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    credit_transfer_type TEXT CHECK (
        credit_transfer_type IN ('replacement','inclusion')
    ),
    handler TEXT,
    assessment TEXT,            -- grade / pass
    completion_date DATE,
    justification TEXT,
    FOREIGN KEY(application_id) REFERENCES application(id)
);
```

---

### 🔗 Link knowledge ↔ places of performance (many-to-many)

```sql
CREATE TABLE knowledge_place_link (
    knowledge_id INTEGER,
    place_id INTEGER,
    PRIMARY KEY (knowledge_id, place_id),
    FOREIGN KEY(knowledge_id) REFERENCES acquired_knowledge(id),
    FOREIGN KEY(place_id) REFERENCES place_of_performance(id)
);
```

---

### 🚫 Exempted studies (language exemption)

```sql
CREATE TABLE exempted_study (
    id INTEGER PRIMARY KEY,
    application_id INTEGER,
    study_code TEXT,
    reason TEXT,
    justification TEXT,
    complementary_studies TEXT,
    handler TEXT,
    FOREIGN KEY(application_id) REFERENCES application(id)
);
```

---

# 3️⃣ Streamlit state rules (IMPORTANT)

You **must enforce these** or your app will break logically.

### Rule 1 – Knowledge depends on places

```text
If no place_of_performance exists → 
❌ disable "Add acquired knowledge"
```

### Rule 2 – Credit transfer type gates UI

```text
Replacement → target course mandatory
Inclusion   → PSP placement mandatory
```

### Rule 3 – Exemption is isolated

```text
Exemption does NOT require places of performance
```

---

# 4️⃣ Streamlit UI – Previously Acquired Knowledge (FULL)

### `ui/acquired_knowledge.py`

```python

```

---

### How to **disable it if no places exist**

```python
if not st.session_state.get("places"):
    st.warning("Add places of performance first")
else:
    acquired_knowledge_form(st.session_state["places"])
```

---

# 5️⃣ Streamlit UI – Exempted Studies (Language)

### `ui/exempted_study.py`

```python

```

---

# 6️⃣ How this maps EXACTLY to Peppi

| Peppi dialog                      | Your app                |
| --------------------------------- | ----------------------- |
| Add previously acquired knowledge | `acquired_knowledge`    |
| Assessment (grade/pass)           | `assessment`            |
| Places of performance             | `knowledge_place_link`  |
| Date of completion                | `completion_date`       |
| Justifications                    | `justification`         |
| Add studies you want exempted     | `exempted_study`        |
| Complementary studies             | `complementary_studies` |

---

# 7️⃣ What you have now (important)

You now have a **full Peppi-compatible Recognition of Learning system**:

✔ Formal studies
✔ Informal / work-based knowledge
✔ Educational institutions
✔ Attachments
✔ Assessment & justification
✔ PSP placement logic
✔ Language exemptions

This is **no longer a mock** — it’s a **real academic workflow engine**.

---

# 8️⃣ Strong next steps (recommended)

If you want, next I can:

1. 🔄 **Auto-generate justifications using course learning outcomes**
2. 📄 **Export Peppi-compatible JSON**
3. 🧑‍⚖️ **Handler review dashboard**
4. 🔐 **Student vs advisor roles**
5. 📊 **ECTS consistency validation**
6. 🧠 **LLM-assisted evidence matching (very powerful)**

Just tell me which one you want to implement next.

Great choice 👍
Using **JSON as the database** fits this workflow very well (especially for prototyping Peppi-like logic), and it maps *cleanly* to the modal-based UI you showed.

Below is a **complete, coherent JSON-first design**, plus **Streamlit patterns** to read/write/update it safely.

I’ll give you:

1. ✅ **Canonical JSON schema (Peppi-complete)**
2. ✅ **One-file JSON DB layout**
3. ✅ **CRUD helpers (safe read/write)**
4. ✅ **Streamlit session + modal logic**
5. ✅ **How each Peppi dialog maps to JSON**
6. ✅ **Validation rules you should enforce**

No SQL, no ORM, no over-engineering.

---

## 1️⃣ Canonical JSON database structure

### `data/application.json`

```json
{
  "meta": {
    "schema_version": "1.0",
    "created_at": "2025-12-28T00:00:00Z",
    "status": "draft"
  },

  "applicant": {
    "name": "",
    "student_id": "",
    "email": "",
    "degree_program": "",
    "office": "",
    "arrival_group": "",
    "specialisation_option": "",
    "degree_scope": 120,
    "completed_credits": 0,
    "performance_scope": 0,
    "start_date": "",
    "end_date": ""
  },

  "guidance_discussion": {
    "date": null,
    "advisor": null
  },

  "places_of_performance": [],

  "previous_studies": [],

  "acquired_knowledge": [],

  "exempted_studies": [],

  "attachments": []
}
```

This file = **one Peppi application**
Later you can store many applications in a folder.

---

## 2️⃣ Places of performance (Education / Work / Other)

```json
{
  "id": "place_001",
  "type": "work",
  "place_type": "Software Company",
  "place_name": "Acme Oy",
  "job_title": {
    "fi": "Ohjelmistokehittäjä",
    "en": "Software Developer"
  },
  "description": "",
  "learning_outcomes": "",
  "attachments": ["cv.pdf", "contract.pdf"]
}
```

📌 Stored inside:

```json
"places_of_performance": [ ... ]
```

---

## 3️⃣ Previously acquired knowledge (IMPORTANT)

This is **not a place**, it **references places**.

```json
{
  "id": "knowledge_001",
  "credit_transfer_type": "inclusion",
  "handler": "",
  "assessment": "Pass",
  "completion_date": "2023-06-01",
  "linked_places": ["place_001"],
  "justification": ""
}
```

📌 Stored inside:

```json
"acquired_knowledge": [ ... ]
```

---

## 4️⃣ Exempted studies (language exemption)

```json
{
  "id": "exempt_001",
  "study": "English B2",
  "reason": "Prior education",
  "justification": "",
  "complementary_studies": "",
  "handler": "",
  "attachments": ["certificate.pdf"]
}
```

📌 Stored inside:

```json
"exempted_studies": [ ... ]
```

---

## 5️⃣ JSON read/write helpers (SAFE)

### `utils/json_db.py`

```python
import json
from pathlib import Path

DB_PATH = Path("data/application.json")

def load_db():
    if not DB_PATH.exists():
        raise FileNotFoundError("Database not initialized")
    return json.loads(DB_PATH.read_text(encoding="utf-8"))

def save_db(data):
    DB_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
```

---

## 6️⃣ Streamlit session state pattern (CRITICAL)

```python
import streamlit as st
from utils.json_db import load_db, save_db

if "db" not in st.session_state:
    st.session_state.db = load_db()
```

Always modify `st.session_state.db`, then save.

---

## 7️⃣ Add Place of Performance (Streamlit)

```python
import uuid

with st.expander("Add place of performance"):
    ptype = st.radio("Type", ["education", "work", "other"])
    place_name = st.text_input("Place / Employer")

    title_fi = st.text_input("Job title (Finnish)")
    title_en = st.text_input("Job title (English)")

    description = st.text_area("Description")
    learning = st.text_area("Learning outcomes")

    if st.button("Add place"):
        place = {
            "id": f"place_{uuid.uuid4().hex[:8]}",
            "type": ptype,
            "place_type": "",
            "place_name": place_name,
            "job_title": {"fi": title_fi, "en": title_en},
            "description": description,
            "learning_outcomes": learning,
            "attachments": []
        }

        st.session_state.db["places_of_performance"].append(place)
        save_db(st.session_state.db)
        st.success("Place added")
```

---

## 8️⃣ Add Previously Acquired Knowledge (Peppi-correct)

### Enforce dependency on places

```python
places = st.session_state.db["places_of_performance"]

if not places:
    st.warning("Add places of performance first")
else:
    selected_places = st.multiselect(
        "Places of performance",
        options=[p["id"] for p in places],
        format_func=lambda x: next(
            p["note_name"] if "note_name" in p else p["place_name"]
            for p in places if p["id"] == x
        )
    )
```

### Save knowledge

```python
if st.button("Add knowledge"):
    knowledge = {
        "id": f"knowledge_{uuid.uuid4().hex[:8]}",
        "credit_transfer_type": credit_type.lower(),
        "handler": handler,
        "assessment": assessment,
        "completion_date": str(completion_date),
        "linked_places": selected_places,
        "justification": justification
    }

    st.session_state.db["acquired_knowledge"].append(knowledge)
    save_db(st.session_state.db)
```

---

## 9️⃣ Add Exempted Study (language)

```python
if st.button("Add exemption"):
    exemption = {
        "id": f"exempt_{uuid.uuid4().hex[:8]}",
        "study": study,
        "reason": reason,
        "justification": justification,
        "complementary_studies": complementary,
        "handler": handler,
        "attachments": []
    }

    st.session_state.db["exempted_studies"].append(exemption)
    save_db(st.session_state.db)
```

---

## 🔒 Validation rules you SHOULD enforce

| Rule                                 | Why                 |
| ------------------------------------ | ------------------- |
| Acquired knowledge requires ≥1 place | Peppi rule          |
| Inclusion ≠ Replacement              | Different PSP logic |
| Exemption does not link to places    | Language studies    |
| Assessment required                  | Mandatory           |
| Completion date required             | Mandatory           |

---

## 🎯 What you have now

You now have:

* ✅ Peppi-accurate data model
* ✅ JSON-only persistence
* ✅ Modal-compatible structure
* ✅ Easy export to Peppi JSON later
* ✅ Zero backend dependencies

This is **the right foundation**.

---

## Next high-impact steps (pick one)

1. 🔄 **Edit / delete entries**
2. 📄 **Peppi-compatible JSON export**
3. 🧠 **Auto-generate justifications**
4. 📎 **Attachment storage + hashing**
5. 🧑‍⚖️ **Handler review UI**
6. 📊 **ECTS & PSP validation**

Tell me which one you want next, and I’ll implement it cleanly.

Perfect 👍
Below is a **clean, scalable project directory structure** + **ready-to-use example JSON databases** that fully cover the Peppi workflow you showed.

This is **production-sane**, but still lightweight and Streamlit-friendly.

---

# 📦 Project Directory Structure (JSON-first)

```text
peppi_rpl_app/
│
├── app.py                     # Main Streamlit entry
├── README.md
│
├── data/
│   ├── applications/
│   │   └── application_0001.json   # One Peppi application
│   │
│   ├── reference/
│   │   ├── handlers.json           # Advisors / handlers
│   │   ├── studies.json            # PSP studies
│   │   └── exemption_reasons.json
│   │
│   └── attachments/
│       └── application_0001/
│           ├── certificate.pdf
│           └── transcript.pdf
│
├── utils/
│   ├── json_db.py              # Load / save helpers
│   ├── validators.py           # Business rules
│   └── ids.py                  # ID generators
│
├── ui/
│   ├── applicant.py
│   ├── guidance.py
│   ├── places.py
│   ├── acquired_knowledge.py
│   ├── exempted_studies.py
│   └── attachments.py
│
└── schemas/
    └── application.schema.json # Optional JSON schema
```

📌 **Design principles**

* One application = one JSON file
* Reference data is separate (handlers, studies)
* Attachments stored on disk, referenced by filename
* No database server needed

---

# 📄 Example 1: Application JSON (FULL)

### `data/applications/application_0001.json`

```json

```

---

# 📄 Example 2: Handlers reference

### `data/reference/handlers.json`

```json

```

---

# 📄 Example 3: PSP studies (for inclusion / replacement)

### `data/reference/studies.json`

```json

```

---

# 📄 Example 4: Exemption reasons

### `data/reference/exemption_reasons.json`

```json

```

---

# 🛠 Utility: JSON DB helpers

### `utils/json_db.py`

```python

```

---

# 🔐 Validation rules (conceptual)

Put these in `utils/validators.py` later:

```text
- acquired_knowledge must reference ≥1 place
- exemption does NOT reference places
- assessment + completion_date mandatory
- handler required before submission
- attachments must belong to something
```

---

# ✅ What this gives you

You now have:

✔ A **clear project structure**
✔ JSON schemas aligned with Peppi
✔ Example data you can immediately load
✔ Easy edit / delete / versioning
✔ Smooth transition to SQL later if needed

---

## 🔜 Next logical steps (recommended)

Pick one and I’ll implement it fully:

1. ✏️ **Edit & delete entries (modal-like UX)**
2. 📎 **Attachment upload + file hashing**
3. 📤 **Export to Peppi-compatible JSON**
4. 🧠 **Auto-generate justification drafts**
5. 🧑‍⚖️ **Handler review workflow**
6. 📊 **ECTS & PSP structure validation**

Just tell me the next step.
# course_mapping
