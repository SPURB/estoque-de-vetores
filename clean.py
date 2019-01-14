import sys, os
from tasks.py import clean

public_folder = './public/'

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        folder = str(sys.argv[1])
        arguments = sys.argv
        del(arguments[0]) # remove 'update.py' da lista de argumentos
        clean.clean_directories(arguments) # cria base.json para a lista de argumentos

    else: 
        public_files = os.listdir(public_folder)
        public_files.remove('_data')
        valid_directories = list(filter(lambda x: os.path.isdir(public_folder + x), public_files)) # apenas diretorios de dentro de /public/
        clean.clean_directories(valid_directories) # cria base.json para todos os diretórios válido