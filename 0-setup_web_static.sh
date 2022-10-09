#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

apt install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'Holberton School' | sudo tee -a /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]
then
	rm /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

sed -i '/displaying a 404./ a\\t\talias /data/web_static/current/;' /etc/nginx/sites-enabled/default

service nginx restart
