def dimensoesObjeto():
    try: 
        altura = float(input('Digite a altura do objeto (em cm): '))
        comprimento = float(input('Digite o comprimento do objeto (em cm): '))
        largura = float(input('Digite a largura do objeto (em cm): '))
        
        volume = altura * largura * comprimento
        
    except ValueError:
        print('Você digitou alguma dimensão do objeto com valor não numérico')
        print('Por favor, entre com as dimensões desejadas novamente.')
