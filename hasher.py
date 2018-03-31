#simple hashing program that tests flags/parameters
import hashlib
import argparse

userinput = input("Please enter a string to hash: ")
parser = argparse.ArgumentParser(description = "Hashes a string")
group = parser.add_mutually_exclusive_group()
group.add_argument("--sha256", help = "Outputs a sha256 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha224", help = "Outputs a sha224 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha384", help = "Outputs a sha384 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha512", help = "Outputs a sha512 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha3_256", help = "Outputs a sha3_256 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha3_224", help = "Outputs a sha3_224 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha3_384", help = "Outputs a sha3_384 hexdigest of an inputted string", action="store_true")
group.add_argument("--sha3_512", help = "Outputs a sha3_512 hexdigest of an inputted string", action="store_true")
group.add_argument("--md5", help = "Outputs a md5 hexdigest of an inputted string", action="store_true")
group.add_argument("--all", help = "Outputs all hashes", action="store_true")
args = parser.parse_args()

if args.sha256:
    print(hashlib.sha256(userinput.encode('utf-8')).hexdigest())
elif args.sha224:
    print(hashlib.sha224(userinput.encode('utf-8')).hexdigest())
elif args.sha384:
    print(hashlib.sha384(userinput.encode('utf-8')).hexdigest())
elif args.md5:
    print(hashlib.md5(userinput.encode('utf-8')).hexdigest())
elif args.sha512:
    print(hashlib.sha512(userinput.encode('utf-8')).hexdigest())
elif args.sha3_256:
    print(hashlib.sha3_256(userinput.encode('utf-8')).hexdigest())
elif args.sha3_224:
    print(hashlib.sha3_224(userinput.encode('utf-8')).hexdigest())
elif args.sha3_384:
    print(hashlib.sha3_384(userinput.encode('utf-8')).hexdigest())
elif args.sha3_512:
    print(hashlib.sha3_512(userinput.encode('utf-8')).hexdigest())
elif args.all:
    print("MD5: " + hashlib.md5(userinput.encode('utf-8')).hexdigest())
    print("Sha256: " + hashlib.sha256(userinput.encode('utf-8')).hexdigest())
    print("Sha224: " + hashlib.sha224(userinput.encode('utf-8')).hexdigest())
    print("Sha384: " + hashlib.sha384(userinput.encode('utf-8')).hexdigest())
    print("Sha512: " + hashlib.sha512(userinput.encode('utf-8')).hexdigest())
    print("Sha3_256: " + hashlib.sha3_256(userinput.encode('utf-8')).hexdigest())
    print("Sha3_224: " + hashlib.sha3_224(userinput.encode('utf-8')).hexdigest())
    print("Sha3_384: " + hashlib.sha3_384(userinput.encode('utf-8')).hexdigest())
    print("Sha3_512: " + hashlib.sha3_512(userinput.encode('utf-8')).hexdigest())
else:
    print("Error: type must be specified in the initial program execution. Try python hasher.py --help")
