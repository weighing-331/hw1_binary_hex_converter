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
