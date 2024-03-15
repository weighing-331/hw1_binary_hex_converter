# hw1_binary_hex_converter
DSA_w2
## Code
```
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = "" 
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def decimal_to_hex(n):
    if n == 0:
        return "0"
    hexa = "" 
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while n > 0:
        remain = n % 16
        if remain >= 10:
            hexa = hex_map[remain] + hexa
        else:
            hexa = str(remain) + hexa
        n = n // 16
    return hexa

while True:
    decimal = input("Decimal number: ")
    
    try:
        decimal = int(decimal)
        binary_output = decimal_to_binary(decimal)
        print("Binary:", binary_output)
        hex_output = decimal_to_hex(decimal)
        print("Hexadecimal:", hex_output)
    except ValueError:
        pass
```
## 執行結果
<img width="464" alt="image" src="https://github.com/weighing-331/hw1_binary_hex_converter/assets/68834074/b8a66139-f963-470e-8183-1e5dff0b025e">
## Code2
```
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
```
## 執行結果2
<img width="496" alt="image" src="https://github.com/weighing-331/hw1_binary_hex_converter/assets/68834074/74b2d579-088a-4939-bbff-ce15387817d8">
