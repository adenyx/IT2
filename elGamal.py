from math import pow
import random

a = random.randint(2, 10)


def genKeyNumber(a, b):
    if a < b:
        return genKeyNumber(b, a)
    elif a % b == 0:
        return b
    else:
        return genKeyNumber(b, a % b)


def genKey(q):
    key = random.randint(pow(10, 20), q)
    while genKeyNumber(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c


def encrypt(message, q, h, g):
    encrypted_message = []
    k = genKey(q)

    # p - g^k
    # s - g^ak
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(message)):
        encrypted_message.append(message[i])

    for i in range(0, len(encrypted_message)):
        encrypted_message[i] = s * ord(encrypted_message[i])
    return encrypted_message, p


def decrypt(encrypted_message, p, key, q):
    decrypted_message = []
    h = power(p, key, q)

    for i in range(0, len(encrypted_message)):
        decrypted_message.append(chr(int(encrypted_message[i] / h)))
    return decrypted_message


def main():
    message = input('Start message: ')
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)  # g - random simple number
    key = genKey(q)
    h = power(g, key, q)  # h - g^a
    encrypted_message, p = encrypt(message, q, h, g)
    print("Encrypted Message:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, p, key, q)
    final_message = ''.join(decrypted_message)
    print("Decrypted Message :", final_message)


main()
