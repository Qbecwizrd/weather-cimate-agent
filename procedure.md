

## 🚀 Project Plan: Weather Journal API (FastAPI)

### ⚙️ Goal:

Create a clean, simplified FastAPI backend that allows users to create and retrieve weather journal entries.

---

### 📅 Phase 0: Setup (1 hour)

**Objective:** Get your project environment and structure ready.

#### ✅ Tasks:

* [ ] Create project folder: `weather-journal-api`
* [ ] Create virtual environment: `.venv`
* [ ] Install dependencies:

  ```bash
  pip install fastapi uvicorn sqlalchemy pydantic
  ```
* [ ] Create files:

  * `main.py`
  * `database.py`
  * `models.py`
  * `schemas.py`
  * `crud.py`
  * `routes.py`
* [ ] Create `requirements.txt`

---

### 📅 Phase 1: Database Setup (1–1.5 hours)

**Objective:** Create and configure a simple SQLite DB.

#### ✅ Tasks:

* [ ] In `database.py`: Setup SQLite engine and session
* [ ] In `models.py`: Create `JournalEntry` model with fields:

  * `id`, `date`, `location`, `temperature`, `description`
* [ ] Create DB tables using SQLAlchemy

---

### 📅 Phase 2: Schema & CRUD (2 hours)

**Objective:** Create data validation and DB logic.

#### ✅ Tasks:

* [ ] In `schemas.py`: Create Pydantic models:

  * `JournalEntryCreate`, `JournalEntryRead`
* [ ] In `crud.py`:

  * `create_journal_entry(session, entry)`
  * `get_all_journal_entries(session)`

---

### 📅 Phase 3: API Routes (1–1.5 hours)

**Objective:** Expose API endpoints.

#### ✅ Tasks:

* [ ] In `routes.py`:

  * `POST /entries`: Create a journal entry
  * `GET /entries`: Get all journal entries
* [ ] In `main.py`: Add FastAPI app, include routes

---

### 📅 Phase 4: Testing & Debugging (1–1.5 hours)

**Objective:** Make sure API works via Swagger or Postman.

#### ✅ Tasks:

* [ ] Run with:

  ```bash
  uvicorn app.main:app --reload
  ```
* [ ] Test `POST` and `GET` endpoints on `http://127.0.0.1:8000/docs`
* [ ] Handle errors and edge cases

---

### 📅 Phase 5: Polish & Share (1–2 hours)

**Objective:** Prepare code for LinkedIn & GitHub.

#### ✅ Tasks:

* [ ] Add `README.md`:

  * What it does, tech stack, how to run
* [ ] Upload to GitHub
* [ ] LinkedIn Post Example:

  > ✅ Just built a Weather Journal API with FastAPI
  > 🔥 Lightweight backend, clean routing, SQLite-powered
  > 💻 Code: \[GitHub Link]
  > 🌧️ Let's track some weather moods together!

---

## 🧩 Bonus (Optional Extensions)

| Feature                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| Weather API Integration | Use OpenWeatherMap API to autofill temperature |
| User Authentication     | Add optional user login                        |
| Frontend                | Connect with a simple React/Vue app            |


