from setuptools import setup, find_packages

setup(
    name="csvjsonconverter",
    version="0.1.0",
    description="A simple package to convert CSV files to JSON",
    author="Daniel Agyekum Amakye",
    author_email="janetobosuayaa@gmail.com",
    packages=find_packages(),
    install_requires=["pandas"]
)
