from getpass import getpass

import click
import logging

from paramiko import SSHClient, PasswordRequiredException

from core.backends.remote_client import RemoteClient

logging.basicConfig()


def handlePass():
    password = getpass("Enter password: ")
    main(password)

def main(password=None):
    """

    """
    print 'Hello World'
    remote = RemoteClient('voms.cat.cbpf.br', 'maany', '/Users/mayanksharma/.ssh/id_rsa', remote_path='/')
    if password is not None:
        remote = RemoteClient('voms.cat.cbpf.br', 'maany', '/Users/mayanksharma/.ssh/id_rsa', password=password, remote_path='/')
    remote.execute_commands(['ls /'])


if __name__ == "__main__":
    try:
        main()
    except PasswordRequiredException as error:
        handlePass()