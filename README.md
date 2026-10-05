# Distributed API Test Framework

A containerized distributed API test automation framework built using Python, pytest, Docker, Docker Compose, and GitHub Actions.

The framework validates multiple API service versions independently and runs automated tests against isolated Docker containers.

## Key Features

- Python-based API test automation
- pytest test framework
- Reusable API client abstraction
- Parameterized API tests
- Response validation
- Request and response logging
- Configurable API timeout
- Error handling for timeout and connection failures
- Dockerized test environment
- Multiple API service versions (v1 and v2)
- Docker Compose orchestration
- Health checks and service readiness
- Parallel test execution with pytest-xdist
- HTML and JUnit test reports
- GitHub Actions CI/CD
- Automated CI test report artifacts

## Architecture

The framework uses Docker containers to create isolated API service environments and dedicated test runners.

```text
                         GitHub Actions
                              │
                              ▼
                    ┌───────────────────┐
                    │   CI Pipeline     │
                    │  Build & Execute  │
                    └─────────┬─────────┘
                              │
                    Docker Compose
                              │
             ┌────────────────┴────────────────┐
             │                                 │
             ▼                                 ▼
      ┌──────────────┐                  ┌──────────────┐
      │   API v1     │                  │   API v2     │
      │  Container   │                  │  Container   │
      │   :8000      │                  │   :8000      │
      └──────┬───────┘                  └──────┬───────┘
             │                                 │
             ▲                                 ▲
             │                                 │
      ┌──────┴───────┐                  ┌──────┴───────┐
      │ API Tests v1 │                  │ API Tests v2 │
      │  Container   │                  │  Container   │
      │    pytest    │                  │    pytest    │
      └──────────────┘                  └──────────────┘
             │                                 │
             └────────────┬────────────────────┘
                          ▼
                  Test Reports
                HTML + JUnit XML
                          │
                          ▼
                  GitHub Artifacts

## Project Structure

```text
distributed-api-test-framework/
│
├── framework/
│   ├── api_client.py
│   ├── config.py
│   └── response_validator.py
│
├── tests/
│   ├── test_data/
│   │   └── user_data.py
│   │
│   ├── conftest.py
│   ├── test_get_user.py
│   ├── test_create_user.py
│   ├── test_update_user.py
│   ├── test_patch_user.py
│   ├── test_delete_user.py
│   ├── test_timeout.py
│   ├── test_connection_error.py
│   └── test_distributed_api.py
│
├── mock_services/
│   ├── v1/
│   │   ├── app.py
│   │   └── Dockerfile
│   │
│   └── v2/
│       ├── app.py
│       └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .dockerignore
├── .gitignore
├── compose.yaml
├── Dockerfile
├── pytest.ini
├── requirements.txt
├── README.md
└── run_tests.bat

## Running the Project

### Prerequisites

Make sure the following are installed:

- Python 3.12+
- Docker Desktop
- Git

### Run Distributed Tests

From the project root:

```bash
docker compose up --build