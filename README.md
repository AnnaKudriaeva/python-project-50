### Hexlet tests and linter status:
[![Actions Status](https://github.com/AnnaKudriaeva/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AnnaKudriaeva/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bb4e44946b8eadb3df3a/maintainability)](https://codeclimate.com/github/AnnaKudriaeva/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/bb4e44946b8eadb3df3a/test_coverage)](https://codeclimate.com/github/AnnaKudriaeva/python-project-50/test_coverage)

An application for finding the difference in 2 files of json, yaml, yaml formats and displaying the result in several variants

## Installation
1. Requires Python 3.12 or higher and Poetry
2. Clone the project: `>> git clone https://github.com/AnnaKudriaeva/python-project-50.git`
3. Build the project using the command: `>> make build`
4. Install the project: `>> make package-install`

### Usage and Options:
To use it just type `gendiff <path_to_file_1> <path_to_file_2>`

* -h, --help - show help message.
* -f, --format - ability to specify format selection.

## Examples of uses
### Diff of deep files
[![asciicast](https://asciinema.org/a/Kn6Kv7LCL0MoKFDHgpE3HaHoz.svg)](https://asciinema.org/a/Kn6Kv7LCL0MoKFDHgpE3HaHoz)
### Diff of deep files with plain style
[![asciicast](https://asciinema.org/a/kDmSpjK4QsN9qscC6cVjauyFU.svg)](https://asciinema.org/a/kDmSpjK4QsN9qscC6cVjauyFU)
### Diff of deep files with json style
[![asciicast](https://asciinema.org/a/zIM374yjWOjoRRd7nmG86rJtf.svg)](https://asciinema.org/a/zIM374yjWOjoRRd7nmG86rJtf)