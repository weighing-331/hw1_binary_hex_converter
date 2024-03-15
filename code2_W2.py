def decimal_to_binary(decimal):
    binary = [0] * 8
    for i in range(7, -1, -1):
        binary[i] = decimal % 2
        decimal //= 2
    return binary

def binary_to_hexadecimal(binary):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ''
    groups = [binary[:4], binary[4:]]    
    for group in groups:
        decimal_value = 0
        for i in range(len(group)):
            decimal_value += int(group[i]) * (2 ** (3 - i))  # 將二進位轉換為十進位
        hexadecimal += hex_chars[decimal_value]
    return hexadecimal

def main():
    decimal_input = int(input("Enter a decimal number (0-255): "))
    if decimal_input < 0 or decimal_input > 255:
        print("Invalid")
        return
    binary = decimal_to_binary(decimal_input)
    hexadecimal = binary_to_hexadecimal(binary)
    print(f'Binary: {binary}, Hexadecimal: {hexadecimal}')

if __name__ == "__main__":
    main()
