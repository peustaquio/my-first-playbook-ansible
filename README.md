Markdown
# Kubernetes Edge Computing Lab for Telecom

## Overview

This repository contains a complete local development platform simulating a high-performance, edge computing infrastructure tailored for telecom and networking customers. The project demonstrates advanced Kubernetes concepts, Infrastructure as Code (IaC) with Ansible, and SRE/Observability automation with Python, mirroring the responsibilities required for platform-level roles.

## Architecture & Concepts Demonstrated

* **Kubernetes (KinD):** Control plane, worker nodes, and core networking infrastructure.
* **Edge Routing (Camada 7):** Nginx Ingress Controller managing incoming traffic for `borda.operadora.com`.
* **Application Resiliency:** Deployment managing a ReplicaSet with 3 pods of Nginx, configured with a custom ConfigMap for native metric exposition.
* **Network Security & Routing:** Native Docker port mapping (port 80) simulating public internet access from the host machine and enabling internal WSL/Ubuntu communication.
* **Infrastructure as Code (IaC):** Ansible playbooks for automated cluster deployment.
* **SRE/Monitoring:** Python script utilizing Liveness/Readiness probe concepts to monitor L7 latency and active connections.

---

## Getting Started

### Prerequisites

* Docker Desktop (running on Windows with WSL2 integration)
* `kubectl` and `kind` CLI tools
* Ansible (installed within WSL Ubuntu)
* Python 3 (with `requests` library installed)

### 🚀 Step 1: Cluster Setup & Application Deployment

You don't need to manually apply multiple YAML files. Utilize the provided Ansible playbook to create the namespace and deploy the entire infrastructure in the correct order:

```bash
ansible-playbook deploy-lab.yml
Verify that all components (Deployment, ReplicaSet, Pods, Services, and Ingress) are running perfectly in the telecom-edge namespace:

Bash
kubectl get all -n telecom-edge
🐍 SRE & Monitoring Automation
The project includes a custom observability tool written in Python (check_edge_health.py) to monitor the health and performance of the Edge cluster.

Network Architecture Note
Instead of relying on unstable port-forwards, the script leverages the native port 80 mapping exposed by Docker into the WSL environment. It injects the custom HTTP Host header to correctly bypass Ingress domain rules.

Running the Health Check Script
Execute the Python monitor directly from your WSL Ubuntu terminal:

Bash
python3 check_edge_health.py
Expected Output:

Bash
📡 Iniciando monitoramento em: [http://127.0.0.1:80/metrics](http://127.0.0.1:80/metrics)

🟢 [SUCCESS] Status: 200 | Latência: 11.89ms
📊 Active connections: 1
💥 Chaos Engineering & Self-Healing Simulation
To understand real-world SRE operations, you can simulate a critical edge link failure and observe how the automated infrastructure responds.

Start the Monitor in a Loop (Terminal 1):

Bash
while true; do python3 check_edge_health.py; echo "---"; sleep 2; done
Simulate the Disaster - Delete the Ingress Router (Terminal 2):

Bash
kubectl delete ingress telecom-edge-ingress -n telecom-edge
Observe Terminal 1 instantly triggering a visual alert: 🟡 [WARNING] Cluster respondeu com código de erro: 404

Automated Recovery via IaC (Terminal 2):

Bash
ansible-playbook deploy-lab.yml
The Ansible playbook will enforce idempotency, scan the environment, detect the missing Ingress component, and restore it seamlessly. Terminal 1 will immediately recover to: 🟢 [SUCCESS].

🗂️ Version Control & Rollback Strategy
This entire infrastructure is managed as code using Git. Every milestone follows the Conventional Commits standard (feat:, fix:, docs:).

In production environments, direct pushes to the main branch are restricted. Changes must follow the Pull Request (PR) workflow, requiring continuous integration (CI) green lights and senior code reviews before deployment. If a malicious or broken state reaches production, native Git operations allow an instant rollback to the last stable hash ID.


---