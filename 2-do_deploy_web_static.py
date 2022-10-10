#!/usr/bin/python3
"""
A scrript to deplot web_Static files on remote server
"""
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['3.230.166.53', '3.238.228.250']


def do_deploy(archive_path):
    """
    deploys webstatic files
    """

    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[0]
        tmp_path = "/tmp/" + archive_name
        release_path = "/data/web_static/releases/{}".format(
                       archive_name.split('.')[0])

        put(remote_path=tmp_path, local_path=archive_path)
        run("mkdir -p {}".format(release_path))
        run("tar -xvf {} -C {}".format(tmp_path, release_path))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -r {}/web_static".format(release_path))
        run("rm -r {}".format(tmp_path))
        run("rm -r /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception:
        return False
