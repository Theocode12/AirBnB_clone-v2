#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
apt-get update
sudo apt install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo 'Holberton School' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/displaying a 404./ a\\t\talias /data/web_static/current/;' /etc/nginx/sites-enabled/default

sudo service nginx restart
