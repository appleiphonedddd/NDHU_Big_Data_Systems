#!/bin/bash

# Step 1: Download Miniconda Installer
echo "Downloading Miniconda Installer..."
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh

# Step 2: Install Miniconda
echo "Installing Miniconda..."
bash Miniconda3-latest-Linux-x86_64.sh

# Step 3: Configure Miniconda
echo "Configuring Miniconda..."
source ~/.bashrc

# Check Miniconda Info
echo "Checking Miniconda installation..."
conda info

# Step 4: Update Miniconda (optional)
read -p "Do you want to update Miniconda now? (y/n): " update_conda
if [ "$update_conda" == "y" ]; then
    echo "Updating Miniconda..."
    conda update --all -y
fi

echo "Miniconda installation and configuration complete."
