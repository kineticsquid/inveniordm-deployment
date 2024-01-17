Docker Images: https://github.com/inveniosoftware/docker-invenio

Getting Sarted: https://inveniordm.docs.cern.ch/install/

1. Install CLI tool
```
pip install invenio-cli
```

2. Check system requirements
```
invenio-cli check-requirements
```

3. Scaffold project¶

Scaffold your InvenioRDM instance. Replace <version> with the version you want to install:

    LTS release (for production systems): v9.1
    STS release (for feature previews): v11.0
```
invenio-cli init rdm -c <version>
```
# e.g:
```
invenio-cli init rdm -c v9.1
```

You will be asked several questions. If in doubt, choose the default.
- project_name: `My Site`
- project_shortname: `my-site`
- project_site: `my-site.com`
- github_repo: `kineticsquid/inveniordm-deployment`
- description: `My test Invenio RDM deployment`
- author_name: `CERN`
- author_email: `kineticsquid@gmail.com`
- year: `2024`
- select python version: `3.9`
- select database: `postgresql`
- select elasticsearch: `7`
- select file_storage: `local`
- select development tools: `yes`

4. Build, setup and run¶

Now that the scaffolding is complete, it is time to check the development requirements
```
cd my-site/
invenio-cli check-requirements --development
```

Wrong Node version: `Errors: Node wrong version.Got [20, 11, 0] expected 14`

You can run the main InvenioRDM application in two modes (choose one):

    Containerized application and services (good for a quick preview).
    Local application with containerized services (good for developers or if you want to customize InvenioRDM).

Containerized application

```
invenio-cli containers start --lock --build --setup
```

Warning: Python 3.9 was not found on your system...
Would you like us to install CPython 3.9.18 with Pyenv? [Y/n]: y


Local application

invenio-cli install
invenio-cli services setup
invenio-cli run

Linux: Managing Docker as a non-root user & Context Errors

If you encounter Docker errors running invenio-cli services setup, see our section on Docker pre-requisites.
5. Explore InvenioRDM¶

Go and explore your InvenioRDM instance on:

    Gitpod: https://5050-inveniosoft-dockerinven-6uekf0cihox.ws-us107.gitpod.io
    Container: https://127.0.0.1

To create a new administrator account:

Containerized application

```
docker exec -it my-site-web-api-1 /bin/bash
docker exec -it ebb5237c96f4 /bin/bash
pipenv run invenio users create kineticsquid@gmail.com --password password --active --confirm
```
In a fully containerized context, connect to a container first e.g. the web-api container: docker exec -it my-site-web-api-1 /bin/bash. Then run the commands from within the container as-is.

Steps The following command creates an activated and confirmed user (assuming you have email verification enabled as is the default).

invenio users create <EMAIL> --password <PASSWORD> --active --confirm

Then, allow the user to access the administration panel:

invenio access allow administration-access user <EMAIL>

6. Stop it¶

When you are done, you can stop your instance and optionally destroy the containers:

Containerized application

To just stop the containers:

invenio-cli containers stop

To destroy them:

invenio-cli containers destroy

Local application

^C [CTRL+C]
invenio-cli services stop

invenio-cli services destroy
