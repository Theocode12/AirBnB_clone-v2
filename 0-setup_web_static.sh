#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

sudo apt install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo 'Holberton School' | sudo tee -a /data/web_static/releases/test/index.html > /dev/null

if [ -L /data/web_static/current ]
then
	rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/displaying a 404./ a\\t\talias /data/web_static/current/;' /etc/nginx/sites-enabled/default

sudo service nginx restart
