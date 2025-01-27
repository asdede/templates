# Project structure templates

#### *What is cookiecutter?*

https://www.cookiecutter.io/

https://github.com/cookiecutter/cookiecutter

## How to use:

`pipx run cookiecutter https://github.com/username/cookiecutter-templates-repo --directory="python-webapp-template"`


## Microservices
`pipx run cookiecutter https://github.com/asdede/templates --directory="microservice-template"`

## Ai model project
`pipx run cookiecutter https://github.com/asdede/templates --directory="ai-model-project-template"`

Template for training ai models in docker with jupyternotebooks. Works with GPU.

Has most of the Deeplearning and machinelearning libraries in it. 
> Tensorflow and pytorch might need 'reinstall' in pip, since they might use different versions of dependencies.

Includes:
- jupyternotebook in docker
- docs in docker

#### Setup envivorment

*create env?*

`docker compose up --build`

___