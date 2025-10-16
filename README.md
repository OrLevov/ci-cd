# 🚀 CI/CD Pipeline Project  

This project demonstrates a **complete CI/CD workflow** — from testing and containerization to automated deployment on a Kubernetes cluster, all using modern DevOps best practices.  

---

## 🧩 Project Structure  

```bash
CICD/
├── .github/workflows/
│   └── ci-cd.yaml          # CI/CD workflow definition
│
├── app/
│   ├── index.html          # Frontend UI
│   ├── script.js
│   └── styles.css
│
├── backend/
│   ├── app.py              # FastAPI backend
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_mongo_ping.py
│
├── k8s/
│   ├── backend/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── frontend/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── ingress.yaml
│
└── Dockerfile              # Base Docker setup

```
---

## ⚙️ CI/CD Workflow  

Every **push to the `main` branch** triggers the following pipeline automatically:  

### 1️⃣ Test Backend  
- Runs FastAPI unit tests.  
- Verifies MongoDB connectivity.  
- Ensures the backend passes all checks before building.  

### 2️⃣ Build & Push  
- Builds Docker images for both frontend and backend.  
- Pushes images to **GitHub Container Registry (GHCR)**.  

### 3️⃣ Deploy  
- Connects to the remote **Kubernetes cluster on AWS EC2** using an encoded kubeconfig (`BASE64_KUBECONFIG`).  
- Applies new deployments with the latest Git commit SHA.  
- Waits for rollout completion to ensure pods are ready.  

---

## 🧠 Tech Stack  

| Category | Technologies |
|-----------|--------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | FastAPI (Python) |
| **CI/CD** | GitHub Actions |
| **Containers** | Docker |
| **Orchestration** | Kubernetes |
| **Cloud** | AWS EC2 |
| **Secrets Management** | GitHub Secrets |
| **Database (optional)** | MongoDB Atlas |

---

## 🔐 Environment Variables  

| Variable | Description |
|-----------|--------------|
| `ATLAS_URI` | MongoDB Atlas connection URI |
| `BASE64_KUBECONFIG` | Encoded kubeconfig for cluster access |
| `DOMAIN` | Application domain (e.g., `<PUBLIC_IP>.nip.io`) |
| `REPO_LC` | Repository name used for GHCR image tagging |

---

## 🌍 Deployment  

Once deployed, the app is accessible via:  
👉 **http://<PUBLIC_IP>.nip.io**

- Frontend and backend communicate internally through Kubernetes Services.  
- Requests are routed externally via the **NGINX Ingress Controller**.

---

## 💡 What I Learned  

This project helped me strengthen my DevOps skills by building a **real-world CI/CD pipeline** from scratch, including:  
- Automated testing and deployment workflows  
- Building and pushing Docker images  
- Managing Kubernetes manifests  
- Handling secrets securely  
- Deploying a full stack (frontend + backend) system on AWS  

---
