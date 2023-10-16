import pyperclip as pc

MAX_SKU_LENGTH = 40

def main():
    welcome()

    # Loop while user continues entering titles
    while True:
        # Get title
        title = input('Enter listing title (press enter to quit): ')

        if title:
            # Skuify the title
            sku = skuify(title)
            print(f'Your Seller SKU: {sku}\n')

            pc.copy(sku)
            print('SKU copied!')
        else:
            if not input('Press Enter again to quit: '):
                break

def welcome():
    """Print a welcome message at start of program."""

    print('Welcome to Amazon FBA Seller SKU builder!')
    print('v2.0 Created by Jackson Hall')
    print()
    print()

def skuify(title):
    """ Create a seller SKU from the alphanumeric chars in the Amazon product title. """

    # Make title lowercase and alphanumeric
    title = ''.join([c for c in title if c.isalnum() or c == ' ']).lower()

    # Amazon SKUs are limited to 40 characters.
    # Just join `words` on '-' and return the first 40 chars
    words = title.split()
    return '-'.join(words)[:MAX_SKU_LENGTH].rstrip('-')

if __name__ == '__main__':
    main()