# 🚀 Azad's Docker Learning Project – Flask + Redis Visitor Counter

This project is a fun and simple way to learn Docker by building a Flask web application that uses Redis to count page visits. It includes clean styling, a personalized touch, and a multi-container Docker setup.

---

## 📸 Preview

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a4eb7db8-d04c-44e0-9789-dd68898be8f2" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/09863e0e-c074-4880-86f8-12de4c1a79ac" />


> *Styled homepage with background gradient and visit counter*

---

## 🛠 Tech Stack

- **Python + Flask** – Backend Web App
- **Redis** – Count tracker (in-memory DB)
- **Docker & Docker Compose** – Container orchestration
- **HTML + CSS** – Frontend styling



---

## 🐳 Running with Docker

### 🔧 Step 1: Clone this repo
```bash
git clone https://github.com/azad/docker-learning.git

cd docker-learning/python-redis-challenge
```

---

### 🧱 Step 2: Start containers

```bash
docker-compose up --build
```
### 🌐 Step 3: Open in browser

Visit: http://127.0.0.1:5002

---

### 🧠 Features
Tracks visitor count using Redis

Two routes:

/ – Welcome screen

/count – See how many times it’s been visited

Responsive and styled with a clean CSS layout

Configurable Redis host/port via environment variables

---

### 📚 What I Learned
Dockerfile basics and multi-service orchestration with docker-compose

-Networking between containers

-Flask routing and HTML rendering

-Redis commands in Python

-Serving static files inside containers







