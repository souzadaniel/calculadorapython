while True:
    numero1 = input ('Digite o primeiro número: ')
    operador = input ('Digite a operação (+-/* ou **): ')
    numero2 = input ('Digite o segundo número: ')
    
    try:
        numero1_float = 0
        numero2_float = 0
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print ('Um ou ambos números são inválidos.')
        continue
    
    operadores_permitidos =  ['+', '-', '*','/', '**']
    
    if operador not in operadores_permitidos:
        print ('Operador inválido.')
        continue
    
    print('Realizando sua conta. Aguarde...')
    
    if operador == '+':
        resultado = numero1_float + numero2_float
        print (f'A soma entre {numero1_float} e {numero2_float} é {resultado}.')
        
    if operador == '-':
        resultado = numero1_float - numero2_float
        print (f'A subtração entre {numero1_float} e {numero2_float} é {resultado}')
    
    if operador == '*':
        resultado =  numero1_float * numero2_float
        print (f'A multiplicação entre {numero1_float} e {numero2_float} é {resultado}')
        
    if operador == '/':
        resultado = numero1_float  / numero2_float
        print (f'A divisão entre {numero1_float} e {numero2_float} é {resultado}')
        
    if operador == '**':
        resultado = numero1_float ** numero2_float
        print (f'A exponenciação entre {numero1_float} e {numero2_float} é {resultado}')  

    sair = input ('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break