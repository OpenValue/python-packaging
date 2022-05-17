from setuptools import setup, find_namespace_packages

with open("requirements.txt") as file_requirements:
    requirements = [line.strip() for line in file_requirements.readlines()]

with open("README.md") as file_readme:
    long_description = [line.strip() for line in file_readme.readlines()]

setup(
    name='python_package', # Name pip will use when install it
    version='0.0.1', # Package version, exposed in the built package name 
    author="Databricks Community",
    description="Package description example",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(include=['src.*']),
    python_requires='>=3.0',
    install_requires=requirements,
)
