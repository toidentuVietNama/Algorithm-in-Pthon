import secrets
import string
def otp(message):
    # Khởi tạo từ điển từ a >z 25 ký tự
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    # đảo ngược chữ cái từ 0:a thành a:0
    inv_dict = {letter:index for index, letter in plain_dict.items()}
    message = message.lower()
    message = ''.join(letter for letter in message if letter.isalnum())
    # Khởi tạo chuỗi
    key = []

    while len(key) < len(message):
        # Khóa sẽ chọn ra ký tự trog 25 ký tự đã khởi tạo ban đầu
        key.append(secrets.choice(range(0,len(plain_dict))))
    #  Hàm thuật toán và đóng gói thuật toán
    encrypt_list = [(inv_dict[let]+ind)%len(plain_dict) for let, ind in zip(message,key)]
    # TRả lại danh sách mã hóa
    return [''.join([plain_dict[ind] for ind in encrypt_list]), key]


def otp_decryption(cipher_text, key):
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    inv_dict = {letter: index for index, letter in plain_dict.items()}
    cipher_list = [inv_dict[let] for let in cipher_text]

    return ''.join([plain_dict[(c_index - key_index) % 26] for c_index, key_index in zip(cipher_list, key)])
otp_encryption = otp("Nguyen Sy KHoi")

otp_cipher = otp_encryption[0]
otp_key = otp_encryption[1]
print(f'Văn bản sau khi được mã hóa  : {otp_cipher}')
print(f"Văn bản sau khi được giải mã :{otp_decryption(otp_cipher, otp_key)}")
