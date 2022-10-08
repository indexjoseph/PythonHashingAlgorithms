# Author Joseph Oladeji and Clay Farrell

from Crypto.Hash import SHA1
from Crypto.Random import get_random_bytes

def collisionBreak():
    attempts = 0
    initial_bytes = get_random_bytes(2)
    first_hash = SHA1.new(initial_bytes)
    second_hash = SHA1.new(get_random_bytes(2))

    first_digest = first_hash.hexdigest()
    second_digest = second_hash.hexdigest()
   
    while(first_digest[0:6] != second_digest[0:6]):
        second_random_bytes = get_random_bytes(2)
        if str(initial_bytes) != str(second_random_bytes):
            second_digest = SHA1.new(second_random_bytes).hexdigest()
            # print("First Digest: " + str(first_digest[0:6]) + " Second Digest " + str(second_digest[0:6]))
        attempts+=1
    return attempts

def oneWayBreak():
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

    sum_av = 0
    for i in range(10):
        num = collisionBreak()
        sum_av += num
        print(num, end=" ")
    print("It took on average " + str(sum_av/10))
    # collisionBreak()


if __name__ == "__main__":
    main()
