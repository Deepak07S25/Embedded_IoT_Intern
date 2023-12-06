def stl_to_binary_01_txt(input_stl_path, output_txt_path):
    with open(input_stl_path, 'rb') as stl_file:
        stl_data = stl_file.read()
    
    binary_data = ' '.join(format(byte, '08b') for byte in stl_data)
    
    with open(output_txt_path, 'w') as txt_file:
        txt_file.write(binary_data)

input_stl_path = 'd.stl'  # Replace with the path to your STL file
output_txt_path = 'bin_stl.txt'  # Replace with the desired output TXT file path

stl_to_binary_01_txt(input_stl_path, output_txt_path)
