"""Setup file for Python lib."""
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="sheets_manager",
    version="1.2.1",
    description="Codebase for operating on Google Sheets",
    url="https://github.com/mr-strawberry66/sheets-manager",
    author="Sam Kenney",
    author_email="sam.kenney@me.com",
    license="MIT",
    long_description=long_description,
    platforms=[],
    install_requires=[
        "google-api-python-client==2.24.0",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==0.4.6",
        "oauth2client==4.1.3",
    ],
    packages=["sheets_manager"]
    + ["sheets_manager." + pkg for pkg in find_packages("sheets_manager")],
)
