# Kubernetes Edge Computing Lab for Telecom

## Overview

This repository contains a complete local development platform simulating a high-performance, edge computing infrastructure tailored for telecom and networking customers. The project demonstrates advanced Kubernetes concepts, Infrastructure as Code (IaC) with Ansible, and SRE/Observability automation with Python, mirroring the responsibilities required for platform-level roles.

## Architecture & Concepts Demonstrated

* **Kubernetes (KinD):** Control plane, worker nodes, and core networking infrastructure.
* **Edge Routing (Camada 7):** Nginx Ingress Controller managing incoming traffic for `borda.operadora.com`.
* **Application Resiliency:** Deployment managing a ReplicaSet with 3 pods of Nginx, configured with a custom ConfigMap for native metric exposition.
* **Network Security:** Native Docker port mapping (port 80) simulating public internet access from the host machine.
* **Infrastructure as Code (IaC):** Ansible playbooks for automated cluster deployment.
* **SRE/Monitoring:** Python script utilizing Liveness/Readiness probe concepts to monitor L7 latency and active connections.

---

## Getting Started

### Prerequisites

* Docker Desktop (running on Windows with WSL2 integration)
* kubectl
* kind
* Ansible (installed within WSL Ubuntu)
* Python 3 (with `requests` library installed)

### 🚀 Step 1: Cluster Setup & Application Deployment

You don't need to manually apply YAML files. Utilize the provided Ansible playbook to create the namespace and deploy the entire infrastructure in the correct order:

```bash
ansible-playbook deploy-lab.yml