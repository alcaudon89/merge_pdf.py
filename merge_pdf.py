#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para fusionar dos PDFs:
    - '1.pdf' contiene las páginas impares en orden.
    - '2.pdf' contiene las páginas pares en orden invertido.
El script crea un PDF fusionado ('merged.pdf') con las páginas intercaladas.
"""

import PyPDF2

def merge_pdfs(pdf_impares_path, pdf_pares_path, output_pdf):
    """
    Función para fusionar dos PDF:
        - pdf_impares_path: Ruta al PDF con las páginas impares.
        - pdf_pares_path: Ruta al PDF con las páginas pares (en orden invertido).
        - output_pdf: Nombre del archivo PDF resultante.
    """
    # Abrir el archivo que contiene las páginas impares
    with open(pdf_impares_path, "rb") as file_impares:
        reader_impares = PyPDF2.PdfReader(file_impares)
        
        # Abrir el archivo que contiene las páginas pares
        with open(pdf_pares_path, "rb") as file_pares:
            reader_pares = PyPDF2.PdfReader(file_pares)
            
            # Guardamos las páginas pares y luego las invertimos
            paginas_pares = list(reader_pares.pages)[::-1]
            
            # Creamos el objeto PdfWriter para generar el PDF final
            writer = PyPDF2.PdfWriter()
            
            # Determinamos el número de páginas de cada PDF
            num_impares = len(reader_impares.pages)
            num_pares = len(paginas_pares)
            
            # Si la cantidad de páginas no coincide, se alerta y se usa el mínimo para intercalar
            num_iterar = min(num_impares, num_pares)
            if num_impares != num_pares:
                print("Advertencia: El número de páginas impares y pares no coincide.")
            
            # Intercalamos las páginas de forma que:
            #  - Se añade primero una página impar (del 1.pdf)
            #  - Luego la correspondiente página par (del 2.pdf ya invertido)
            for i in range(num_iterar):
                writer.add_page(reader_impares.pages[i])
                writer.add_page(paginas_pares[i])
            
            # Si alguno de los archivos tiene páginas restantes, se añaden al final
            if num_impares > num_iterar:
                for i in range(num_iterar, num_impares):
                    writer.add_page(reader_impares.pages[i])
            if num_pares > num_iterar:
                for i in range(num_iterar, num_pares):
                    writer.add_page(paginas_pares[i])
            
            # Escribimos el resultado en el archivo de salida
            with open(output_pdf, "wb") as out_file:
                writer.write(out_file)
            print(f"PDF fusionado creado exitosamente: {output_pdf}")

if __name__ == "__main__":
    # Los archivos '1.pdf' y '2.pdf' deben estar en el mismo directorio que este script.
    merge_pdfs("1.pdf", "2.pdf", "merged.pdf")
