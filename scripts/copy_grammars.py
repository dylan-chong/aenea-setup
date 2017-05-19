import shutil
import os

# Ensure working directory is the directory containing ".git"
if os.getcwd().endswith("/scripts"):
    os.chdir("..")

shutil.copyfile("./aenea-grammars/_vim/_vim.py", "./MacroSystem/_vim.py")
