# Django Project Setup Guide

Welcome to our Django project! This guide will walk you through the setup process to get your development environment up and running.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.8 or newer)
- pip (Python package installer)
- Virtualenv (optional, but recommended for managing Python packages)
- PostgreSQL (Ensure you have a PostgreSQL instance ready)

### 1. Clone the Repository

First, clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/scientiststwin/bs-backend
cd bs-backend
```

### 2. Create a Virtual Environment OR PipEnv (Optional)


It's recommended to create a virtual environment for your project dependencies. You can do this by running:

```bash
Copy code
python -m venv venv
```
Activate the virtual environment:

On Windows: `venv\Scripts\activate`
On macOS/Linux: `source venv/bin/activate`

### 3. Install Dependencies

Install the project dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Setup `.env` File
For environment variables, you need to create a .env file in the project root directory. Use the .env.example file as a template:

```bash
cp .env.example .env
```

### 5. Run Database Migrations
With your PostgreSQL database configured and your environment variables set, run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 6. Running the Application
**Finally**, to start the Django development server, run:

```bash
python manage.py runserver
```

