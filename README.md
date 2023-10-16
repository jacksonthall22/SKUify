# SKUify

## Overview
This simple script turns an Amazon product title into a seller SKU. Amazon SKUs must be alphanumeric, lowercase, and 40 characters or less.

```
$ title = 'Cra-Z-Art Classic Fineline Markers, 10pk'
$ skuify(title)
'cra-z-art-classic-fineline-markers-10pk'
```

## Install
```
git clone https://github.com/jacksonthall22/SKUify.git && cd SKUify
pip install -r requirements.txt
```

## Command line usage
Running `main.py` executes a continuous loop where you can paste product titles. The skuified result is printed to the screen and copied to the clipboard using [`Pyperclip`][pyperclip].

## Excel usage
You can use `skuify()` directly in Excel using [`pyxll`][pyxll]. Read their install instructions, but basically:

```
pip install pyxll
pyxll install
```

then update pyxll.cfg to include the full path to `pyxll-functions.py` (or move the file to a better location, like the default `pyxll`` install location).

Use it just like a regular Excel function:

|   | A                                        | B           |
|---|------------------------------------------|-------------|
| 1 | Title                                    | SKU         |
| 2 | Cra-Z-Art Classic Fineline Markers, 10pk | =skuify(A2) |

## Todo
- [ ] Store map from SKU to ASIN & other product data; search existing SKUs and append `...-1`, `...-2`, etc. if SKU already exists for different title
- [ ] Get approved for Amazon Business APIs
- [ ] Excel function to get product title from ASIN / ISBN via Amazon Product Search API

<sub>Copyright © 2019 Jackson Hall. All rights reserved.</sub>

[pyperclip]: https://pypi.org/project/pyperclip/
[pyxll]: https://www.pyxll.com/