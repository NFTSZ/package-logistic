# inicio da função dimensoesObjeto()
def dimensoesObjeto():
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
    global multiplicadorPeso
    while True:
        try: 
            peso = float(input('Digite o peso do objeto (em kg): '))
            
        except ValueError:
            print('Você digitou o peso do objeto com valor não numérico')
            print('Por favor, entre com o peso desejado novamente.')
            
        else: 
            if peso <= 0.1:
                multiplicadorPeso = 1
                break
            elif 0.1 <= peso < 1:
                multiplicadorPeso = 1.5
                break
            elif 1 <= peso < 10:
                multiplicadorPeso = 2
                break
            elif 10 <= peso < 30:
                multiplicadorPeso = 3
                break
            else:
                print('Não aceitamos objetos tão pesados.')
                print('Entre com o peso desejado novamente.')
# Fim da função pesoObjeto()

# inicio da função rotaObjeto()
def rotaObjeto():
    global multiplicadorRota
    while True:
        rotas = ['br', 'bs', 'rb', 'rs', 'sr', 'sb']
        print('Selecione uma rota: ')
        print('BR - De Brasília para Rio de Janeiro')
        print('BS - De Brasília para São Paulo')
        print('RB - De Rio de Janeiro para Brasília')
        print('RS - De Rio de Janeiro para São Paulo')
        print('SR - De São Paulo para Rio de Janeiro')
        print('SB - De São Paulo para Brasília')
        rota = str(input('>>> ')).lower()
        
        if rota in rotas:
            if rota == 'rs':
                multiplicadorRota = 1
            elif rota == 'sr' :
                multiplicadorRota = 1
            elif rota == 'bs':
                multiplicadorRota = 1.2
            elif rota == 'sb':
                multiplicadorRota = 1.2
            elif rota == 'br':
                multiplicadorRota = 1.5
            elif rota == 'rb':
                multiplicadorRota = 1.5
            break
        else:
            print('Você digitou uma rota que não existe')
            print('Por favor, entre com a rota desejada novamente.')
            continue
# Fim da função rotaObjeto()


# Incio do Main
# variáveis globais
valor = 0
multiplicadorPeso = 0
multiplicadorRota = 0

print('------ Bem vindo(a) á Empresa de Logística Naftaly Benedita Souza S.A. -------')
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
print(f'Total a pagar (R$): {valor * multiplicadorPeso * multiplicadorRota} (dimensões: {valor} * peso {multiplicadorPeso} * rota {multiplicadorRota})')
# Fim do Main