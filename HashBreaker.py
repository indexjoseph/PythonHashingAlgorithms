from Crypto.Hash import SHA1
from Crypto.Random import get_random_bytes
def collisionBreak():
    attempts = 0

    first_hash = SHA1.new(get_random_bytes(6))
    second_hash = SHA1.new(get_random_bytes(6))

    first_digest = first_hash.digest()
    second_digest = second_hash.digest()
    while(first_digest[0:5] != second_digest[0:5]):
        first_random_bytes = get_random_bytes(6)
        second_random_bytes = get_random_bytes(6)
        if str(first_random_bytes) != str(second_random_bytes):
            first_digest = SHA1.new(first_random_bytes).digest()
            second_digest = SHA1.new(second_random_bytes).digest()
        attempts = attempts + 1
        print("Attempts: " + str(attempts))
    
    print("Attempts taken to match (6 Bytes) on Collision Free Property: " + str(attempts))

def oneWayBreak():
    # Not Finished
    pass

def main():
    oneWayBreak()
    collisionBreak()


if __name__ == "__main__":
    main()