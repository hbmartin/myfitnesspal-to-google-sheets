# myfitnesspal-to-google-sheets

[![PyPI](https://img.shields.io/pypi/v/mfp2sheets.svg)](https://pypi.org/project/mfp2sheets/)
[![GitHub issues](https://img.shields.io/github/issues-raw/hbmartin/myfitnesspal-to-google-sheets.svg)](https://github.com/hbmartin/myfitnesspal-to-google-sheets/issues)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://travis-ci.com/hbmartin/myfitnesspal-to-google-sheets.svg?branch=master)](https://travis-ci.com/hbmartin/myfitnesspal-to-google-sheets)

Copy daily MyFitnessPal data to Google Sheets

## Installation and Usage

```
pip3 install mfp2sheets --upgrade
mfp2sheets <MFP username>
```

You need to [authorise pygsheets](https://pygsheets.readthedocs.io/en/stable/authorization.html) and [authenticate python-myfitnesspal](https://github.com/coddingtonbear/python-myfitnesspal#authentication).

## Built With

* [mypy](http://mypy-lang.org/)
* [pygsheets](https://pygsheets.readthedocs.io/en/stable/index.html)
* [python-myfitnesspal](https://github.com/coddingtonbear/python-myfitnesspal)


## Contributing

Pull requests are very welcome! For major changes, please open an issue first to discuss what you would like to change.

### Code Formatting

This project is linted with [pyflakes](https://github.com/PyCQA/pyflakes) and makes strict use of [Black](https://github.com/ambv/black) for code formatting.

### Code of Conduct

Everyone participating in this community is expected to treat other people with respect and more generally to follow the guidelines articulated in the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Authors

* [Harold Martin](https://www.linkedin.com/in/harold-martin-98526971/) - harold.martin at gmail
* [Matthew Edwards](https://github.com/mje-nz)

## License

[MIT](LICENSE.txt)