

from Calcularora_Binaria import Calculadora_Binaria


class CalculadoraPrincipal:
    
    def __init__(self):
        self.calculadora = Calculadora_Binaria()
       
    def main(self):
        while True:
            print("Escolha o tipo de conversão:")
            print("1: Binário para Decimal")
            print("2: Decimal para Binário")
            print("3: Hexadecimal para Binário")
            print("4: Binário para Hexadecimal")
            print("5: Octal para Decimal")
            print("6: Decimal para Octal")
            print("0: Sair \n")
            
            choice = input("Selecione o número da conversão desejada:  ")
            
            if choice == "0":
                print("Saindo...")
                break
            
            if choice == "1":
                bin_str = input("Digite o número binário: ")
                if all(digit in '01' for digit in bin_str):
                    print("Resultado:", self.calculadora.bin_to_dec(bin_str))
                else:
                    print("Erro: Entrada inválida. Apenas 0 e 1 são permitidos.")
                
            elif choice == "2":
                try:
                    dec_int = int(input("Digite o número decimal: "))
                    print("Resultado:", self.calculadora.dec_to_bin(dec_int))
                except ValueError:
                    print("Erro: Entrada inválida. Digite um número decimal válido.")
            
            elif choice == "3":
                hex_str = input("Digite o número hexadecimal: ").upper()
                if all(digit in '0123456789ABCDEF' for digit in hex_str):
                    print("Resultado:", self.calculadora.hex_to_bin(hex_str))
                else:
                    print("Erro: Entrada inválida. Apenas dígitos hexadecimais (0-9, A-F) são permitidos.")
            
            elif choice == "4":
                bin_str = input("Digite o número binário: ")
                if all(digit in '01' for digit in bin_str):
                    print("Resultado:", self.calculadora.bin_to_hex(bin_str) )
                else:
                    print("Erro: Entrada inválida. Apenas 0 e 1 são permitidos.")
            
            elif choice == "5":
                oct_str = input("Digite o número octal: ")
                if all(digit in '01234567' for digit in oct_str):
                    print("Resultado:", self.calculadora.oct_to_dec(oct_str))
                else:
                    print("Erro: Entrada inválida. Apenas dígitos octais (0-7) são permitidos.")
            
            elif choice == "6":
                try:
                    dec_int = int(input("Digite o número decimal: "))
                    print("Resultado:", self.calculadora.dec_to_oct(dec_int))
                except ValueError:
                    print("Erro: Entrada inválida. Digite um número decimal válido.")
            
            else:
                print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    print("Calculadora de conversão na base decimal \n")
    calculadora_principal = CalculadoraPrincipal()
    calculadora_principal.main()
