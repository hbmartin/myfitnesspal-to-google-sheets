from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "src", "version.py")) as fp:
    exec(fp.read())

setup(
    name="mfp2sheets",
    version=__version__,
    description="Copy daily MyFitnessPal data to Google Sheets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hbmartin/myfitnesspal-to-google-sheets/",
    author="Harold Martin",
    author_email="harold.martin@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    license="MIT",
    keywords="myfitnesspal",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pygsheets", "myfitnesspal"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["mfp2sheets=src.mfp_sheets:main"]
    },
    project_urls={
        "Bug Reports": "https://github.com/hbmartin/myfitnesspal-to-google-sheets/issues"
    },
)
