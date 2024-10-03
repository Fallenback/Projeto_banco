menu = str( '''

    Selecione a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    
    ''')
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0

while True:

    opcao = input(menu)
    if opcao == '1':

            print("DEPOSITO".center(20, '-'))
            valor = float(input('Qual valor deseja depositar? R$ '))
            if valor > 0: 
                saldo += valor 
                extrato += f'Deposito: R${valor}\n'

            else:
                print('Valor Inválido')
            

    elif opcao == '2':

        print('SAQUE'.center(20, '-'))
        print('')
        
        valor = float(input('Qual valor deseja sacar? R$ '))
        sem_saldo = valor > saldo
        sem_saque = numero_saques >= LIMITE_SAQUES
        sem_limite = valor > limite

        if sem_saldo:
            print('Operação Invalida! Saldo insuficiente.')

        elif sem_saque:
            print('Operação Invalida! Limites de saques atingido.')

        elif sem_limite:
            print('Operação Invalida! Valor do saque excede o limite.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! Valor invalido.')



    elif opcao == '3':
        print('EXTRATO'.center(20, '-'))
        print('')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            print(extrato)
            print(f'Saldo: R${saldo:.2f}')  
            
        print('-' * 20)

    elif opcao == '0':
        break

    else:
        print('Opção Inválida! Selecione uma operação disponível.')
