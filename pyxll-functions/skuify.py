from pyxll import xl_func
from ..skuify import skuify as skuify_raw


# Wrap the existing skuify function in the xl_func decorator so it can be used as a worksheet function
@xl_func
def skuify(title: str) -> str:
    return skuify_raw(title)
