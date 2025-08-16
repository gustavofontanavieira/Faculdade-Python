arquivo = open('dados.txt', 'r', encoding='utf-8')

abrirArquivo = arquivo.readline()
print(abrirArquivo)

#exibe o conteúdo em apenas uma linha com todas as quebrar de linha
#print(repr(abrirArquivo))

proximaLinha = arquivo.readline()
print(proximaLinha)

proximaLinha2 = arquivo.readline()
print(proximaLinha2)

proximaLinha2 = arquivo.readline()
print(proximaLinha2)

proximaLinha2 = arquivo.readline()
print(proximaLinha2)