#!/usr/bin/env python3
# Fabfile that defines functions to pack, clean, and deploy
# current directory to a remote server.
from fabric import task


@task
def pack(c):
    """Creates tar gzipped archive of current directory."""
    c.run("touch holbertonwebapp.tar.gz")
    c.run("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


@task
def deploy(c):
    """Uploads archive to remote server in  /tmp/ directory."""
    c.user = "ubuntu"
    c.put("holbertonwebapp.tar.gz", "/tmp")
    c.run("mkdir /tmp/holbertonwebapp")
    c.run("tar -C /tmp/holbertonwebapp -xzvf /tmp/holbertonwebapp.tar.gz")


@task
def clean(c):
    """Deletes holbertonwebapp.tar.gz on local machine."""
    c.run("rm holbertonwebapp.tar.gz")
