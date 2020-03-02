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

from core.executors import compiler


class DeploymentManager:
    """

    """
    def __init__(self):
        self.deployments = []
        self.current_deployment = None
        self.deployments = self.load_saved_deployments()
        self.current_deployment = self.get_current_deployment()

    def load_saved_deployments(self):
        """

        :return:
        """
        pass

    def get_current_deployment(self):
        """

        :return: the currently loaded deployment
        """

    def load(self, name):
        """
        Load the deployment to /etc/simple_grid.
        @:param: name: The name of the deployment to be loaded.
        :return:
        """
        try:
            compiler.compile(self.site_config)
        except Exception as error:
            raise error
        pass

    def unload(self, deployment=None):
        """
        Unload the development from /etc/simple_grid.
        If the deployment name is not specified, the currently loaded deployment gets unloaded
        @:param: deployment: Name of the deployment that should be unloaded
        @:raises:
        :return:
        """
        pass

    def list(self):
        """
        :return: list of all deployments
        """
        pass

    def new(self, name):
        """
        @:param name: The name of the new deployment to be created.
        :return:
        """
        pass