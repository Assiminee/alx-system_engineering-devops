#!/usr/bin/env bash

sed -i '/listen 80 default_server/i add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
sudo service nginx restart
