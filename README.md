# Cloud-Native Microservices System (FastAPI, Docker)

## Overview

This project is a **cloud-native backend system** built using **FastAPI
microservices** to demonstrate real-world software engineering concepts
such as **modular design, REST API development, service communication,
and containerization**.

The system consists of three independent services:

-   **Auth Service** -- handles user registration and login
-   **Analytics Service** -- tracks user activity events
-   **Notification Service** -- handles user notifications (simulated
    delivery)

This project is designed as a **learning-focused implementation** of
microservice architecture and backend engineering best practices.

------------------------------------------------------------------------

## Architecture

    Client → Auth Service
              → Analytics Service (records login events)
              → Notification Service (sends alerts/logs)

Each service: - Runs independently
- Exposes REST APIs
- Has its own `/health` endpoint
- Can be containerized and deployed separately

------------------------------------------------------------------------

## Services

### Auth Service

Responsible for user authentication.

**Features:** - User registration and login
- Token-based authentication (UUID)
- Sends login events to Analytics service

**Endpoints:** - POST `/register`
- POST `/login`
- GET `/health`

------------------------------------------------------------------------

### Analytics Service

Responsible for tracking and analyzing user activity.

**Features:** - Receives events from Auth service
- Tracks actions per user and globally
- Provides basic metrics for observability

**Endpoints:** - POST `/events`
- GET `/metrics/actions`
- GET `/metrics/user/{user_id}/actions`
- GET `/health`

------------------------------------------------------------------------

### Notification Service

Responsible for handling notifications.

**Features:** - Receives notification requests
- Simulates delivery by logging messages
- Designed to be extended for email/SMS in the future

**Endpoints:** - POST `/notify`
- GET `/health`

------------------------------------------------------------------------

## Tech Stack

-   **Language:** Python
-   **Framework:** FastAPI
-   **API Style:** REST
-   **Containerization:** Docker
-   **Version Control:** Git & GitHub
-   **Development Tools:** VS Code, Uvicorn
-   **Environment:** Linux-based containers

------------------------------------------------------------------------

## Running Services Locally (Without Docker)

Each service can be run independently.

Auth Service:

``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Analytics Service:

``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

Notification Service:

``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
```

Swagger UI for testing APIs: - Auth: http://127.0.0.1:8000/docs
- Analytics: http://127.0.0.1:8001/docs
- Notification: http://127.0.0.1:8002/docs

------------------------------------------------------------------------

## Running with Docker

Each service includes its own Dockerfile.

Example for Auth Service:

``` bash
docker build -t auth-service .
docker run -p 8000:8000 auth-service
```

Repeat similarly for: - analytics-service (port 8001)
- notification-service (port 8002)

------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates:

-   REST API development using FastAPI
-   Microservices architecture design
-   Service-to-service communication
-   Event tracking for observability
-   Docker-based containerization
-   Modular backend system design
-   Debugging and system improvement through metrics

