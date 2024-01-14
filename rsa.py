import random
from sympy import isprime

def generate_prime_candidate(length):
    # Generate random odd integer
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    p = 4
    # Keep generating until a prime number is found
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    # Extended Euclidean Algorithm to find the modular inverse
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1, temp2 = temp_phi // e, temp_phi % e
        temp_phi, e = e, temp2
        
        x1, x2 = x2 - temp1 * x1, x1
        y1, d = d - temp1 * y1, y1
    
    return d + phi

def generate_keypair(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    # Calculate n (modulus for public and private keys)
    n = p * q

    # Calculate phi (Euler's totient function)
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    # Public key (e, n) and private key (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Unpack the key into its components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = generate_prime_number(1024)
    q = generate_prime_number(1024)
    public, private = generate_keypair(p, q)
    print("Public key: ", public)
    print("Private key: ", private)
    
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print("Encrypted message: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    
    print("Decrypted message: ")
    print(decrypt(private, encrypted_msg))
