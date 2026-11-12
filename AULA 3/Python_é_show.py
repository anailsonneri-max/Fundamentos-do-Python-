# variável de testo e variável booleana
frase = 'Python é Show'
booleano = True # tem que ser letra maiscula

resultado = frase + ' '  + str(booleano) # convertendo booleano para texto

print(resultado)

# booleano (Thre ou False) valores booleanos sempre começam com a primeira letra maiúscula e não levam aspas.
# str() o python não permite juntar deretamente um texto com um booleano usando o sinal +
# a função str(booleano) transforma o valor True em texto para a concatenação funcionar.


