# Secure Notes API

This project is a secure notes API designed to allow users to create, view, and manage their personal notes. It is built with Python, leveraging FastAPI for the backend, and Docker for containerization. The application is designed to be a simple, secure solution for storing notes, with built-in testing.

## Features

- **CRUD Operations**: Create, read, update, and delete notes securely.
- **Authentication**: Simple JWT-based authentication.
- **Testing**: Unit tests for API endpoints using `pytest`.
- **Containerization**: Dockerized application for easy deployment.
- **Environment Variables**: Configured to handle sensitive data securely.

## Tech Stack

- **FastAPI**: Fast, modern web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI server for serving FastAPI applications.
- **Docker**: Containerized for easy deployment and scalability.
- **Pytest**: Testing framework for unit and integration testing.
- **JWT**: Used for secure user authentication.

## Getting Started

### Prerequisites

- Python 3.9+ 
- Docker (optional for containerization)

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/cybmin/secure-notes-api.git
   cd secure-notes-api
pip install -r app/requirements.txt


uvicorn app.main:app --reload

docker build -t secure-notes-api .
docker run -p 8000:8000 secure-notes-api

pytest app/test_main.py

### API Documentation
http://127.0.0.1:8000/docs

### Folder Structure
/app
    ├── Dockerfile            # Dockerfile for containerization
    ├── main.py               # FastAPI application entry point
    ├── requirements.txt      # Project dependencies
    └── test_main.py          # Unit tests for the FastAPI app

### License

### Steps:
1. Create a file named `README.md` in your project root directory (e.g., where the `app` folder is).
2. Paste the above content into the `README.md` file.
3. Save and close the file.
4. Commit and push this file to GitHub using these commands:
   ```bash
   git add README.md
   git commit -m "Add README"
   git push origin main
