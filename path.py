from pathlib import Path
import os
import sys

BASE_DIR = Path(r'.\CarEmployeeManagementApp2')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))  # динамично добавяне на
# основната директория на проекта към пътя за търсене на Python (sys.path).
