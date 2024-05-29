print("Calculadora de conversão na base decimal \n")

def bin_to_dec(bin_str):
    decimal = 0
    for digit in bin_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def dec_to_bin(dec_int):
    binary = ""
    while dec_int > 0:
        binary = str(dec_int % 2) + binary
        dec_int = dec_int // 2
    return binary if binary else "0"

def hex_to_bin(hex_str):
    hex_to_dec = int(hex_str, 16)
    return dec_to_bin(hex_to_dec)

def bin_to_hex(bin_str):
    dec = bin_to_dec(bin_str)
    return hex(dec)[2:].upper()

def oct_to_dec(oct_str):
    decimal = 0
    for digit in oct_str:
        decimal = decimal * 8 + int(digit)
    return decimal

def dec_to_oct(dec_int):
    octal = ""
    while dec_int > 0:
        octal = str(dec_int % 8) + octal
        dec_int = dec_int // 8
    return octal if octal else "0"

def main():
    
    while True:
        print("Escolha o tipo de conversão:")
        print("1: Binário para Decimal")
        print("2: Decimal para Binário")
        print("3: Hexadecimal para Binário")
        print("4: Binário para Hexadecimal")
        print("5: Octal para Decimal")
        print("6: Decimal para Octal")
        print("0: Sair")
        
        choice = input("Digite o número da conversão desejada:  ")
        
        if choice == "0":
            print("Saindo...")
            break
        
        if choice == "1":
            bin_str = input("Digite o número binário: ")
            print("Resultado:", bin_to_dec(bin_str))
            
        elif choice == "2":
            dec_int = int(input("Digite o número decimal: "))
            print("Resultado:", dec_to_bin(dec_int))
        
        elif choice == "3":
            hex_str = input("Digite o número hexadecimal: ")
            print("Resultado:", hex_to_bin(hex_str))
        
        elif choice == "4":
            bin_str = input("Digite o número binário: ")
            print("Resultado:", bin_to_hex(bin_str))
        
        elif choice == "5":
            oct_str = input("Digite o número octal: ")
            print("Resultado:", oct_to_dec(oct_str))
        
        elif choice == "6":
            dec_int = int(input("Digite o número decimal: "))
            print("Resultado:", dec_to_oct(dec_int))
        
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
