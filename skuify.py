MAX_SKU_LENGTH = 40

def main():
    welcome()

    print(skuify('This is a test 1 2 3 !@#$%^&*()_+'))
    print(skuify('This is a test 1 2 3 !@#$%^&*()_+ extra words for added longness extra words for added longness'))

def welcome():
        print('Welcome to Amazon FBA Seller SKU builder!')
        print('v1.0')
        print('Created by Jackson Hall')
        print()
        print()

def skuify(title):
    # Make title lowercase alphanumeric (strips special characters)
    title = ''.join([c for c in title if c.isalnum() or c == ' ']).lower()

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