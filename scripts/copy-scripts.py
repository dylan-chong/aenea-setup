#!/usr/bin/python

import shutil
import os

# Ensure working directory is the directory containing ".git"
if os.getcwd().endswith('/scripts'):
    os.chdir('..')

# Files and directories to copy into a new place. The destination is deleted
files_to_copy = [
    # (source file/directory name, source directory, destination directory)
    # Aenea files
    ('aenea/', './aenea/client/', './MacroSystem/'),
    ('vocabulary_config/', './aenea-grammars/', './MacroSystem/'),
    # Grammars
    ('_charwise_vim.py', './aenea-grammars/_charwise_vim/', './MacroSystem/'),
    ('_git.py', './aenea-grammars/_git/', './MacroSystem/'),
    ('git_commands.py', './aenea-grammars/_git/', './MacroSystem/'),
    # TODO Copy a list of folders instead of copy pastin}
]


def main():
    copy_files_and_dirs(files_to_copy)
    print ''
    print 'Done copying files!'


def ensure_ends_with_slash(path_str):
    if not path_str.endswith('/'):
        path_str += '/'
    return path_str


def ensure_path_doesnt_exist(path):
    if not os.path.exists(path):
        return

    print 'Removing existing file/directory ' + path
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def copy_files_and_dirs(file_tuples):
    for (file_or_dir_name, source_dir, destination_dir) in file_tuples:
        source = ensure_ends_with_slash(source_dir) + file_or_dir_name
        destination = (
            ensure_ends_with_slash(destination_dir) + file_or_dir_name
        )
        ensure_path_doesnt_exist(destination)

        print 'Copying {} to {}'.format(source, destination)
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy(source, destination)


if __name__ == '__main__':
    main()
