# FlashIntel

FlashIntel provides actionable intelligence and workflow automation for go-to-market teams. This repository will host all major components of the platform.

## Architecture Overview

The system is split into a **backend** for the API and background workers and a **frontend** for the web application. Supporting services such as Postgres and Redis are orchestrated through `docker-compose`. A high-level view of the planned components is shown below:

- **Postgres** – main relational database
- **Redis** – message broker and caching layer
- **API** – backend service exposing application logic
- **Worker** – background job processor
- **Web** – frontend React application

## Basic Setup

1. Install [Docker](https://www.docker.com/) and `docker-compose`.
2. Clone the repository and change into the project directory.
3. Start the services:
   ```bash
   docker-compose up
   ```
4. The API and web interfaces will be available once the services build successfully.

Detailed configuration will be added as each service is implemented.
