from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MetalGear",
    version="0.0.1",
    author="Matt Williams",
    author_email="mattltf@pm.me",
    description="Classes that represent foxhound members",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattcoding4days/MetalGear",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
