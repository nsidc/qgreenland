#!/bin/bash

# Note: Both docker-ce and docker-ce-cli must exist at this version. To check
# available versions:
#     apt-cache madison docker-ce-cli
VERSION="5:19.03.1~3-0~ubuntu-xenial"

apt-get -q remove docker docker-engine docker.io containerd runc
apt-get -q update
apt-get -q install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
apt-get -q update
apt-get -q install -y docker-ce=$VERSION docker-ce-cli=$VERSION containerd.io

curl --silent -L \
  "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

usermod -aG docker vagrant
