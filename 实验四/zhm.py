with (open('C:/Users/zezr/Desktop/zhm.txt', 'r') as source_file,
      open('C:/Users/zezr/Desktop/encrypted.txt', 'w') as target_file):
    for line in source_file:
        encryption = ''
        for char in line:
            if 'A' <= char <= 'Z':
                encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                encrypted_char = char
            encryption += encrypted_char
        target_file.write(encryption)
    print("修改成功")