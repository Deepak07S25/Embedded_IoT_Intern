def encrypt_binary_text(binary_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(0, len(binary_text), key_length):
        encrypted_chunk = ""
        for j in range(key_length):
            if i + j < len(binary_text):
                encrypted_chunk += str(int(binary_text[i + j]) ^ int(key[j]))
        encrypted_text += encrypted_chunk
    
    return encrypted_text

def stl_to_binary_01_txt(input_stl_path, output_txt_path):
    with open(input_stl_path, 'rb') as stl_file:
        stl_data = stl_file.read()
    
    binary_data = ' '.join(format(byte, '08b') for byte in stl_data)
    
    with open(output_txt_path, 'w') as txt_file:
        txt_file.write(binary_data)

input_stl_path = 'd.stl'  # Replace with the path to your STL file
output_txt_path = 'bin_stl.txt'  # Replace with the desired output TXT file path

stl_to_binary_01_txt(input_stl_path, output_txt_path)

# Load the binary text from the file
with open(output_txt_path, 'r') as txt_file:
    binary_text = txt_file.read().replace(" ", "")

encryption_key = "11111111"  # Replace with your desired encryption key

encrypted_text = encrypt_binary_text(binary_text, encryption_key)

encrypted_output_path = 'encrypted_bin_stl.txt'
with open(encrypted_output_path, 'w') as encrypted_file:
    encrypted_file.write(encrypted_text)
