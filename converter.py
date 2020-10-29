#!/usr/bin/env python 
import os
from nbconvert import PythonExporter
import nbformat

python_exporter = PythonExporter()

notebook_full_path = "training/model-code/train_predict_2.ipynb"

notebook_file = os.path.basename(notebook_full_path)

notebook_path = os.path.dirname(notebook_full_path)

notebook_name = os.path.splitext(notebook_file)

with open(notebook_full_path) as f:
    nb = nbformat.read(f, as_version=4)

python_data, resources = python_exporter.from_notebook_node(nb)

separator = '.'
py_file_ext = '.py'

python_file = os.path.join(notebook_path, notebook_name[0] + py_file_ext)

with open(python_file, "w") as f:
    f.write(python_data)
    f.close
