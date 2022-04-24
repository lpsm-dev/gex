# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from gex import __app_name__, __version__

SHORT_DESCRIPTION = """
Gex is a tool for manage G-Earth extensions write using G-Python
""".strip()

DEPENDENCIES = [
    "arrow==1.2.1",
    "asciimatics==1.14.0",
    "coloredlogs==15.0",
    "g-python==0.1.6",
    "python-json-logger==2.0.1",
    "rich==11.0.0",
]

LICENSE = "MIT license"
URL = "https://github.com/lpmatos/gex"
EMAIL = "lpsm-dev@protonmail.com"
AUTHOR = "CI Monk"
REQUIRES_PYTHON = ">=3.6.0"

setup(
    name=__app_name__,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    zip_safe=False,
    description=SHORT_DESCRIPTION,
    long_description=__doc__,
    install_requires=DEPENDENCIES,
    python_requires=REQUIRES_PYTHON,
    entry_points=f"""
        [console_scripts]
        {__app_name__}={__app_name__}.main:main
    """,
    keywords=["cli", "g-earth", "g-python", "python"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Helm",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Repository": URL,
    },
)
