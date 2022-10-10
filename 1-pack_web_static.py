#!/usr/bin/python3
"""
Creates .tgz archive for web_Static
"""

from fabric.api import *
from datetime import datetime

def do_pack():
    """
    packing webstatic files
    """

    try:
        dateT = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir versions")
        file_dir = "versions/web_static_{}.tgz".format(dateT)
        local("tar -cvzf {} web_static".format(file_dir))
        return file_dir

    except:
        return None
