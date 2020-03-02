class DeploymentManager:

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

    def load(self):
        """
        Load the deployment to /etc/simple_grid
        :return:
        """
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

        :return:
        """
