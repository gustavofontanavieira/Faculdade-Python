import os #importação da biblioteca do sistema operacional

#Criação da variável
#open() -> Utilizado para abrir um arquivo, 
#passe como parâmetro o que vamos fazer com arquivo
# o W, é para escrever, caso não exista, ele cria o arquivo
"""
'r'	Abre o arquivo para leitura (default).
'w'	Abre o arquivo para escrita, truncando o arquivo primeiro.
'x'	Cria um arquivo para escrita e falha, caso ele exista.
'a'	Abre o arquivo para escrita, acrescentando conteúdo ao final do arquivo, caso ele exista.
'b'	Modo binário.
't'	Modo texto (default).
'+'	Abre o arquivo para atualização (leitura ou escrita)."""
"""
arquivo1 = open("dados.txt", 'r', encoding='utf-8')

#retorna o caminho absoluto do arquivo
#relpath retorna apenas o nome do arquivo
#print(os.path.abspath(arquivo1.name))

#Escreve no arquivo
#arquivo1.write("Hello my felas")
print("Foi fechado: ", arquivo1.closed)
print("modo de abertura: ", arquivo1.mode)
print("caminho absoluto: ", os.path.abspath(arquivo1.name))
print("caminho relativo: ", os.path.relpath(arquivo1.name))

#Fecha o arquivo"
#arquivo1.close()



arquivo.name -> retorna o nome do arquivo
arquivo.mode -> modo como abri o arquivo
arquivo.closed -> verifica se o arquivo já foi fechado ou não retornando false ou true

os -> é um módulo
path -> é um submódulo de OS
relpath -> submodulo do path
os.path.relpath -> caminho relativo do arquivo
        abspath -> caminho absoluto do arquivo

"""


"""
Para ler o conteúdo de um arquivo é bem simples e sugestivo
Read() -> retorna todo o conteúdo do arquivo
Realine() -> retorna uma linha de arquivo
Readlines() -> retorna uma lista onde cada elemento é uma linha do arquivo


#repr -> realProduct, retorna qual o valor verdadeiro que está dentro do arquivo

#Lembrando que ele segue como se fosse um enter a cada operação read
#se ele leu uma vez, o proximo read, independente de qual seja, será na proxima linha
print(repr(arquivo1.readlines()))
print(repr(arquivo1.readline()))
print(repr(arquivo1.read()))

arquivo_escrita = open('dados.txt1', 'w')
arquivo_escrita.write("Conteúdo da primeira linha")
arquivo_escrita.write("\nConteúdo da segunda linha")
arquivo_escrita.close()

linhas = ["Escrita da linha 1", "Escrita da linha 2", "Escrita da linha 3"]
arquivo_escrita2 = open('dados2.txt', 'w')
arquivo_escrita2.writelines(linhas) #escreve o arquivo de acordo com as linhas passadas no array
arquivo_escrita2.close()

#sempre que for abrir um arquivo, é boa prática utilizar o with, visto que ele vai fechar o arquivo
#sempre que terminar a execução dentro da sua identação, de forma que não precisamos fechar
with open("dados.txt", 'r') as arquivo:
    for linha in arquivo:
        print("dentro do with: ",linha)
    print("Fim do arquivo: ", arquivo.name)
exit() #encerra o programa

"""

#Arquivos binários -> imagens, vídeos, sons e etc.
"""
FLUXO DE TABALHO
-> Abrir imagem
-> TRANSFORMAR dados da imagem em array (numpy)
-> escrever um arquivo cópia
-> redimensionar o array (largura, altura, profundidade, cor, brilho e etc)
-> inverter dados
-> exibir
"""
"""
from PIL import Image
import numpy as np #bom para trabalhar com numeros

def main():
    #carrega imagem
    img = Image.open("icon.bin")
    
    #transforma os dados da imagem em um array
    img_data = np.array(img)
    #transforma em binario
    binary_data = img_data.tobytes()
    #mostra o tamanho da imagem quanto por quanto
    print(img_data.shape)

    # Salvar os dados binários em um arquivo
    with open("icon_new.bin", "wb") as file:
        file.write(binary_data)     

    #copia o arquivo binario
    with open("icon.bin", "rb") as original_file:
        data = original_file.read()

    with open("icon.bin", "wb") as copy_file:
        copy_file.write(data)

    # Manipulação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes
    with open("icon.bin", "rb") as file:
        data = bytearray(file.read())
    
    # Inverte todos os bytes
    data = data[::-1]

    with open("icon.bin", "wb") as file:
        file.write(data)
 
    # Carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()
 
main()

"""
"""
STRIP -> RETIRA DETERMINADOS CARACTERES DE UM INÍCIO E DO FINAL DE UM TEXTO
SPLIT -> QUEBRA UM TEXTO EM UM ARRAY
JOIN -> JUNTA CARACTERES UTILIZANDO UM SEPARADOR COMO PARAMETRO
COUNT -> CONTA




print("Olá {}, como você está, eu me chamo {}".format("João", "Gustavo"))
nomejoao = "João"
nomeGustavo = "Gustavo"
mensagem = f"Olá {nomejoao}, como você está, eu me chamo {nomeGustavo}"
print(mensagem)
    

valor = 3.1415
mensagem = f"Numero de pi é: {valor:.2f}"
print(mensagem)
"""

"""
CODIFICANDO MENSAGENS EM PYTHON

ZENIT POLAR -> Substitui as letras que estão na palavra ZENIT pelas que estão na POLAR
"""

def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title()  # Primeira letra de cada palavra em maiúscula
 
    # Dividir a frase em palavras
    words = phrase.split()
 
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(phrase) for word in words]
 
    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Coded:", coded_phrase)
 

main()