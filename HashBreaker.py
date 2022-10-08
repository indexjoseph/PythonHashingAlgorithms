"""
Author: Joseph Oladeji and Clay Farrell
This Python Program will attempt to break the collision free and one way properties. Afterwards
it will print out the amount of attempts it took to break the one way property.
user.
"""
from Crypto.Hash import SHA1 # Import the SHA1 Hash Algorithm
from Crypto.Random import get_random_bytes # Import the random byte generator

def collisionBreak():
    """
    This method will attempt to break the collision free property, it will generate 
    an initial set of random bytes then generate another set of random bytes. Both bytes
    will be entered into a hash object then, the hashed object will be checked against one
    another. If the digest of the two hash objects are the same, then the method succeeded,
    otherwise it will geenerate another set of byte and pass it to a hash object, where the
    digest will be checked again. That process will repeat until the two digest are the same
    and the random bytes ( messagee ) are different. It will then return the number of attempts.
    """
    attempts = 0 # Set the initial attempts
    initial_bytes = get_random_bytes(2)
    first_hash = SHA1.new(initial_bytes) 
    second_hash = SHA1.new(get_random_bytes(2)) 

    first_digest = first_hash.hexdigest()
    second_digest = second_hash.hexdigest()
   
    while(first_digest[0:6] != second_digest[0:6]):
        second_random_bytes = get_random_bytes(2)
        if str(initial_bytes) != str(second_random_bytes):
            second_digest = SHA1.new(second_random_bytes).hexdigest()
        attempts+=1
    return attempts

def oneWayBreak():
    """
    This method will attempt to break the one way property, it will generate 
    an initial set of random bytes then generate another set of random bytes. Both bytes
    will be entered into a hash object then, the hashed object will be checked against one
    another. If the digest of the two hash objects are the same, then the method succeeded,
    otherwise it will geenerate another set of byte and pass it to a hash object, where the
    digest will be checked again. That process will repeat until the two digest are the same.
    """
    attempts = 0
    const_hash = SHA1.new(get_random_bytes(3))
    hex_check = const_hash.hexdigest()
    hex_24_bits = hex_check[0:6]
    changing_hash = None
    while changing_hash != hex_24_bits:
        changing_hash = SHA1.new(get_random_bytes(3))
        hex_check = changing_hash.hexdigest()
        changing_hash = hex_check[0:6]
        attempts += 1
    return attempts



def main():
    """
    This method will run both the oneWayBreak and collisionBreak method. It will then print the number of attempts
    each method took.
    """
    print("It took " + oneWayBreak() + " attempts to break the one way property")
    print("It took " + collisionBreak() + " attempts to break the collission free property")


if __name__ == "__main__":
    main()
