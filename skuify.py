import pyperclip as pc

MAX_SKU_LENGTH = 40

def main():
    welcome()

    # Loop while user continues entering titles
    cont = True
    while cont:
        # Get title
        title = input('Enter listing title (press enter to quit): ')

        if title != '':
            # Skuify the title
            sku = skuify(title)
            print(f'Your Seller Sku: {sku}\n')

            # Copy SKU
            pc.copy(sku)
            print('SKU copied!')
        else:
            cont = False

def welcome():
    """Print a welcome message at start of program."""

    print('Welcome to Amazon FBA Seller SKU builder!')
    print('v1.0 Created by Jackson Hall')
    print()
    print()

def skuify(title):
    """Create valid seller SKU from listing title."""

    # Make title lowercase alphanumeric (strips special characters)
    title = ''.join([c for c in title if c.isalnum() or c == ' ' or c == '-']).lower()

    # Break into words
    words = title.split()

    # Loop through words to build SKU
    sku = ''
    i = 0
    cont = True
    while i < len(words) and cont:
        # Add next word and dash if SKU will not be longer than 40 chars
        if len(sku) + len(words[i]) <= MAX_SKU_LENGTH:
            sku += words[i] + '-'
        else:
            cont = False

        i += 1

    return sku.rstrip('-')

if __name__ == '__main__':
    main()