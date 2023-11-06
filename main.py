import pyperclip as pc
from skuify import skuify

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
            try:
                pc.copy(sku)
                print('SKU copied!')
            except pc.PyperclipException:
                print('SKU could not be copied (PyperclipException)')
        else:
            if not input('Press Enter again to quit: '):
                break

def welcome():
    """Print a welcome message at start of program."""

    print('Welcome to Amazon FBA Seller SKU builder!')
    print('v2.0 Created by Jackson Hall')
    print()
    print()
    
if __name__ == '__main__':
    main()
