# self-hosted-api-gateway
### High-Performance API Gateway using HAProxy & Nginx on Kubernetes

This project sets up an **API Gateway** capable of handling **100K+ requests per second** using **HAProxy and Nginx** in a Kubernetes cluster. This project is still in progress, firstly it should be deployed on k8s and later will try to port for VM.

### Features
- **High-Performance Load Balancing** using HAProxy & Nginx
- **Auto-Scaling** based on request load
- **Prometheus Integration** for monitoring
- **Lightweight Flask Backend** to test scaling
- **Namespace Isolation** for better organization (`app`, `haproxy`, `nginx`)

## TODO
- **Setup Auth with LUA**  JWT verification
- **Setup Rate Limit with LUA**
- **Test Results** Post Test Results
- **Connection Pooling**
- **Caching**
- **Payload Compression**


### Setup & Deployment

#### Install Kubernetes & Helm
Ensure you have a **Kubernetes cluster** running (e.g., Kind, Minikube, or a real cluster) and **Helm** installed.

#### Deploy API Gateway Components
Apply the Kubernetes manifests:
```sh
kubectl apply -f manifests/
