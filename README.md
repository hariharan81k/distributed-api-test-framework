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


## Testing Capabilities

The framework validates API behavior across multiple HTTP operations and distributed service versions.

### HTTP Operations

| Operation | Purpose | Example Endpoint | Expected Result |
|---|---|---|---|
| GET | Retrieve user information | `/users/1` | `200 OK` |
| GET | Validate missing user | `/users/999` | `404 Not Found` |
| POST | Create a new user | `/users` | `201 Created` |
| PUT | Replace user information | `/users/1` | `200 OK` |
| PATCH | Partially update user information | `/users/1` | `200 OK` |
| DELETE | Delete a user | `/users/1` | `200 OK` |

### Response Validation

The framework validates:

- HTTP status codes
- Expected JSON fields
- JSON field values
- Required response fields
- API version
- Service health status

Example:

```python
ResponseValidator.assert_status(
    response,
    200
)

ResponseValidator.assert_json_field(
    response,
    "version",
    expected_version
)


## CI/CD Pipeline

The project uses GitHub Actions to automatically build and execute the distributed API test framework.

The CI pipeline runs on:

- Push to `main`
- Pull requests targeting `main`

### CI Workflow

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout source code
    │
    ├── Build Docker images
    │
    ├── Start API v1 and API v2
    │
    ├── Run API v1 tests
    │
    ├── Run API v2 tests
    │
    ├── Generate test reports
    │
    └── Upload reports as artifacts