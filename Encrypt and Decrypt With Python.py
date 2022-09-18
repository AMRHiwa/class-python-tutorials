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
    
    # print(key)
    # print(str(key, 'utf-8'))
    return key

# now we need a function to Encrypt the message or text
def encryption(themessage, key):
    # we need a value to store the generated key that we do it in this way
    #       the_value_name = Fernet(value of key in byte type) 
    #   like :
    #       key1 = Fernet(b'_9uPhouCcO5bBm6o68ULD-mt6AV1qjKnmxUNH8Vl2sk=')
    storekey = Fernet(key)
    
    # now we need to encrypt the text or message that we can give it straight or
    # import that from another text's file and also we need a value to save encrypt message
    # we do it by this method from Fernet
    #       value's_name = the_value_of_store_key.encrypt(message in byte type) 
    #   like :
    #       encryptmessage = storekey.encript(b'This is tutorial encrypting by python')
    #       or we can give it text from outside the function by argument
    encryptmessage = storekey.encrypt(themessage)
    print(f"the encrypt message is : ",str(encryptmessage, 'utf-8'))
    return encryptmessage

def decryption(encryptmessage, key):
    storekey = Fernet(key)
    decryptionmessage = storekey.decrypt(encryptmessage)
    print(str(decryptionmessage, "utf-8"))

key = generatekey()
the_encrypt_message = encryption(b'hello', key)
print(f'the encrypt message in body program : ', str(the_encrypt_message, "utf-8"))
decryption(the_encrypt_message, key)