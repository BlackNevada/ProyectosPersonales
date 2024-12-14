import csv
import os
import re

# Ruta del archivo CSV
archivo_csv = 'data.csv'

# Crear un directorio para guardar las notas
os.makedirs('output', exist_ok=True)
os.makedirs('output2', exist_ok=True)

# Leer el archivo CSV
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Saltar el encabezado (si existe)
    next(reader, None)
    
    # Iterar sobre las filas del archivo CSV
    anonN=0
    for row in reader:
        # Título (columna 3)
        titulo = row[2]
        
        # Contenido (columna 2)
        contenido = row[1]
        
        horarios = re.findall(r'\w[a-z 0-9\-]+', contenido)
        
        # Nombre del archivo de la nota
        if titulo == "":
            nombre_archivo = f'output/anon{anonN}.md'
            anonN+=1
        else:
            nombre_archivo = f'output/{titulo}.md'
        
        # Crear la nota de horario en formato Markdown
        for h in horarios:
            with open(f'output2/{h}.md', 'w', encoding='utf-8') as nota:
                nota.write(f'[[Main]]\n\n')
                nota.write("#horario")
            
        
        # Crear la nota de persona en formato Markdown
        with open(nombre_archivo, 'w', encoding='utf-8') as nota:
            nota.write(f'# {titulo}\n\n')
            for h in horarios:
                nota.write(f"[[{h}]]\n")
                nota.write("#alumno")



