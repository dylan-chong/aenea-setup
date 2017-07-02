import shutil
import os

# Ensure working directory is the directory containing ".git"
if os.getcwd().endswith('/scripts'):
    os.chdir('..')

# Files and directories to copy into a new place. The destination is deleted
files_to_copy = [
    # (source file/directory name, source directory, destination directory)
    ('_vim.py', './aenea-grammars/_vim/', './MacroSystem/'),
    ('aenea/', './aenea/client/', './MacroSystem/')
    ]


def main():
    copy_files_and_dirs(files_to_copy)
    print 'Done copying files!'
    print '  If you just changed the grammars'
    print '    Then just turn the microphone off and on again inside Dragon'
    print '    to see the changes you have made'
    print '  Otherwise'
    print '    Restart Dragon to see the changes you have made'


def ensure_ends_with_slash(path_str):
    if not path_str.endswith('/'):
        path_str += '/'
    return path_str


def ensure_path_doesnt_exist(path):
    if not os.path.exists(path):
        return

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def copy_files_and_dirs(file_tuples):
    for (file_or_dir_name, source_dir, destination_dir) in file_tuples:
        source = ensure_ends_with_slash(source_dir) + file_or_dir_name
        destination = ensure_ends_with_slash(destination_dir) + file_or_dir_name

        ensure_path_doesnt_exist(destination)

        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy(source, destination)


if __name__ == '__main__':
    main()
