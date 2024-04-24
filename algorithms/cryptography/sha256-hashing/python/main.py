Implementing a SHA-256 hashing algorithm from scratch is quite complex due to its cryptographic nature. However, I can provide you with a simplified version for educational purposes. Keep in mind that this implementation may not be as secure or efficient as established libraries, so it's not suitable for production use. Here's a basic implementation of SHA-256 in Python:

python

def right_rotate(n, b):
    return ((n >> b) | (n << (32 - b))) & 0xFFFFFFFF

def sha256(message):
    # Initialize hash values
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Initialize array of round constants
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Pre-processing
    original_message = message
    message = bytearray(message, 'utf-8')
    length = len(message) * 8

    # Append the bit '1' to the message
    message.append(0b10000000)

    # Append zeros to make message length in bits congruent to 448 mod 512
    while len(message) % 64 != 56:
        message.append(0)

    # Append length of message
    message += length.to_bytes(8, 'big')

    # Process the message in successive 512-bit chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        words = [int.from_bytes(chunk[j:j + 4], 'big') for j in range(0, 64, 4)]

        # Initialize hash value for this chunk
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Main loop
        for j in range(64):
            if j < 16:
                w = words[j]
            else:
                w = (right_rotate(words[j - 15], 7) ^ right_rotate(words[j - 15], 18) ^ (words[j - 15] >> 3)) + \
                    (right_rotate(words[j - 2], 17) ^ right_rotate(words[j - 2], 19) ^ (words[j - 2] >> 10)) + \
                    words[j - 16] + words[j - 7]

            t1 = h + (right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)) + \
                 ((e & f) ^ (~e & g)) + k[j] + w
            t2 = (right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))

            h, g, f, e, d, c, b, a = g, f, e, (d + t1) & 0xFFFFFFFF, c, b, a, (t1 + t2) & 0xFFFFFFFF

        # Add this chunk's hash to result so far
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Produce the final hash value
    return '%08x%08x%08x%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4, h5, h6, h7)


# Test the implementation
message = "Hello, world!"
hashed_message = sha256(message)
print("SHA-256 Hash:", hashed_message)

This implementation is simplified and may not be suitable for all use cases. It's recommended to use established cryptographic libraries like hashlib in Python for production-level applications.