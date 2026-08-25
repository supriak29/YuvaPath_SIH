# Kaushal Darpan

## SIH 2026 – Team 9

Kaushal Darpan is a longitudinal skilling-outcomes and impact-measurement platform that tracks trainee outcomes after training and certification.

## Project Structure

- `frontend/` – Next.js + React frontend
- `backend/` – FastAPI backend and APIs
- `ai/` – AI/ML and analytics
- `database/` – PostgreSQL schema, migrations and SQL
- `docs/` – ER diagram, API contract, data dictionary and documentation

## Technology Stack

### Frontend
- Next.js
- React
- Tailwind CSS
- Recharts
- Mapbox

### Backend
- FastAPI
- PostgreSQL
- Redis + Celery

### Authentication & Storage
- Firebase Authentication
- Firebase Storage / Object Storage

### AI & Analytics
- Python
- Pandas
- Scikit-learn

## Git Workflow

- `main` – stable version
- `dev` – team integration branch
- `feature/frontend` – frontend development
- `feature/backend` – backend development
- `feature/ai` – AI/ML development
- `feature/database` – database development

Do not directly push to `main` or `dev`.

Create changes in your assigned feature branch and submit a Pull Request to `dev`.

## Development Rule

Before implementing a module, coordinate with the team on:

1. Data Dictionary
2. ER Diagram
3. API Contract
4. Module fields and validation

All modules must use the same agreed data structure.