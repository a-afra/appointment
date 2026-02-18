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

Fill the `.env` file based on `.env.sample` and provide all required
environment variables needed by `settings.py` (e.g., SECRET_KEY,
DEBUG, DATABASE configuration, etc.).

The application will not run correctly if required environment variables
are missing.

### 5. Apply migrations

    python manage.py migrate

### 6. Run server

    python manage.py runserver

------------------------------------------------------------------------

## Authentication (Djoser + JWT)

Base path:

    /auth/

### User Management Endpoints

| Method | Endpoint        |
|--------|-----------------|
| POST   | /auth/users/    |
| GET    | /auth/users/me/ |


### JWT Endpoints

| Method | Endpoint        |
|--------|-----------------|
| POST   | /auth/jwt/create/    |
| GET    | /auth/jwt/refresh/ |


------------------------------------------------------------------------

## pre-commit Setup

Enable hooks:

    pre-commit install

pre-commit ensures formatting, linting, and quality checks before
commits.

------------------------------------------------------------------------
