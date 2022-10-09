#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo 'Holberton School' | /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

#sed -i '/displaying a 404./ a\\t\talias /data/web_static/current/;' /etc/nginx/sites-enabled/default

service nginx restart
