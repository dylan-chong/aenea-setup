import shutil
import os
from glob import glob

# Ensure working directory is the directory containing ".git"
if os.getcwd().endswith("/scripts"):
    os.chdir("..")

grammar_files = glob("./aenea-grammars/*")
for file in grammar_files:
    shutil.copy(file, "./MacroSystem/")
