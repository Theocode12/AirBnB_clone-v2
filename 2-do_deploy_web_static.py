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
	archive = archive_path.split("/")[-1]

        tmp_path = '/tmp/' + archive
        release_path = '/data/web_static/releases/{}/'.format(
            archive.partition('.')[0])

        put(archive_path, tmp_path)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf {} -C {}'.format(tmp_path, release_path))
        run('rm {}'.format(tmp_path))
        run('mv {}web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}web_static/'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        # Task carried out successfully
        print('New version deployed!')
        return True
    except Exception:
        return False
