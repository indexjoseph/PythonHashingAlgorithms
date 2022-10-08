# PythonHashingAlgorithms
# C-Hashing

  For the C program that takes two command line arguments, after you have completed compiling and know
      the name of your executable, you should run the executable like the following:
        
        ./<executable name> <hashing algo> <String to hash>
  
  For the C program that does not take a string as an argument:
  
        ./<executable name> <hashing algo>
  
  NOTE:
  
    Both of these are running on the virtual box on my machine. Not in a labtainer. To get them to run
    as they are now, I had to upgrade my appstream before updating and installing openssl and libssl. 
    The command to do this is seen in section (1) just below.
  
    In both scenarios, the hashing algorithm is not marked as a flag, you simply use one of the following:
        
        md5
        sha1
        sha256
        <any other supported within the library>
  
  (1) If you run into issues running compiling it, you may have to upgrade your appstream _then_ update your openssl stuff.
  To upgrade the appstream
        
        sudo apt-get upgrade appstream

# Python - HashString.py

For the HashString.py program it allows for the user to input a text file on
the command line and given the text file, it will preform a chosen hashing algorithm.
The optional Hashing Algorithms are MD5, SHA1, and SHA256. Once the user input a text
file and chooses an algorithm, the program will produce a digest and prin it out to the
user.

# Usage
 
python HashString.py <text> <hashing algorithm>
  
# Python - HashBreaker.py

For the HashString.py program will attempt to break the collision free and one way properties. Afterwards
it will print out the amount of attempts it took to break the one way property.
user.

# Usage
 
python HashBreaker.py
