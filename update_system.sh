#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root"
    exit 1
fi

echo "Update..."
apt update

#The -y option allows to automate /Yes/ confirmation
#Upgrading packages
echo "Upgrade..."
apt upgrade -y

#Removing unnecessary packages
echo "Autoremove..."
apt autoremove -y

#Removes only the package files that can no longer be downloaded
echo "Autoclean..."
apt autoclean -y

echo "Updates completed successfully."