import random
import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_number():
    while True:
        num = random.randint(1000, 10000)  # Larger range for better security
        if is_prime(num):
            return num

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keys():
    # Generate two distinct prime numbers
    p = generate_prime_number()
    q = generate_prime_number()
    while q == p:
        q = generate_prime_number()

    # Calculate n (modulus) and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose e
    e = random.randint(1, phi_n)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)

    # Calculate d
    gcd, x, y = extended_euclidean(e, phi_n)
    d = x % phi_n

    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)

if __name__ == "__main__":
    # Generate keys
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Input message
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)

