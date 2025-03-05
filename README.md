# Project structure templates

#### *What is cookiecutter?*

https://www.cookiecutter.io/

https://github.com/cookiecutter/cookiecutter

## How to use:

`pipx run cookiecutter https://github.com/username/cookiecutter-templates-repo --directory="python-webapp-template"`


## Microservices
`pipx run cookiecutter https://github.com/asdede/templates --directory="microservice-template"`

Template for microservice project.

Has basic dockerfiles etc for microservice project:
- App (Front)
- Backend
- API

Has template app or frontend made with streamlit.

## Ai model project
`pipx run cookiecutter https://github.com/asdede/templates --directory="ai-model-project-template"`

Template for training ai models in docker with jupyternotebooks. Works with GPU.

Has most of the Deeplearning and machinelearning libraries in it. 
> Tensorflow and pytorch might need 'reinstall' in pip, since they might use different versions of dependencies.

Includes:
- jupyternotebook in docker
- docs in docker

## Phone app template
`pipx run cookiecutter https://github.com/asdede/templates --directory="phone-app-template"`

Template for react-native phone app projects with backend. Remember that you need Android studio and neccesary libraries etc for it.

Includes:
- Backend in dockerfile
- Documentation in docker

**IMPORTANT**
Dependeciens:
- npm, Node.js

Start with `npm init`

**.gitignore has basics for python and react-native, BUT CHECK IT!!**


#### Setup envivorment

*create env?*

`docker compose up --build`

___