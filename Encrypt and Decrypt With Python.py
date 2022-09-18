from cryptography.fernet import Fernet

# we need a function to generate a key
def generatekey():
    # for genarating a key to encrypt and decrypt files we use this method from Fernet module
    #     values_name = Fernet.generate_key()
    key = Fernet.generate_key()
    # the generated key with this function is bit and if we want to show that
    #           we have some thing like this:
    #           b'_9uPhouCcO5bBm6o68ULD-mt6AV1qjKnmxUNH8Vl2sk='
    #           that 'b' in this statement means bit and that string in '...' is our key
    # if we want to show that key in string, we can use this command 
    #       print(str(key, 'utf-8'))
    print(key)
    print(str(key, 'utf-8'))
    
generatekey()