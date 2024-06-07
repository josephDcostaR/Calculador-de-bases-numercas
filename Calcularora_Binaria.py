class Calculadora_Binaria:
    
    # Conversão Binário para Decimal
    def bin_to_dec(self, bin_str):
        decimal = 0
        for digit in bin_str:
            decimal = decimal * 2 + int(digit)
        return decimal 
    
    # Conversão Decimal para Binário
    def dec_to_bin(self, dec_int):
        binary = ""
        while dec_int > 0:
            binary = str(dec_int % 2) + binary
            dec_int = dec_int // 2
        return binary if binary else "0"

    # Conversão Hexadecimal para Binário
    def hex_to_bin(self, hex_str):
        hex_to_dec = int(hex_str, 16)
        return self.dec_to_bin(hex_to_dec)
    
    # Conversão Binário para Hexadecimal
    def bin_to_hex(self, bin_str):
        dec = self.bin_to_dec(bin_str)
        return hex(dec)[2:].upper()

    # Conversão Octal para Decimal
    def oct_to_dec(self, oct_str):
        decimal = 0
        for digit in oct_str:
            decimal = decimal * 8 + int(digit)
        return decimal

    # Conversão Decimal para Octal
    def dec_to_oct(self, dec_int):
        octal = ""
        while dec_int > 0:
            octal = str(dec_int % 8) + octal
            dec_int = dec_int // 8
        return octal if octal else "0"
