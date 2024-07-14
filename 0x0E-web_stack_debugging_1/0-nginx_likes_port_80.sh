#!/usr/bin/env bash
# debugging task: Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs

rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
service nginx restart
