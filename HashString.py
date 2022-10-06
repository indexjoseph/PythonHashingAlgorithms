import sys
from Crypto.Hash import MD5, SHA1, SHA256

def md5_hash(text):
    md5_hash_output = MD5.new(text)
    return md5_hash_output.digest()

def sha1_hash(text):
    sha1_hash_output = SHA1.new(text)
    return sha1_hash_output.digest()

def sha256_hash(text):
    sha256_hash_output = SHA256.new(text)
    return sha256_hash_output.digest()

def readFile(filename):
    try:
        file = open(filename, "r")
    except IOError:
        print("Unable to read/find: ", filename)
        exit(1)
    return file.read()

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
