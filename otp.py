import binascii


def additive_cipher(text, key, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        key = -key

    for char in text:
        if char.isupper():
            shifted = (ord(char) - 65 + key) % 26
            result += chr(shifted + 65)
        elif char.islower():
            shifted = (ord(char) - 97 + key) % 26
            result += chr(shifted + 97)
        else:
            result += char

    return result

def multi_cipher(text, key, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        try:
            key = pow(key, -1, 26)
        except ValueError:
            raise ValueError("The key was not coprime of 26")

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            pos = ord(char) - start
            new_pos = (pos * key) % 26
            result += chr(new_pos + start)
        else:
            result += char

    return result

def substituion():
    add_key = 20
    multi_key = 15
    print(" Substitution Menu ".center(120,'-'))
    phrase = input("Please enter a phrase you would like to Encrypt: ").strip()
    while True:
        encrypt = input("Please enter '1' for Additive Cipher or '2' for Multiplicitive Cipher: ")
        match encrypt:
            case '1':
                add_enc = additive_cipher(phrase, add_key, mode='encrypt')
                add_dec = additive_cipher(add_enc, add_key, mode='decrypt')
                print(f"Original: {phrase}")
                print(f"Encrypted: {add_enc}")
                print(f"Decrypted: {add_dec}")
                break

            case '2':
                multi_enc = multi_cipher(phrase, multi_key, mode='encrypt')
                multi_dec = multi_cipher(multi_enc, multi_key, mode='decrypt')
                print(f"Original: {phrase}")
                print(f"Encrypted: {multi_enc}")
                print(f"Decrypted: {multi_dec}")
                break
            case _:
                print("Invalid Entry. Please entry please try again.")
            


def otp_recover_and_encryption():
    mickey_cipher_text = "100001000000011101010100000111000001110101111001"

    mickey_bytes = "mickey".encode('ascii')
    mickey_bin_int = int.from_bytes(mickey_bytes, byteorder='big')
    total_bits = len(mickey_cipher_text)

    mickey_bin_str = format(mickey_bin_int, f"0{total_bits}b")
    ciphertext_int = int(mickey_cipher_text, 2)
    secret_key_int = mickey_bin_int ^ ciphertext_int

    secret_key_bin = format(secret_key_int, f'0{total_bits}b')
    donald_bytes = "donald".encode('ascii')
    donald_bin_int = int.from_bytes(donald_bytes, byteorder='big')
    donald_bit_len = len(donald_bytes)* 8
    donald_bin_str = format(donald_bin_int, f'0{donald_bit_len}b')

    recovered_key_bit_len = total_bits

    if donald_bit_len > recovered_key_bit_len:
        raise ValueError(f"The second name, {donald_bytes}, requires {donald_bit_len}, "
                         f"but the discovered key only provides up to {recovered_key_bit_len} bits.")

    shift_amount = max(0, recovered_key_bit_len - donald_bit_len)
    used_key_int = secret_key_int >> shift_amount

    new_ciphertext_int = donald_bin_int ^ used_key_int
    new_ciphertext_bin = format(new_ciphertext_int, f'0{donald_bit_len}b')

    fmt_mickey_cipher = " ".join([mickey_cipher_text[i:i+8] for i in range(0, len(mickey_cipher_text), 8)])
    fmt_mickey_bin = " ".join([mickey_bin_str[i:i+8] for i in range(0, len(mickey_cipher_text), 8)])
    fmt_secret_key = " ".join([secret_key_bin[i:i+8] for i in range(0, len(mickey_cipher_text), 8)])
    fmt_donald_bin = " ".join([donald_bin_str[i:i+8] for i in range(0, len(mickey_cipher_text), 8)])
    fmt_donald_cipher = " ".join([new_ciphertext_bin[i:i+8] for i in range(0, len(mickey_cipher_text), 8)])
    print(" One-Time Pad Example ".center(120,'-'))
    print(f"Original Ciphertext (mickey):  {fmt_mickey_cipher}")
    print(f"Unencoded Binary (mickey):     {fmt_mickey_bin}")
    print(f"Recovered Secret Key:          {fmt_secret_key}")
    print(f"Unencoded Binary (donald):     {fmt_donald_bin}")
    print(f"New Encrypted Binary (donald): {fmt_donald_cipher}")

    user_input = input("Press any key to return to the previous menu...")

    return

def main():
    while True:
        print(" Encryption Menu ".center(120,'-'))
        user_select = input("Enter a '1' for Substitution Cipher | Enter a '2' for the OTP Encryption example | 'exit' to Exit:\n").strip()
        match user_select:
            case '1':
                substituion()
            case '2':
                otp_recover_and_encryption()
            case 'exit':
                print("Exiting...")
                exit()
            case _:
                print("Invalid Entry. Please enter 1, 2, or exit.")
#calling of the main function
main()






