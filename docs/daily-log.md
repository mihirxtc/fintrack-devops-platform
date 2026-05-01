# Logs regarding incidents 

## Day 1 — Local Environment Setup

### What I did
- Installed all required DevOps tools: git, docker, kubectl, 
  terraform, aws-cli, helm, python3, jq, curl
- Created GitHub repository: fintrack-devops-platform
- Set up correct folder structure: app, terraform, k8s, 
  monitoring, scripts, docs, .github/workflows
- Configured .gitignore for Terraform, Python, secrets
- Created IAM user in AWS, configured aws-cli
- Used feature branch setup/local-environment instead of 
  committing directly to main
- Opened PR and merged to main

### What I learned
- Never use root AWS credentials programmatically
- Always use IAM users with least privilege
- .gitignore prevents secrets and junk files entering the repo
- Branch protection — always work on feature branches
- AWS Account ID should never be shared publicly
- Document architectural decisions with reasons, not just outcomes

### Region Decision
- Using us-east-1 instead of eu-west-2 due to existing 
  university project resources in that region
  To be revisited after university project completion

### Tools Installed & Versions
- git 2.54.0
- Docker 29.4.1
- kubectl v1.32.13

## Day 2 — Containerisation

### What I did
- Built Dockerfile for FinTrack Flask API
- Used Alpine base image, non-root user, gunicorn
- Created docker-compose with healthcheck and named network
- Created .dockerignore

### What I learned
- Docker layer caching — copy what changes least first
- HTTP status codes — 400 bad request, 404 not found, 201 created
- Gunicorn vs Flask dev server
- app:app in gunicorn = filename:flask-variable-name
- Principle of least privilege — never run containers as root

### Incident #001
- Root cause: POST request in API showing error due to it not contained all the required params: description & catagory
- Fix: Upon exploring logs by "docker logs $(docker ps -q) --tail 20" that some params are missing in which requied by POST request
- Status: Resolved

