# -*- coding: future_fstrings -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import logging
from os import system
from paramiko import SSHClient, AutoAddPolicy, RSAKey, PasswordRequiredException
from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException

from core.logman import LogMan

""" Handle connections and actions with remote hosts """


logger = LogMan.get_backend_logger('remote_client')


class RemoteClient:
    """ Client to interact with remote host via SSH & SCP """

    def __init__(self, host, user, ssh_key_filepath, password=None ,remote_path='/'):
        self.host = host
        self.user = user
        self.password = password
        self.ssh_key_filepath = ssh_key_filepath
        self.remote_path = remote_path
        self.client = None
        self.scp = None
        self.__upload_ssh_key()

    def __get_ssh_key(self):
        """Fetch locally stored SSH key."""
        try:
            self.ssh_key = RSAKey.from_private_key_file(self.ssh_key_filepath)
            logger.info('Found SSH key at self {self.ssh_key_filepath}')
        except SSHException as error:
            logger.error(error)
        return self.ssh_key

    def __upload_ssh_key(self):
        try:
            system(f'ssh-copy-id -i {self.ssh_key_filepath} {self.user}@{self.host}>/dev/null 2>&1')
            system(f'ssh-copy-id -i {self.ssh_key_filepath}.pub {self.user}@{self.host}>/dev/null 2>&1')
            logger.info(f'{self.ssh_key_filepath} uploaded to {self.host}')
        except IOError as error:
            logger.exception(error)

    def __connect(self):
        """Open connection to remote host.
        @:raises PasswordRequiredException if private key file is encrypted. This should be handled by CLI by asking the
        password from the user at the command line.
        @:raises AuthenticationException if the user failed to specify proper ssh keys. The CLI should print the exception
        and exit.
        """
        try:
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(AutoAddPolicy())
            if self.password is not None:
                self.client.connect(self.host,
                                    username=self.user,
                                    password = self.password,
                                    key_filename=self.ssh_key_filepath,
                                    look_for_keys=True,
                                    timeout=5000)
            else:
                self.client.connect(self.host,
                                    username=self.user,
                                    key_filename=self.ssh_key_filepath,
                                    look_for_keys=True,
                                    timeout=5000)
            self.scp = SCPClient(self.client.get_transport())
        except PasswordRequiredException as error:
            logger.exception(error)
            raise error
        except AuthenticationException as error:
            logger.info('Authentication failed: did you remember to create an SSH key?')
            logger.error(error)
            raise error
        return self.client

    def disconnect(self):
        """Close ssh connection."""
        self.client.close()
        self.scp.close()

    def execute_commands(self, commands):
        """Execute multiple commands in succession."""
        if self.client is None:
            self.client = self.__connect()
        for cmd in commands:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            for line in response:
                logger.info(f'INPUT: {cmd} | OUTPUT: {line}')

    def bulk_upload(self, files):
        """Upload multiple files to a remote directory."""
        if self.client is None:
            self.client = self.__connect()
        uploads = [self.__upload_single_file(file) for file in files]
        logger.info(f'Uploaded {len(uploads)} files to {self.remote_path} on {self.host}')

    def __upload_single_file(self, file):
        """Upload a single file to a remote directory."""
        try:
            self.scp.put(file,
                         recursive=True,
                         remote_path=self.remote_path)
        except SCPException as error:
            logger.error(error)
            raise error
        finally:
            return file

    def download_file(self, file):
        """Download file from remote host."""
        if self.conn is None:
            self.conn = self.connect()
        self.scp.get(file)