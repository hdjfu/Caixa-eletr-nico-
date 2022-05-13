from time import sleep


#Funcao para limpar console
import os

def limpar():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


ac1 = '+criar'
ac2 = '+criar'
ac3 = '+criar'
login = 0

loop = 1
while loop == 1:
    if login == 0:
        limpar()
        print('===================')
        print('Entre com sua conta\n')

        print('[1]', ac1)
        print('[2]', ac2)
        print('[3]', ac3)

        opcao = input('\ndigite opção: ')

        #Slot 1
        if opcao == '1':    
            if ac1 == '+criar':
                limpar()
                print('=====================================')
                ac1 = input("\nQual será o nome da sua conta: ")
            login = 1 #A primeira conta está logada
            nome = ac1 #"nome" recebe o nome da conta que está logada

        #Slot 2
        if opcao == '2':    
            if ac2 == '+criar':
                limpar()
                print('=====================================')
                ac2 = input("\nNome para criar conta: ")
            login = 2
            nome = ac2

        #Slot 3
        if opcao == '3':    
            if ac3 == '+criar':
                limpar()
                print('=====================================')
                ac3 = input("\nDigite o nome para criar a conta: ")
            login = 3
            nome = ac3



        sleep(0.2)
        limpar()
        print('==========================')
        print('\nSeja bem vindo,', nome)
        sleep(1.5)
        limpar()


    
    #===============================
    #Apenas demonstração, não funciona
    print('====================')
    print('[%s]\n' %(nome))
    print('[1] Saque')
    print('[2] Depósito')
    print('[3] Transferência')
    print('[4] Extrato')
    a = input('\nDigite o que deseja realizar: ')
    limpar()
    #==================================


    print('====================')
    print('[%s]\n' %(nome))
    print('[1] Sair da conta')
    print('[2] Realizar outra ação')
    final = input('\nDigite a opção: ')

    if final == '1':
        login = 0 #desloga da conta
