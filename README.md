# Repository for `hungarian-stemmer`

[![tests](https://github.com/montana-knowledge-management/hungarian-stemmer/actions/workflows/ci.yml/badge.svg)](https://github.com/robust/actions)
[![codecov](https://codecov.io/gh/montana-knowledge-management/hungarian-stemmer/branch/main/graph/badge.svg?token=KMYGW7NHWH)](https://codecov.io/gh/montana-knowledge-management/hungarian-stemmer)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/montana-knowledge-management/hungarian-stemmer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/montana-knowledge-management/hungarian-stemmer/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/montana-knowledge-management/hungarian-stemmer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/montana-knowledge-management/hungarian-stemmer/context:python)

## How to use this package?

### Install `hungarian-stemmer`

For the simplest install simply run:

```shell
pip install hungarian-stemmer
```

## Differences compared to `cyhunspell` repository

The `hungarian-stemmer` package is built on top of the well-known `cyhunspell` Python package,
available [here](https://pypi.org/project/cyhunspell/). Therefore, the tool is capable of doing the same as the original
tool, except for modifying (adding and removing) the dictionary, using bulk processes.

The `hungarian-stemmer` fixes several issues present in the currently available `hunspell` for the Hungarian language.
Such an example would be the overly extensive stemming often resulting in stems having a completely different meaning (
see first row in the table), not handling the phrasal verbs well (second row), and experiencing a malfunction in
stemming (third row).
The following table shows some examples of the differences.

|     word     |   hunspell   |    hungarian-stemmer    |
|:------------:|:------------:|:-----------------------:|
|    mással    |  más, ma, mi |           más           |
|  megtörtént  |   történik   | megtörtént, megtörténik |
| köztestületi | köztestületi |       köztestület       |

## Examples of usage

### Importing and instantiating HungarianStemmer object

```python
from hungarian_stemmer.hungarian_stemmer import HungarianStemmer

hunstem = HungarianStemmer()
```

### Stemming

```python
hunstem.stem("megcsinálták")  # ("megcsinál",)
```

### Analyze

```python
hunstem.analyze(
    "megcsinálták")  # ("ip:PREF sp:meg  st:csinál po:vrb ts:PRES_INDIC_INDEF_SG_3 " "is:PAST_INDIC_DEF_PL_3",)
```

### Suggest

```python
hunstem.suggest(
    "megcsinálták")  # ("megcsináltak","megcsinálták","megcsinálték","megcsináltál","megcsinálnák","megcsináltok","megcsináltuk","megcsinálják","meg csinálták","meg-csinálták",)
```

### Spell

```python
hunstem.spell("megcsinálták")  # True
hunstem.spell("megcsinláták")  # False
```

### Suggest suffixes

```python
hunstem.suffix_suggest("megcsinálták")  # ("csinálnia","csinálja","csinálja", ...,)
```
