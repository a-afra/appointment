# Django Appointment Project

## Setup Instructions

### 1. Clone repository

    git clone <repo-url>
    cd <project>

### 2. Create virtual environment

    python -m venv .venv
    source .venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Environment Variables

Fill the `.env.dev` file based on `.env.dev.sample` and provide all required
environment variables needed by `settings.py` (e.g., SECRET_KEY,
DEBUG, DATABASE configuration, etc.).

The application will not run correctly if required environment variables
are missing.

### 5. Apply migrations

    python manage.py migrate

### 6. Run server

    python manage.py runserver

---

## Authentication (Djoser + JWT)

Base path:

    /auth/

### User Management Endpoints

| Method | Endpoint        |
| ------ | --------------- |
| POST   | /auth/users/    |
| GET    | /auth/users/me/ |

### JWT Endpoints

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /auth/jwt/create/  |
| GET    | /auth/jwt/refresh/ |

---

## pre-commit Setup

Enable hooks:

    pre-commit install

pre-commit ensures formatting, linting, and quality checks before
commits.

---

---

# Git Branching Strategy

## Core Branches

### main

- Production-ready code only
- Always stable
- Tagged for releases (e.g., v1.0.0)
- No direct commits allowed

### develop

- Integration branch
- All features and fixes merge here first
- Must remain runnable at all times

---

## Branch Naming Convention

All branches (except **hotfixes**) are created from `develop`.

### Feature Branch

    feat/<short-description>

Example:

    feat/sample-create-api

Used for new features or enhancements.

---

### Fix Branch

    fix/<short-description>

Example:

    fix/sample-owner-filter

Used for bug fixes.

---

### Hotfix Branch (Production Critical)

    hotfix/<short-description>

Examples:

    hotfix/security-patch

Rules:

- Branch from `main`
- Merge into `main`
- Also merge into `develop`
- Tag new version

---

## Development Workflow

### Start a Feature

    git checkout develop
    git pull origin develop
    git checkout -b feat/sample-create-api

### Push Branch

    git push origin feat/sample-create-api

Open a Pull Request and merge into `develop`.

---

## Rules

- Never commit directly to `main`
- Never develop directly on `main`
- Always branch from `develop`
- Always use Pull Requests
- Write meaningful commit messages

---
