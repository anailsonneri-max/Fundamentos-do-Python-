# e-commerce
alunos = []
medias = []


pergunta = input('deseja acessar?').lower()
while pergunta == 'sim':
    
    for i in range(3):
        senha = input('senha:')
        if senha == '123':
            print('sistema de notas..')
            nome = input('nome: ')
            nota1 = float(input('nota matematica:'))
            nota2 = float(input('nota ingles:'))
            nota3 = float(input('nota quimica:'))
            media = (nota1+nota2+nota3) / 3
            print('media', media, 'Aluno(a):', nome)
            alunos.append(nome)
            medias.append(media)
            pergunta = input('deseja continuar?')
            if pergunta != 'sim':
                print('lista de alunos')
                print(alunos)
                print('media')
                print(medias)
                print('media da sala: ', sum(medias)/len(medias))
                print('***' * 8)
        else:
             print('senha incorreta')
    else:
        print('senha bloqueada...')
        break
else:
    print('até logo...')