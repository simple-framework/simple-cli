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

"""
Represents the models that comprise the SIMPLE ecosystem
"""


class ActionHistory:
    """
    ActionHistory tracks the log_id and the incoming command for the current deployment
    """
    def __init__(self):
        pass


class LCHost:
    """
    Represents a host in the site infrastructure
    """
    def __init__(self, fqdn, ip):
        self.fqdn = fqdn
        self.ip = ip


class LC:
    """
    Represents a Lightweight_Component
    """
    def __init__(self, fqdn, ip, lc_host):
        """

        :param fqdn: FQDN in the overlay network of the LC
        :param ip: IP address in the overlay network of the LC
        :param lc_host: The LCHost on which the container is deployed
        """
        self.fqdn = fqdn
        self.lc_host = lc_host
        self.ip = ip


class Deployment:
    """
    Represents a Deployment in the SIMPLE Framework i.e. contents that can be loaded into the /etc/simple_grid directory
    """

    def __init__(self, name, directory, site_config):
        """

        :param name: Name of the deployment
        :param directory: Actual path of where the deployment is stored
        :param site_config: Actual path of where the site level config file is stored
        """
        self.name = name
        self.directory = directory
        self.site_config = site_config
        self.lc_hosts = []
        self.lc = []
        self.action_history = []
        self.cm = [] #TODO replace with hostname of the current machine?