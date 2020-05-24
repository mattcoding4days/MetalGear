# MetalGear
This is a test repository to make a python package that can be imported
with pip via this this github repo, as well as be tested without needed MetalGear
to install itself as a package ( a recursive dependency )


``` bash
# make sure pre reqs are installed
pip install wheel setuptools --user

# install with this command
pip install git+https://github.com/mattcoding4days/MetalGear#egg=MetalGear --user

# run the unittests from root directory ( where .git, tests/ directorys are )
python -m tests.test_foxhound
```
