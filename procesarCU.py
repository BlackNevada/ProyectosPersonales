import re


def tokenize(textFile):
    types = {'INDEX':r'^#Section=Index:Begin[\s\S]+?#Section=Index:End',
             'FILETAG':r'^# Author: [\w\s.]+;[ \t]+Title: [\w\s.]+;[ \t]+Version: [\w\s.]+;[ \t]+Date: \d{4}/\d{2}/\d{2}',
             'SECTION':r'^# [a-zA-Z0-9 ]*',
             'ANY':r'[\s\S]+?',
            }
    tok_regex = '|'.join(f'(?P<{key}>{value})' for key, value in types.items())
    lista = list()
    for matchingObject in re.finditer(tok_regex, textFile, flags=re.MULTILINE):
        kind = matchingObject.lastgroup
        groupchar = matchingObject.group()
        lista.append((kind, groupchar))
    return lista

def indexar(tokens):
    indice = list(filter(lambda x: x[0] in ['INDEX', 'FILETAG', 'SECTION'], tokens))
    indice_texto = ""
    for elemento in indice:
    	if elemento[0] == 'INDEX':
    	    indice_texto = indice_texto+"Índice\n"
    	elif elemento[0] == 'FILETAG':
    	    indice_texto = indice_texto+"Rastreador\n"
    	elif elemento[0] == 'SECTION':
    	    indice_texto = indice_texto+"Sección:"+elemento[1][2:]+"\n"
    	    
    nuevo_texto = ""
    for elemento in tokens:
        if elemento[0] == 'INDEX':
            add = f"#Section=Index:Begin\n{indice_texto}#Section=Index:End"
        else:
            add = elemento[1]
    	
        nuevo_texto+=add
    return nuevo_texto
    


# Tokenizar el archivo
archivoTexto = ""
with open("Comandos útiles.txt", 'r') as file:
    for line in file:
        archivoTexto = archivoTexto+line
tokens = tokenize(archivoTexto)

archivoNuevo = indexar(tokens)
with open("Comandos útilesOut.txt", 'w') as file:
    file.write(archivoNuevo)

