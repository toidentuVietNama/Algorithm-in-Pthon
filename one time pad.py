import secrets
import string
def otp(message):
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    inv_dict = {letter:index for index, letter in plain_dict.items()}
    message = message.lower()
    message = ''.join(letter for letter in message if letter.isalnum())
    key = []
    while len(key) < len(message):
        key.append(secrets.choice(range(0,len(plain_dict))))
        encrypt_list = [(inv_dict[letter]+index )%len(plain_dict) for letter, index in zip(message,key)]
        # VD : [(inv_dict['H'] + 4 ) % 26
    return [''.join([plain_dict[ind] for ind in encrypt_list]), key]


def otp_decryption(cipher_text, key):
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    # 0:a ; 1:b
    inv_dict = {letter: index for index, letter in plain_dict.items()}
    # a:0 ; 1:b
    cipher_list = [inv_dict[let] for let in cipher_text]

    return ''.join([plain_dict[(c_index - key_index) % 26] for c_index, key_index in zip(cipher_list, key)])
otp_encryption = otp("Nguyen Sy Khoi")

otp_cipher = otp_encryption[0]
otp_key = otp_encryption[1]
print(f'Văn bản sau khi được mã hóa  : {otp_cipher}')
print(f"Chìa khóa của văn bản:  {otp_key}")
print(f"Văn bản sau khi được giải mã :{otp_decryption(otp_cipher, otp_key)}
"""
a   b   c  d  e  f  g   h  i  j  k   l    m    n   o    p  q    r    s    t    u     v    w    x    y    z
0   1   2  3  4  5  6   7  8  9  10  11  12   13  14   15  16  17   18   19   20    21   22   23   24   25

Văn bản truyền vào : Nguyen Sy Khoi
Văn bản sau khi được mã hóa  : itkiteembfoc
Chìa khóa của văn bản :  [21, 13, 16, 10, 15, 17, 12, 14, 17, 24, 0, 20] > dạng chữ : vnqkqmoryau
Văn bản sau khi được giải mã :nguyensykhoi

"""