# Infrastructure Setup

This directory contains files related to the deployment of the Reusable Delivery Capability Engine.

## Docker Setup
To run the engine using Docker, you can create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  capability_engine:
    image: capability_engine_image
    build: .
    ports:
      - '5000:5000'
    environment:
      - ENV_VAR=value
```

## Deployment Instructions
1. Ensure Docker is installed on your machine.
2. Run `docker-compose up` to start the service.
3. Access the API at `http://localhost:5000/api`.