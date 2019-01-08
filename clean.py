import sys
from assets.py import cleaner

if __name__ == "__main__":
    folder = str(sys.argv[1])
    if(folder == 'all'):
        cleaner.clean('./pictogramas/')
        cleaner.clean('./blocos/')
        cleaner.clean('./infograficos/')
        
    else:
        cleaner.clean('./' + folder + '/')

