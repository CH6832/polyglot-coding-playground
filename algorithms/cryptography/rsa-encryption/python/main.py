Sure, here's a basic implementation of RSA encryption and decryption in Python:

python

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

# Example usage:
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
print("Public Key:", public_key)
print("Private Key:", private_key)

plaintext = "Hello, world!"
print("Original message:", plaintext)

encrypted_msg = encrypt(public_key, plaintext)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)

This code implements the RSA encryption and decryption process using Python. It includes functions to generate key pairs, encrypt plaintext, and decrypt ciphertext. You can test it with different values for p and q to generate different key pairs.