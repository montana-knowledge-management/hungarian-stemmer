# Template repository for distiller based projects

[![tests](https://github.com/montana-knowledge-management/distiller-based-plugin-template/actions/workflows/ci.yml/badge.svg)](https://github.com/robust/actions)
[![codecov](https://codecov.io/gh/montana-knowledge-management/distiller-based-plugin-template/branch/main/graph/badge.svg?token=KMYGW7NHWH)](https://codecov.io/gh/montana-knowledge-management/distiller-based-plugin-template)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/montana-knowledge-management/distiller-based-plugin-template.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/montana-knowledge-management/distiller-based-plugin-template/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/montana-knowledge-management/distiller-based-plugin-template.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/montana-knowledge-management/distiller-based-plugin-template/context:python)

## How to use this template?

### Install `poetry`

If you didn't use `poetry` before, then you have to install it.
The documentation can be found [here](https://python-poetry.org/docs/).

1. Download the installer script somewhere:

    **Note**: Make sure you don't have any virtual environment active in your terminal.
    ```shell
    curl -O https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py
    ```
2. Run the installation script:
   ```shell
   python3 install-poetry.py
   ```
   Pay attention to the script output, you might have to append the line below at the end of your `.bashrc` file.
   ```shell
   export PATH="$HOME/.poetry/bin:$PATH"
   ```

### Installing dependencies
At this stage you should have poetry installed on your system. The next step is to create a virtual environment and install
the project dependencies:
```shell
poetry install
```
This command will create a `.venv` directory into the repository and install all dependeny.

**Note**: If you are using Pycharm, then you should install the poetry plugin.

#### Troubleshooting

If `poetry` throws a `JSONEncodeEerror` you should clear the `poetry` cache:
```shell
rm -rf ~/.cache/pypoetry
```

### Badges

Open this `README.md` file with your favorite editor and use its _Search and Replace_ function. 
Search for `distiller-based-plugin-template`  and replace it with the repository name.

### Package description

Open the `pyproject.toml` file and change the relevant fields in the first section (`[tool.poetry]`):
`<PACKAGENAME>`, `<DESCRIPTION>`

### Making the source directory

Create the source directory with the name of your choice. After that open the `pyproject.toml` file and 
replace `src` with the directory name int the `[tool.coverage.run]` section.

In the `.pre-commit-config.yaml` file the `pylint` section has a `files: '^src/'` row. Replace
the `src` part with the source directory name.

### Install `pre-commit` hooks

Use this command to install `pre-commit` hooks. They will run before each commit and will correct your files to meet 
the requirements:
```shell
pre-commit install --hook-type commit-msg --overwrite
pre-commit install --hook-type=pre-commit --overwrite
```

## Development

Run tests and calculating the coverage automatically:
   ```shell
   poetry run coverage run
   ```
   
   Generating an html from the results
   ```shell
   poetry run coverage html
   ```
   
   If your virtualenv is activated you can omit `poetry run` from the commands.
   
   Here is the compact form:
   ```shell
   clear;coverage run;coverage html;coverage report
   ```