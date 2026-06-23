# Dev Enablement Toolkit

A CLI tool that helps engineers monitor and manage infrastructure.

## Features
- Kubernetes health checker — inspect pod status across namespaces
- GitHub Actions trigger — trigger and monitor workflows via API
- Deployment report generator — summarise cluster state

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python cli.py health
python cli.py health --namespace kube-system
python cli.py trigger
python cli.py report
```