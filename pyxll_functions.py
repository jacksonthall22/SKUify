from pyxll import xl_func
from skuify import skuify as skuify_raw


@xl_func
def skuify(title: str) -> str:
    return skuify_raw(title)
