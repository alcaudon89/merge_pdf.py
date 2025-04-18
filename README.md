# 📄 Merge PDF - Odd & Even Pages Combiner

This is a simple Python script designed to merge two PDF files: one containing **odd pages in order** (e.g., 1, 3, 5...) and another containing **even pages in reverse order** (e.g., 6, 4, 2...). It's especially useful if you're using a scanner with an automatic feeder that doesn't support double-sided scanning.

### 🛠️ Why this script?

When scanning double-sided documents with a one-sided feeder, a common trick is:

1. First, scan the front side of all pages (1, 3, 5...) – this gives you `1.pdf`.  
2. Then, flip the stack, scan the back side (now in reverse order: 6, 4, 2...) – this gives you `2.pdf`.

This script combines both files into a properly ordered PDF: 1, 2, 3, 4, 5, 6... without any manual rearranging.

---

## 🚀 How to use it

### Requirements

- Python 3 installed on your system  
- The PyPDF2 library (install it with pip)

```bash
pip install PyPDF2
```

---

### ✅ Steps

1. Place both PDF files (`1.pdf` with odd pages, `2.pdf` with even pages in reverse) in the same folder as the script.  
2. Run the script with:

```bash
python merge_pdf.py
```

3. The script will merge both files and generate a new PDF called `merged_output.pdf`.

That’s it!

---

## 📝 Example

- `1.pdf`: pages 1, 3, 5, 7...  
- `2.pdf`: pages 8, 6, 4, 2...

➡️ Output: `merged_output.pdf` with pages in correct order: 1, 2, 3, 4, 5, 6, 7, 8

---

## 🇪🇸 Instrucciones en Español

### ¿Por qué este script?

Cuando escaneas documentos a doble cara con un escáner que **solo admite una cara**, puedes hacer lo siguiente:

1. Escanea primero todas las caras delanteras (páginas impares) → obtienes `1.pdf`
2. Luego das la vuelta al montón y escaneas las caras traseras → obtienes `2.pdf` (con las páginas pares pero en orden inverso)

Este script se encarga de unir esos dos archivos en un PDF final con todas las páginas en orden.

---

### Pasos para usarlo

1. Asegúrate de tener Python instalado.
2. Instala la librería necesaria:

```bash
pip install PyPDF2
```

3. Coloca los archivos `1.pdf` y `2.pdf` junto al script.
4. Ejecuta:

```bash
python merge_pdf.py
```

5. Obtendrás un archivo nuevo llamado `merged_output.pdf` con todas las páginas en orden.

---

👨‍💻 Simple, útil y sin necesidad de herramientas online o pagar por software extra.

---

¿Te preparo ahora el archivo `LICENSE` (MIT) y un `.gitignore` básico para Python?
