# My Notes 🤓🤓
### Pytest provides options for stopping test cases after a certain number of failures
we use: python -m pytest --maxfail=1 (or --maxfail=2 for two failures)...

### pytest includes an option that would generate a JUnit XML file for test results 
we use python -m pytest --junit-xml report.xml (report.xml is the name of the file in which the results will be stored)

### Supported pytest configuration file types
 pytest.ini
 tox.ini
 setup.cfg
 pyproject.toml

 pytest.ini
pytest.ini files take precedence over other files, even when empty.

### pytest.ini
```
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
pyproject.toml
New in version 6.0.
```

pyproject.toml are considered for configuration when they contain a tool.pytest.ini_options table.

### pyproject.toml
```
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
```

Note
One might wonder why [tool.pytest.ini_options] instead of [tool.pytest] as is the case with other tools.

The reason is that the pytest team intends to fully utilize the rich TOML data format for configuration in the future, reserving the [tool.pytest] table for that. The ini_options table is being used, for now, as a bridge between the existing .ini configuration system and the future configuration format.

tox.ini
tox.ini files are the configuration files of the tox project, and can also be used to hold pytest configuration if they have a [pytest] section.

### tox.ini
```
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
setup.cfg
setup.cfg files are general purpose configuration files, used originally by distutils, and can also be used to hold pytest configuration if they have a [tool:pytest] section.
```

### setup.cfg
```
[tool:pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration 
```

Warning
Usage of setup.cfg is not recommended unless for very simple use cases. .cfg files use a different parser than pytest.ini and tox.ini which might cause hard to track down problems. When possible, it is recommended to use the latter files, or pyproject.toml, to hold your pytest configuration.

### Writing RestAPI tests using yaml 
we use Tavern API
 - See and read about [Tavern](https://tavern.readthedocs.io/en/latest/)
 - 📫 Get in touch: [LinkedIn](https://www.linkedin.com/in/emmanuel-ndaliro-501771124/)

### Plugins in Pytest
To use the html plugin, we first install pytest-html plugin using pip
then we run "python -m pytest --html=report.html"
### pytest-cov
for the coverage plugin we first install pytest-cov plugin using pip
then we run "python -m pytest --cov=stuff"
### pytest-xdist
for thexdist plugin we first install pytest-xdist plugin using pip
then we run "python -m pytest -n 3" where 3 is the number of parallel threads
