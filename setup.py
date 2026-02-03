from setuptools import setup, find_packages

setup(
    name="acme-inventory-api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "sqlalchemy>=1.3.0",
    ],
)
