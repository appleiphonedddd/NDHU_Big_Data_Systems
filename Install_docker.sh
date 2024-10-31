#!/bin/bash

# Update and install prerequisites
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Set up the stable Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# Update package index and install Docker CE
sudo apt update
sudo apt install -y docker-ce

# Check Docker status
sudo systemctl status docker --no-pager

# Add the current user to the Docker group
sudo usermod -aG docker "$USER"

# Refresh group membership without logging out and back in
newgrp docker

# Confirm user groups
groups "$USER"

# Print a success message
echo "Docker installed successfully. User $USER has been added to the Docker group."
