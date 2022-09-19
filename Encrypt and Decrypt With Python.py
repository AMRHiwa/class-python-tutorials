# we need to import 'Fernet' mudole from 'cryptography.fernet'
# we must to install cryptography by pip in cmd or terminal
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
    print(f'key is : ', str(key, 'utf-8'))
    
    # we can also return the key into the program's main body
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
    #       encryptmessage = storekey.encrypt(b'This is tutorial encrypting by python')
    #       or we can give it text from outside the function by argument
    encryptmessage = storekey.encrypt(themessage)
    
    # we can show the encrypted message to user 
    print(f"the encrypt message is : ",str(encryptmessage, 'utf-8'))
    
    # in this program another ability we can add it that is return the encrypted message
    # into main body if we want it by the 'return' command
    return encryptmessage

# we need a function to decryption of encrypt message
def decryption(encryptmessage, key):
    
    # we need a value to store the generated key that we do it in this way
    #       the_value_name = Fernet(value of key in byte type) 
    #   like :
    #       key1 = Fernet(b'_9uPhouCcO5bBm6o68ULD-mt6AV1qjKnmxUNH8Vl2sk=')
    storekey = Fernet(key)

    # now we need to decrypt the text or message that we can give it straight or
    # import that from another text's file and also we need a value to save decrypt message
    # we do it by this method from Fernet
    #       value's_name = the_value_of_store_key.decrypt(message in byte type) 
    #   like :
    #       decryptionmessage = storekey.decrypt(b'This is tutorial encrypting by python')
    #       or we can give it text from outside the function by argument
    decryptionmessage = storekey.decrypt(encryptmessage)
    
    # in this function we can also show the decrypted message to our user
    print(f'the decrypt message : ',str(decryptionmessage, "utf-8"))

# for a build a key we have to call the generatekey function that we defined above
key = generatekey()

# for encrypting the message we must call the encryption function that defined above before
# and give it two arguments , a message with byte type and the key that used for encrypting
# for set a message in a byte type we can set it in " b'the message text' " format
the_encrypt_message = encryption(b'hello', key)

# print(f'the encrypt message in body program : ', str(the_encrypt_message, "utf-8"))

# for decrypt the encrypted message we must call the decryption function that defined above before
# and give it two arguments, a encrypted message in byte type and the key that used for encrypt
decryption(the_encrypt_message, key)