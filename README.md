# simple-cli

## Setting up Development Environment
1. You'll need Python 2, pip and virtualenv available on your system.  On a CentOS machine, you can install pip and virtualenv by:
    ```bash
    yum install -y python-pip
    pip install virtualenv
    ```

1. Fork and close this repository

    ```bash
    git clone http://github.com/<your_git_username>/simple-cli
    cd simple-cli
    ```
1. Create a virtualenv and install the requirements
    ```bash
    virtualenv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    ```
1. Install the CLI in the virtual environment
    ```bash
    pip install --editable .
    ```
1. Setup whatever IDE you prefer to work with. You can access the CLI in the terminal directly in the virtual environment