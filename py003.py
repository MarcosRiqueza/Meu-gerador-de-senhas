import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    senha_gerada = gerar_senha(comprimento)
    print("Senha gerada:", senha_gerada)

if __name__ == "__main__":
    main()
