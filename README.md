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
You can use `skuify()` directly in Excel:

1. Press `alt + f11` in Excel to open the VBA Editor
1. `Insert` > `Module`
1. Copy and paste the contents in `excel_vba_script.vba` into the code editor
1. Save
1. Now you can use `SKUify` like a regular Excel function:

|   | A                                        | B           |
|---|------------------------------------------|-------------|
| 1 | Title                                    | SKU         |
| 2 | Cra-Z-Art Classic Fineline Markers, 10pk | =SKUify(A2) |

## Todo
- [ ] Store map from SKU to ASIN & other product data; search existing SKUs and append `...-1`, `...-2`, etc. if SKU already exists for different title
- [ ] Get approved for Amazon Business APIs
- [ ] Excel function to get product title from ASIN / ISBN via Amazon Product Search API

<sub>Copyright © 2019 Jackson Hall. All rights reserved.</sub>

[pyperclip]: https://pypi.org/project/pyperclip/
[pyxll]: https://www.pyxll.com/
