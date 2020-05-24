# MetalGear
This is a test repository to make a python package that can be imported
with pip via this this github repo, as well as be tested without needed MetalGear
to install itself as a package ( a recursive dependency )

### Using python3.8, python=python3

``` bash
# make sure pre reqs are installed
pip install wheel setuptools --user

# if you want to have access to the tests, clone the repo 
# run the unittests from root directory ( where .git, tests/ directorys are )
python -m unittest discover test

# else, if you just want to pip install the package ( like pypi )
# install with this command
pip install git+https://github.com/mattcoding4days/MetalGear#egg=MetalGear --user

# now it will be in your $HOME/.local/lib/python3.X/site-packages/MetalGear
# now you can include it in any other module you want
From MetalGear import foxhound
```
