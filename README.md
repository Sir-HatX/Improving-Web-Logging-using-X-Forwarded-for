# Improving Web Logging using X-Forwarded-For

This project enhances traditional web server logging by incorporating the `X-Forwarded-For` (XFF) HTTP header to more accurately capture the original client IP address—especially useful in environments with proxies, load balancers, or CDN services. By parsing and validating the XFF header, this solution ensures more reliable IP tracking for auditing, analytics, and security monitoring.

## Features

- Extracts original client IPs from `X-Forwarded-For` headers  
- Supports configurable trusted proxy chains  
- Works with popular web servers (e.g., Nginx, Apache) and frameworks  
- Enhances existing logging formats with accurate IP information  
- Mitigates spoofing with optional IP validation  

## Use Cases

- Real client IP logging behind reverse proxies  
- Accurate geolocation and rate-limiting  
- Improved security incident tracing  

## Demo Setup

The architecture below illustrates a typical setup using an Nginx load balancer, Nginx web server, HAProxy, and a Python API container:

![image](https://github.com/user-attachments/assets/3498aeda-2b67-47a9-a802-7f6969c6024f)

---

## Getting Started

Follow the steps below to get the full stack up and running using Docker Compose.

### Prerequisites

- Docker  
- Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/Sir-HatX/Improving-Web-Logging-using-X-Forwarded-for.git
cd Improving-Web-Logging-using-X-Forwarded-for/web_demo
```
### 2. Project Structure
```
.
├── docker-compose.yml
├── image.png
├── haproxy.cfg
├── nginx_web.conf
├── nginx_lb.conf
├── nginx_api/
│   ├── app.py
│   └── Dockerfile
```
### 3. Start the Services
```bash
docker-compose up --build
```
This will start the following services:
- nginx_lb (Load Balancer on port 8000)
- nginx_web (Web server on port 7000)
- haproxy (Proxy on port 6000)
- nginx_api (Python API on port 5000)

### 4. Test the Flow
Visit: http://localhost:8000 and http://localhost:8000/test
Check logs at each layer to verify the correct IP flow using X-Forwarded-For.
Play with it untill you achieve your target outcome :)
Feel free to reachout for support.
![image](https://github.com/user-attachments/assets/68f74e2c-94dc-4be4-bea0-b76d2c67f9b3)

![image](https://github.com/user-attachments/assets/3a346f39-08f0-418b-bebb-eb9bdef2cc16)


