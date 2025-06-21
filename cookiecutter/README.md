# cookiecutter-pypackageによるテンプレート

## 通常のテンプレート

<https://github.com/audreyfeldroy/cookiecutter-pypackage>

```bash
uv pip install -U cookiecutter
```

```bash
cd cookiecutter-pypackage

cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git
```

質問内容は以下である。

```bash
(python-package-templates) bash>~/python-package-templates/cookiecutter$ cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git 
  [1/14] full_name (Audrey Roy Greenfeld): Kuroki-g
  [2/14] email (audreyr@example.com): 64629990+Kuroki-g@users.noreply.github.com
  [3/14] github_username (audreyr): Kuroki-g
  [4/14] project_name (Python Boilerplate): 
  [5/14] project_slug (python_boilerplate): 
  [6/14] project_short_description (Python Boilerplate contains all the boilerplate you need to create a Python package.): 
  [7/14] pypi_username (Kuroki-g): 
  [8/14] version (0.1.0): 
  [9/14] use_pytest (n): 
  [10/14] use_pypi_deployment_with_travis (y): n
  [11/14] add_pyup_badge (n):  
  [12/14] Select command_line_interface
    1 - Typer
    2 - Argparse
    3 - No command-line interface
    Choose from [1/2/3] (1): 
  [13/14] create_author_file (y): 
  [14/14] Select open_source_license
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from [1/2/3/4/5/6] (1): 6
```

## jacebrowning/template-python によるテンプレート

<https://github.com/jacebrowning/template-python?tab=readme-ov-file>

```bash
(python-package-templates) bash>~/python-package-templates/cookiecutter$ cookiecutter gh:jacebrowning/template-python -f

  [1/11] full_name (Your Name): Kuroki-g
  [2/11] email (you@yourdomain.com): 64629990+Kuroki-g@users.noreply.github.com
  [3/11] github_username (jacebrowning): Kuroki-g
  [4/11] github_repo (template-python-demo): 
  [5/11] default_branch (main): 
  [6/11] project_name (TemplateDemo): 
  [7/11] package_name (demo): 
  [8/11] project_short_description (Sample project generated from Jace's Python Template.): 
  [9/11] python_major_version (3): 
  [10/11] python_minor_version (11): 
  [11/11] Select license
    1 - MIT
    2 - Apache-2.0
    3 - AGPL-3.0-only
    4 - Unlicense
    Choose from [1/2/3/4] (1): 4
```