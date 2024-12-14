import re
import random

def read_rules(file_path):
    rules = {}
    antiRules = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'([A-Z]):(\S+)', line)
            if match:
                nombre = match.group(1)
                contenido = match.group(2)
                rules[nombre] = contenido.split('/')
            match = re.match(r'(!A||!R):(\S+)', line)
            if match:
                nombre = match.group(1)
                contenido = match.group(2)
                rules[nombre] = contenido.split('/')
    return rules

def decompose_grammar(grammar):
    types = {'START':r'!R',
            'OPTION':r'([A-Z]|\([A-Z]+\))\?',
            'GROUP':r'(?<=\()[A-Z]+(?=\))',
            'CHOICE':r'[A-Z!\(\)?]+(?=/)|(?<=/)[A-Z!\(\)?]+',
            'CHAR':r'[A-Z]',
            'WEIGHT':r'!\d',
            }
    tok_regex = '|'.join(f'(?P<{key}>{value})' for key, value in types.items())
    for matchingObject in re.finditer(tok_regex, grammar):
        kind = matchingObject.lastgroup
        groupchar = matchingObject.group()
        yield (kind, groupchar)

def generate_word(gramatica_reglas, gramatica_X):
    if not gramatica_X:  # Si no quedan más reglas en la gramática X
        return ''  # Devolver una cadena vacía
    
    #Descubre si el proximo caracter la gramtica X es la raíz, una regla simple o un caracter no definido
    match = re.match(r'([A-Z])', gramatica_X[0])
    if gramatica_X == "!R":
        rule = "!R"
        gramatica_X = gramatica_X[1:]
    elif match:
        rule = gramatica_X[0]
    else:
        return gramatica_X[0]

    if rule in gramatica_reglas:  # Si la regla está definida en el diccionario
        char = random.choice(gramatica_reglas[rule])  # Seleccionar aleatoriamente un caracter
        if re.search(r'[A-Z]', char):  #Recorre la letra recursivamente si tiene un grupo
            aid=""
            for c in char:
                aid = aid+generate_word(gramatica_reglas, c)
            char=aid
        suffix = generate_word(gramatica_reglas, gramatica_X[1:])  # Generar recursivamente el resto de la palabra
        return char + suffix # Devolver la combinación actual
    else:
        return "{Exception:UndefinedRule}"
    
    

# Archivo de texto con las reglas
archivo_reglas = "test.txt"

# Leer las reglas del archivo
reglas = read_rules(archivo_reglas) 
gramatica = [x for x in decompose_grammar("EJ?AS!K/J?(FKS)?FN")]

print(reglas)
print()
#print(gramatica)



# Imprimir las combinaciones
i=0
lista=list()
while i<100:
    lista.append(generate_word(reglas, '!R'))
    i+=1
print(lista)

