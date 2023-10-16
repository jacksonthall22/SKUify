MAX_SKU_LENGTH = 40


def skuify(title: str) -> str:
    """ Create a seller SKU from the alphanumeric chars in the Amazon product title. """

    # Replace '-' with spaces and remove duplicate whitespaces
    title = title.replace('-', ' ')
    title = ' '.join(title.split())

    # Make title lowercase and alphanumeric
    title = ''.join([c for c in title if c.isalnum() or c == ' ']).lower()

    # Amazon SKUs are limited to 40 characters.
    # Just join words on '-' and return the first 40 chars.
    return '-'.join(title.split())[:MAX_SKU_LENGTH]
