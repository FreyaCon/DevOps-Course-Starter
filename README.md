# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie. You will need a trello API key and token. Create a trello board and get the trello board id and a to do list id and a done list id. These can be retrived using the trello api end points.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Running the Unit Tests

To run all the unit tests run the command `poetry run pytest` in the terminal.
To run tests in a module run the command `poetry run pytest path\to\test`.

# Provision a VM from an Ansible Control Node

## prerequisites

Ensure the following prerequisites are met:

- Ansible is installed and configured on the control node.
- Necessary permissions and credentials to access the VM.

## steps

1. Copy the files in the ansible folder into the control node
2. Run the ansible playbook by running `ansible-playbook playbook.yml -i inventory.ini`
3. Go to http://18.134.222.201:5000/ to see the app

# Running in Docker

To run the app in docker you need docker desktop installed.
Run unit tests:
1. `docker build --target test -t todo_app:test .`
2. `docker run --rm todo_app:test`

Development app run:
1. `docker build --target development --tag todo-app:dev  .`
2. `docker run --env-file .env --publish 5000:5000 --mount type=bind,source="$(pwd)/todo_app",target=/todo_app/todo_app todo-app:dev`

Production app run:
1. `docker build --target production --tag todo-app:prod  .`
2. `docker run --env-file .env --publish 5000:5000 todo-app:prod`

# The Deployed Site

The deployed site can be found at https://freya-to-do-2.azurewebsites.net/. It is hosted on an Azure web app

## How to manually Deploy

To deploy a new version of the app you must run:
1. `docker login`
2. `docker build --target production --tag todo-app:prod  .`
3. `docker push nanofrecon/todo-app:prod`
The azure web app might take some mins to update.
