# inicio da função dimensoesObjeto()
def dimensoesObjeto():
    global volume
    global valor
    while True: 
        try: 
            altura = float(input('Digite a altura do objeto (em cm): '))
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
            
            volume = altura * largura * comprimento
            
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor, entre com as dimensões desejadas novamente.')

        else:
            print(f'O volume do objeto (em cm²) é: {volume}')

            if volume < 1000:
                valor = 10
                break
            elif 1000 <= volume < 10000:
                valor = 20
                break
            elif 10000 <= volume <= 30000:
                valor = 30
                break
            elif 30000 <= volume < 100000:
                valor = 50
                break
            else:
                print('Não aceitamos objetos com dimensões tão grandes.')
                print('Entre com as dimensões desejadas novamente.')
# Fim da função dimensoesObjeto()

# inicio da função pesoObjeto()
def pesoObjeto():
    print('')
# Fim da função pesoObjeto()

# inicio da função rotaObjeto()
def rotaObjeto():
    print('')
# Fim da função rotaObjeto()


# Incio do Main
volume = 0
valor = 0
peso = 0
multiplicador = 0

print('------ Bem vindo(a) á Empresa de Logistica Naftaly Benedita Souza S.A. -------')
dimensoesObjeto()
pesoObjeto()
rotaObjeto()