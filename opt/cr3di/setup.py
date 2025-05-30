from setuptools import setup, find_packages

setup(
    name="cr3di",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "rich",
        "python-gnupg",
        "pydantic"
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cr3di = cr3di.cr3di:app"
        ]
    },
    description="Encrypted credential manager for pentesters.",
    author="Your Name",
    author_email="you@example.com"
)
