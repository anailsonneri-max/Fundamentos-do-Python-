# Qual objetivo do sistema:
# simulação de um banco

# o que banco tem?
# cadastro
# saldo
# saque
# deposito
# extrato

saldo = 5000.2 # real / float
senha = 1234

print('BANCO Z')
print('Seja bem Vindo(a)')
senha = int(input('Digite sua senha: '))
op = input('''
               Escolha a operação:

               1 - SAQUE
               2 - DEPOSITO
               3 - EXTRATO
               
               ''')

resultado = op == '1' and float(input('Você escolheu saque R$:')) - saldo or op == '2' and float(input('Você escolheu Deposito')) or ('Extrato:', saldo)
print(resultado)





