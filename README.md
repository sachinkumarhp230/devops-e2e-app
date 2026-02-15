# DevOps E2E Application (CI Layer)

This repository contains the application source code and CI pipeline configuration for a production-style DevOps platform built using GitOps principles.

It is responsible for building, testing, and publishing Docker images.

Deployment to Kubernetes is handled separately via ArgoCD using a GitOps repository.

---

## 🎯 Responsibilities

This repository owns:

- Application source code
- Unit tests
- Dockerfile
- Jenkins CI pipeline
- Docker image publishing

This repository does NOT:

- Deploy directly to Kubernetes
- Apply Kubernetes manifests
- Provision infrastructure
- Access the cluster via kubectl

CI and CD responsibilities are strictly separated.

---

## 🔁 CI Workflow

When code is pushed to the `main` branch:

1. Jenkins checks out the repository.
2. Tests are executed inside a Docker-based Python agent.
3. A Docker image is built.
4. The image is pushed to Docker Hub.
5. Jenkins updates the GitOps repository with the new image tag.
6. ArgoCD detects the Git change and deploys automatically.

The CI pipeline does NOT run `kubectl apply`.

Deployment is fully Git-driven.

---

## 🧪 Running Tests Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

---

## 🐳 Build & Run Docker Image Locally

```bash
docker build -t sachinaws751/devops-e2e-app:local .
docker run -p 8080:8080 sachinaws751/devops-e2e-app:local
```

---

## 📦 Docker Image Repository

Docker Hub:

docker.io/sachinaws751/devops-e2e-app

Image tags are versioned using Jenkins build numbers to ensure traceability.

---

## 📂 Repository Structure

```
devops-e2e-app/
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── tests/
```

- `app.py` – Application source code
- `Dockerfile` – Container build definition
- `Jenkinsfile` – CI pipeline definition
- `requirements.txt` – Python dependencies
- `tests/` – Unit tests

---

## 🧠 Design Principles

- Clear separation of CI and CD layers
- Immutable Docker images
- Git as the deployment contract
- No direct CI access to the Kubernetes cluster
- Reproducible builds using Docker agents

---

## 🔗 Related Repositories

- GitOps (CD Layer): `devops-e2e-gitops`
- Infrastructure (IaC Layer): `devops-e2e-infra`

---

## 🚀 Project Objective

This repository is part of a complete DevOps platform designed to demonstrate:

- Automated CI pipelines
- Containerized application builds
- GitOps-based continuous delivery
- Infrastructure as Code (Terraform + EKS)
- Production-style deployment practices
