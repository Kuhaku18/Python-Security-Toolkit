# Hash Cracker - A cybersecurity tool that brute-forces an MD5 hash using a predefined dictionary wordlist.
import hashlib
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
wordlist = ["admin", "123456", "qwerty", "password", "letmein", "shadow"]
print("Starting Hash Cracker...\n")
for word in wordlist:
    guess_hash = hashlib.md5(word.encode()).hexdigest()
    print(f"Trying: {word} -> {guess_hash}")
    if guess_hash == target_hash:
        print(f"\nPASSWORD CRACKED! The password is: '{word}'")
        break
else:
    print("\nHash not found in wordlist.")