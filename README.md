# Python Development Environment Setup Guide

This guide covers essential setup instructions for Python development environments, package management, and common development workflows.

## Environment Management

### Virtual Environment (venv)

Create a new virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

Deactivate the virtual environment:
```bash
deactivate
```

## Package Management

### Pip (Package Installer for Python)

Install packages:
```bash
pip install package_name
pip install -r requirements.txt
```

Generate requirements.txt:
```bash
pip freeze > requirements.txt
```

Upgrade pip:
```bash
python -m pip install --upgrade pip
```

Install specific version:
```bash
pip install package_name==1.2.3
```

Uninstall package:
```bash
pip uninstall package_name
```

### Poetry

Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Initialize new project:
```bash
poetry new project-name
# or for existing project
poetry init
```

Add dependencies:
```bash
poetry add package_name
poetry add package_name@^2.0.0  # specific version
poetry add --dev pytest  # development dependency
```

Install dependencies:
```bash
poetry install
```

Update dependencies:
```bash
poetry update
```

Generate requirements.txt from Poetry:
```bash
poetry export -f requirements.txt --output requirements.txt
```

Run scripts:
```bash
poetry run python your_script.py
```

### Conda

Create new environment:
```bash
conda create --name myenv python=3.9
```

Activate environment:
```bash
conda activate myenv
```

Install packages:
```bash
conda install package_name
```

Export environment:
```bash
conda env export > environment.yml
```

Create environment from file:
```bash
conda env create -f environment.yml
```

## Development Tools

### Running Tests

Using pytest:
```bash
pytest
pytest tests/test_file.py -v  # verbose
pytest -k "test_name"  # run specific test
```

### Code Formatting

Using Black:
```bash
pip install black
black .
```

Using isort (import sorting):
```bash
pip install isort
isort .
```

### Linting

Using flake8:
```bash
pip install flake8
flake8 .
```

### Type Checking

Using mypy:
```bash
pip install mypy
mypy your_file.py
```

## Best Practices

1. Always use virtual environments for project isolation
2. Keep dependencies updated and documented
3. Use version control for your requirements files
4. Choose either pip or poetry for a project, don't mix them
5. Include development dependencies separately
6. Use appropriate Python version for your project

## Troubleshooting

Common issues and solutions:

- **Package conflicts**: Use `pip check` to verify dependencies
- **Virtual environment not activating**: Ensure correct activation command for your shell
- **Poetry lock file conflicts**: Delete poetry.lock and reinstall
- **Package installation fails**: 
  - Check Python version compatibility
  - Verify internet connection
  - Use `pip install --verbose` for detailed output