from setuptools import setup, find_packages

setup(
    name="dice-tests",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "pytest",
        "pytest-playwright",
        "python-dotenv",
        "ruff"
    ],
) 