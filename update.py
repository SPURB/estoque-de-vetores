import sys, os
from tasks.py import update

public_folder = './public/'

if __name__ == "__main__":

    update.sections(public_folder)

    if(len(sys.argv) > 1):
        arguments = sys.argv
        del(arguments[0]) # remove 'update.py' da lista de argumentos
        update.create_bases(arguments) # cria .json para a lista de argumentos
    else:
        public_files = os.listdir(public_folder)
        public_files.remove('_data')
        valid_directories = list(filter(lambda x: os.path.isdir(public_folder + x), public_files)) # apenas diretorios de dentro de /public/
        update.create_bases(valid_directories) # cria base.json para todos os diretórios válidos

