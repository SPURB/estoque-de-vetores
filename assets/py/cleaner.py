#!/usr/bin/python
import os
import pathlib
import shutil
from .valid_extensions import valid_extensions

def clean(local):
	items = os.listdir(local)
	index_paths = list(map(lambda item: local + item, items))
	removed_files = 0
	removed_folders = 0

	for folder in index_paths:
		if os.path.isdir(folder):
			folder_itens = os.listdir(folder)

			for item in folder_itens:
				extension = pathlib.Path(folder + item).suffix # get extension
				extension = extension.lower()
				if not(extension in valid_extensions):
					path = folder + '/' + item
					if(os.path.isfile(path)):
						os.remove(path)
						print(path + ' removido')
						removed_files = removed_files + 1
					elif(os.path.isdir(path)):
						shutil.rmtree(path, ignore_errors=True)
						print(path + ' removido')
						removed_folders = removed_folders + 1
	

	if(removed_files > 0 and removed_folders == 0):
		print(str(removed_files) + ' arquivos removidos')
	elif(removed_files > 0 and removed_folders > 0):
		print(str(removed_files) + ' arquivos removidos.' + str(removed_folders) + ' pastas removidas')
	elif(removed_files == 0 and removed_folders > 0):
		print(str(removed_folders) + ' pastas removidas')
	elif(removed_files == 0 and removed_folders == 0): 
		print('Nenhum item removido')