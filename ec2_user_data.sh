#!/bin/bash
set -e

echo "===== Updating system ====="
apt-get update -y
apt-get upgrade -y

echo "===== Installing basic tools ====="
apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    python3 \
    python3-pip \
    python3-venv

echo "===== Installing Docker ====="
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update -y
apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

echo "===== Enabling Docker ====="
systemctl enable docker
systemctl start docker
usermod -aG docker ubuntu

echo "===== Installing Ollama ====="
curl -fsSL https://ollama.com/install.sh | bash

echo "===== Pulling smollm2 model ====="
sleep 8
sudo -u ubuntu ollama pull smollm2 || true

echo "===== Setting up project: AgenticBackend ====="
cd /home/ubuntu
sudo -u ubuntu mkdir -p AgenticBackend
cd AgenticBackend

echo "===== Cloning GitHub repo ====="
# Replace with your repo URL
sudo -u ubuntu git clone https://github.com/SourabhGuptaGit/MultiAgent-FastAPI-Backend.git .

echo "===== Creating Python virtual environment ====="
sudo -u ubuntu python3 -m venv venv

echo "===== Installing Python dependencies ====="
sudo -u ubuntu /home/ubuntu/AgenticBackend/venv/bin/pip install --upgrade pip
sudo -u ubuntu /home/ubuntu/AgenticBackend/venv/bin/pip install -r backend/requirements.txt

echo "===== DONE! Everything is installed and ready ====="
echo "Login via SSH and run docker compose manually inside AgenticBackend/"
