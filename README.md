#  Python Module 08 — The Matrix: Data Engineering Foundations

This project is part of the **42 School Common Core** and introduces
practical Python development practices used in data engineering.

The module focuses on:

- virtual environments and Python runtime isolation;
- dependency management with `pip` and Poetry;
- external libraries for data analysis and visualization;
- environment variables and `.env` configuration;
- secure handling of sensitive values.

Each exercise represents a stage of a small data engineering workflow.

## 📚 Table of Contents

- [Python Module 08 — The Matrix: Data Engineering Foundations](#python-module-08--the-matrix-data-engineering-foundations)
  - [📚 Table of Contents](#-table-of-contents)
  - [📁 Project Structure](#-project-structure)
  - [📌 Exercises Overview](#-exercises-overview)
    - [**Exercise 0 — Entering the Matrix**](#exercise-0--entering-the-matrix)
    - [**Exercise 1 — Loading Programs**](#exercise-1--loading-programs)
    - [**Exercise 2 — Accessing the Mainframe**](#exercise-2--accessing-the-mainframe)
  - [⚙️ Key Learning Points](#️-key-learning-points)
  - [🔐 Security and Best Practices](#-security-and-best-practices)
  - [✅ Notes](#-notes)

## 📁 Project Structure

```text
.
├── ex0/
│   └── construct.py
├── ex1/
│   ├── loading.py
│   ├── pyproject.toml
│   └── requirements.txt
├── ex2/
│   ├── .env.example
│   ├── .gitignore
│   ├── oracle.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

## 📌 Exercises Overview

### **Exercise 0 — Entering the Matrix**

File: `ex0/construct.py`

Introduces virtual environments and runtime isolation.

- Detects whether Python is running inside a virtual environment;
- displays the active interpreter and package installation path;
- explains how to create and activate a `venv`.

**Concepts:** `venv`, `sys.prefix`, Python interpreters and isolated
dependencies.

Run it with:

```bash
python3 ex0/construct.py
```

### **Exercise 1 — Loading Programs**

Files: `ex1/loading.py`, `ex1/requirements.txt` and `ex1/pyproject.toml`

Focuses on dependency management and a basic data analysis pipeline.

- Checks dependencies dynamically with `importlib`;
- supports installation with `pip` or Poetry;
- generates data with `numpy`;
- processes data with `pandas`;
- creates a visualization with `matplotlib`.

The generated `matrix_analysis.png` is an execution output and is ignored
by Git.

Run it from the exercise directory:

```bash
cd ex1
pip install -r requirements.txt
python loading.py
```

### **Exercise 2 — Accessing the Mainframe**

Files: `ex2/oracle.py`, `ex2/.env.example` and `ex2/requirements.txt`

Introduces environment configuration and secure handling of secrets.

- loads configuration with `python-dotenv`;
- supports development and production modes;
- validates required values;
- allows operating-system variables to override `.env` values;
- avoids printing credentials and other sensitive data.

Create a local configuration before running:

```bash
cd ex2
cp .env.example .env
pip install -r requirements.txt
python oracle.py
```

The `.env` file is intentionally ignored and must never be committed.

## ⚙️ Key Learning Points

- Virtual environments isolate project dependencies from the global Python installation.
- `pip` and Poetry provide different workflows for dependency management.
- Dynamic imports make dependency checks explicit and user-friendly.
- `numpy`, `pandas` and `matplotlib` form a small but realistic data pipeline.
- Environment variables make configuration portable across environments.
- Secrets belong in local or managed configuration, not in source code.

## 🔐 Security and Best Practices

- Never commit `.env` files or real credentials.
- Use `.env.example` only as a template with placeholder values.
- Keep production secrets in environment variables or a dedicated secret manager.
- Validate required configuration before starting the application.
- Keep generated files, virtual environments and local materials out of Git.

## ✅ Notes

- Written for **Python 3.10+**.
- The exercises are intentionally small and focused on real-world practices.
- The repository contains source files and configuration templates only; local
	environments and generated outputs are not part of the submission.