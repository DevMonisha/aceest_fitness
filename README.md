# ACEest Fitness and Gym

A Flask-based web application for managing a fitness and gym system.  
This project demonstrates core functionalities including member and trainer management, workout tracking, and API health monitoring. It is designed with DevOps practices in mind, including Docker containerization and CI/CD pipeline integration.

## Features

- **Home Page:** A welcome endpoint to confirm the application is running.
- **Members Management:** View a list of gym members with details like name, age, and membership type.
- **Trainers Management:** View a list of trainers and their specialties.
- **Workouts Management:** 
  - List all workouts.
  - Add new workouts with title and duration.
  - Delete existing workouts.
- **Health Check:** An endpoint to monitor the API status.
- **Unit Testing:** Pytest-based unit tests for core functionalities.
- **Dockerized:** Application packaged in a Docker container for consistent deployment.
- **CI/CD:** Automated build and testing pipeline using GitHub Actions.

## Prerequisites

Before running the application locally or in Docker, ensure you have the following installed:

- **Python 3.11** (or compatible)
- **pip** (Python package manager)
- **Docker** (for containerization)
- **Git** (for version control)
- **GitHub account** (for CI/CD integration)

Optional but recommended:

- **VS Code** or any IDE for Python development
- **Postman** or a browser for testing API endpoints

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd aceest_fitness
```

### 2. Create and Activate Virtual Environment
#### Windows
```bash 
python -m venv .venv
.\.venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
``` 
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application Locally
```bash
python -m aceest_fitness.app
```

### 5. Run the Application in Docker

  #### Build Docker image
  ```bash
  docker build -t aceest_fitness:latest .
  ```

  #### Run Docker container
  ```bash
  docker run -p 5000:5000 -e PYTHONPATH=/app aceest_fitness:latest
  ```

## Running Tests

### 1. Running Tests Locally
Make sure your virtual environment is active:
```bash
# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate

```

#### 1. Running Tests in Docker
```bash
docker run -it --rm -e PYTHONPATH=/app aceest_fitness:latest pytest -v
```
![alt text](image.png)