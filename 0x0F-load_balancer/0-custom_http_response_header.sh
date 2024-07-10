#!/usr/bin/env bash
# Configures nginx in an ubuntu machine

sudo apt-get update -y
sudo apt-get upgrade -y
# -y flag: Automatic yes to prompts
sudo apt install nginx -y

sed -i '/listen 80 default_server/i add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
sudo service nginx restart
