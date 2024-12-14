#!/bin/bash

# Define el patrón para los archivos comprimidos
patron="*.tar.gz"  # Cambiar según el formato: archivo.tar.gz, archivo.zip, etc.

# Obtén el directorio donde se encuentra el script
directorio_base="$(dirname "$0")"

# Recorre todas las carpetas en el directorio base
for carpeta in "$directorio_base"/*; do
    # Verifica si es una carpeta
    if [ -d "$carpeta" ]; then
        # Busca archivos que coincidan con el patrón en la carpeta actual
        for archivo_comprimido in "$carpeta"/$patron; do
            if [ -f "$archivo_comprimido" ]; then
                # Obtén el nombre del archivo sin la extensión
                nombre_base=$(basename "$archivo_comprimido" .tar.gz)
                carpeta_destino="$carpeta/$nombre_base"

                # Crea la carpeta de destino
                mkdir -p "$carpeta_destino"

                echo "Descomprimiendo $archivo_comprimido en $carpeta_destino"
                tar -xzf "$archivo_comprimido" -C "$carpeta_destino"
            else
                echo "No se encontró ningún archivo que coincida con $patron en $carpeta"
            fi
        done
    fi
done



