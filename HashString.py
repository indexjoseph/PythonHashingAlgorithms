"""
Author: Joseph Oladeji and Clay Farrell
This Python Program allows for the user to input a text file on
the command line and given the text file, it will preform a chosen hashing algorithm.
The optional Hashing Algorithms are MD5, SHA1, and SHA256. Once the user input a text
file and chooses an algorithm, the program will produce a digest and prin it out to the
user.
"""


import sys
from Crypto.Hash import MD5, SHA1, SHA256 # Import the Hashing Algorithms

def md5_hash(text):
    """ Creates a hashed digest of the text passed, utilizing the MD5 Algorithm """
    md5_hash_output = MD5.new(text) # Enter the messagee in the MD5 HASH
    return md5_hash_output.digest() # Return the MD5 Hashed Message

def sha1_hash(text):
    """ Creates a hashed digest of the text passed, utilizing the SHA1 Algorithm """
    sha1_hash_output = SHA1.new(text) # Enter the messagee in the SHA1 HASH
    return sha1_hash_output.digest() # Return the SHA1 Hashed Message


def sha256_hash(text):
    """ Creates a hashed digest of the text passed, utilizing the SHA256 Algorithm
    """
    sha256_hash_output = SHA256.new(text) # Enter the messagee in the SHA256 HASH
    return sha256_hash_output.digest() # Return the SHA256 Hashed Message

def readFile(filename):
    """ Attempts to read of file, if the file cannot be found/read it will notify the user 
     Otherwise the file contents will be returned """
    try:
        file = open(filename, "r") # Attempt to open file
    except IOError:
        print("Unable to read/find: ", filename) # Print error message if the file couldn't be read/found
        exit(1) # Exit the program
    return file.read() # Return the file's content

def main():
    digest_result = None
    if(len(sys.argv) == 3):
        text = readFile(sys.argv[2]).encode("utf-8")
        if(sys.argv[1].lower() == "md5"):
            digest_result = md5_hash(text)
        if(sys.argv[1].lower() == "sha1"):
            digest_result = sha1_hash(text)
        if(sys.argv[1].lower() == "sha256"):
            digest_result = sha256_hash(text)
    if digest_result == None:
        print("Usage: python HashString.py <Hashing Algorithm> <Text File>")
        print("Example: python HashString.py md5 plaintext.txt")
        print("Hashing Algorithms: md5, sha1, sha256")
    else:
        print(digest_result)

    print("Closing program...")


if __name__ == "__main__":
    main()
