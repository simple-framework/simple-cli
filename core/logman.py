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


""" Manager of Log Files and stdout logs for the Framework and the CLI """

import logging
import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=settings.LOG_LEVEL_STDOUT,
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LogMan:
    """ Class to manage logs for the entire application """

    executor_loggers = {}
    backend_loggers = {}


    @staticmethod
    def register_executor_logger(executor_name):
        """ register a new logger for an executor type i.e. puppet, compiler, ..."""
        executor_logger = logging.getLogger(executor_name)
        LogMan.executor_loggers[executor_name] = executor_logger
        executor_logger.addHandler(LogMan.__new_stream_handler())
        executor_logger.addHandler(LogMan.__new_file_handler(executor_name))


    @staticmethod
    def register_backend_logger(backend_name):
        """ register a new logger for an execution backend type i.e. ssh, local, ..."""
        backend_logger = logging.getLogger(backend_name)
        LogMan.backend_loggers[backend_name] = backend_logger
        backend_logger.addHandler(LogMan.__new_stream_handler())
        backend_logger.addHandler(LogMan.__new_file_handler(backend_name))

    @staticmethod
    def __new_stream_handler():
        """ default STDOUT log settings """
        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(settings.LOG_LEVEL_STDOUT)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)

        return c_handler

    @staticmethod
    def __new_file_handler(filename):
        """
        Default settings for logs sent to files
        @:param filename: Name of the file to which the logs should be saved. The log directory is decribed in
        settings.py

        """
        # Create handlers
        f_handler = logging.FileHandler(f"{settings.LOG_DIR}/{filename}.log")
        f_handler.setLevel(settings.LOG_LEVEL_FILE)

        # Create formatters and add it to handlers
        f_format = logging.Formatter('%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)

        return f_handler

    @staticmethod
    def get_executor_logger(name):
        if name not in LogMan.executor_loggers:
            LogMan.register_executor_logger(name)
        return LogMan.executor_loggers[name]

    @staticmethod
    def get_backend_logger(name):
        if name not in LogMan.backend_loggers:
            LogMan.register_backend_logger(name)
        return LogMan.backend_loggers[name]
