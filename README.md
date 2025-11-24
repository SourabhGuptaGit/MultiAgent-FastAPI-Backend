# 🚀 MultiAgent FastAPI Backend  
An end-to-end **AI-powered multi-agent backend system** built using **FastAPI**, **LangGraph**, **LangChain**, **PostgreSQL**, and **Docker**, designed to showcase modern backend engineering, cloud deployment, and LLM integrations using both **OpenAI** and **Ollama**.

---

## 💡 What This Project Demonstrates

This project highlights my full-stack backend, automation, and DevOps skill set by combining:

### 🧠 AI / LLM Stack
- **LangGraph** (multi-agent workflows + supervisor agent)  
- **LangChain** (tools, agents, structured output)  
- **Ollama** (local LLMs: smollm2, llama models, etc.)  
- **OpenAI GPT-4.1-mini** (production mode)  
- Agent tools for:
  - Email automation (send, read, research)
  - Research assistant workflow
  - Multi-agent supervisor orchestration

### 🐍 Backend Engineering
- **FastAPI** (modular API architecture)
- **Pydantic + SQLModel** (models, validation, ORM)
- **Email automation system** (SMTP, IMAP inbox parser)
- **Production-ready routing & schema design**
- **Clean modular Python code structure**

### 🗄️ Database & Storage
- PostgreSQL (via Docker)
- SQLModel ORM
- Auto-init DB lifecycle using FastAPI lifespan hooks

### 🐳 DevOps, Infra & Deployment
- **Docker** (multi-stage builds, isolated services)
- **Docker Compose** (backend + DB + hot reload)
- **AWS Cloud Infra**
  - VPC, Subnets, IGW
  - EC2 development environment
  - Load balancer, target groups, autoscaling
- **Railway Deployment**
  - Docker build workflow
  - Environment-based LLM switching
- **Git & Linux proficiency**
  - Systemctl service management (Ollama, API)
  - EC2 hardening & environment setup

---

## 🧩 Project Summary

This system implements a **Multi-Agent AI backend** where:

- A **Supervisor agent** coordinates:
  - An **Email Agent** (send/read/generate emails)
  - A **Research Agent** (summaries, research output)
- All agents operate through a unified LLM backend:
  - **OpenAI** when `IS_PROD="True"`
  - **Ollama** in development mode

API endpoints include:
- Chat message creation  
- Email drafting agent  
- Inbox reading agent  
- Supervisor orchestration  

Out of the box, the project supports:
- Sending emails via Gmail SMTP
- Fetching unread emails (IMAP)
- Generating email content with LLMs
- Saving chat history in PostgreSQL
- Providing agent output through FastAPI APIs

This repo acts as a **complete demonstration** of modern backend development, multi-agent AI workflows, and production-grade containerized infrastructure.

---

## 🛠️ Tech Stack Summary

| Category | Skills & Tools |
|---------|----------------|
| **Languages** | Python |
| **Backend** | FastAPI, Pydantic, SQLModel |
| **AI / LLM** | LangGraph, LangChain, Ollama, OpenAI |
| **Database** | PostgreSQL, psycopg |
| **DevOps** | Docker, Docker Compose, Linux, Git |
| **Cloud** | AWS VPC, EC2, Load Balancer, ASG, Railway Deployment |
| **Automation** | Email automation (SMTP/IMAP), research agents |
| **Other** | JSON configs, environment management, virtualenv |

---

## 🧭 Purpose

This project is intentionally designed as an **end-to-end showcase project** that demonstrates my skills across:

- Backend architecture  
- Cloud deployment  
- Multi-agent AI systems  
- DevOps and automation  
- Database design  
- Production-ready API development  

It is fully functional, easy to extend, and ideal for demonstrating engineering capability in real-world AI-driven backend systems.

