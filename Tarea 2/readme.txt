El código fue echo para python 2.7

Las librerias necesarias son
- numpy
- scipy
- matplotlib
- ipython
- jupyter
- pandas
- sympy
- nose
- scikit-learn

Los scripts tienen el siguiente formato de nombre
s3_nItem.py: script para ejecutar una pregunta, no hace nada si se corre solo
s3_nItem_datset.py: script para correr una pregunta con dataset pequeño (s) o grande (g)

Ejemplo: s3_1_s.py
from s3_1 import run

run('TrainSet', 'TestSet', 's3_1_s_1to100inc1.log', 1, 101, 1)

Corre vecinos cercanos con datos pequeños y guarda el log en s3_1_s_1to100inc1.log

Al descomprimir los dataset tienen que llamarse asi:
 - TestSet: set test pequeño
 - TrainSet: set train pequeño
 - TestSet 2: set test grande
 - TrainSet 2: set train grande

Los zip no están incluidos en la entrega para que no sea tan pesada

(o puedes cambiar los strings en los archivos s3_nItem_s.py y s3_nItem_b.py)

El informe está escrito en Markdown (s3.md) y exportado a .pdf usando markdown-pdf de Atom
