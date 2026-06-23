# Dev Enablement Toolkit

A CLI tool built to improve developer productivity by providing real-time 
visibility into Kubernetes cluster health and GitHub Actions workflows.

Built as a hands-on project to explore Developer Enablement tooling — 
the kind of internal platform work that helps engineering teams ship faster.

## Features

- **Kubernetes Health Checker** — inspect pod status, restart counts, 
  and detect issues like `CrashLoopBackOff` across namespaces
- **GitHub Actions Trigger** — trigger and monitor CI/CD workflows 
  via GitHub API with real-time polling
- **Deployment Report** — summarise cluster state (coming soon)

## Tech Stack

- Python 3.9
- [Click](https://click.palletsprojects.com/) — CLI framework
- [Kubernetes Python Client](https://github.com/kubernetes-client/python) — cluster interaction
- [Rich](https://rich.readthedocs.io/) — terminal formatting
- [Requests](https://requests.readthedocs.io/) — GitHub API calls
- Docker — multi-stage containerisation
- GitHub Actions — CI/CD pipeline (lint → build → docker)

## Setup

### Prerequisites
- Python 3.9+
- kubectl configured with a running cluster
- GitHub Personal Access Token with `repo` and `workflow` scopes

### Install

```bash
git clone https://github.com/khanshakeeb/dev-enablement-toolkit
cd dev-enablement-toolkit

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```bash
GITHUB_TOKEN=your_token_here
GITHUB_OWNER=your_github_username
GITHUB_REPO=your_repo_name
```

## Usage

### Check Kubernetes cluster health
```bash
python cli.py health
python cli.py health --namespace kube-system
```

### Trigger a GitHub Actions workflow
```bash
python cli.py trigger
python cli.py trigger --workflow ci.yml
```

### Generate deployment report
```bash
python cli.py report
```

## Run with Docker

```bash
docker build -t dev-enablement-toolkit .
docker run dev-enablement-toolkit --help
```

## CI/CD Pipeline

Every push to `master` triggers a 3-stage GitHub Actions pipeline:
- **lint** — flake8 code quality checks
- **build** — install dependencies + smoke test
- **docker** — build and verify Docker image

## Project Structure

dev-enablement-toolkit/
```

├── cli.py                      # CLI entry point

├── modules/

│   ├── k8s_health.py           # Kubernetes health checker

│   ├── github_actions.py       # GitHub Actions API client

│   └── report.py               # Deployment report generator

├── .github/

│   └── workflows/

│       └── ci.yml              # CI/CD pipeline

├── k8s/

│   └── deployment.yaml         # Kubernetes manifests

├── Dockerfile                  # Multi-stage Docker build

└── requirements.txt
```