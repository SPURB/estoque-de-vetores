import os
# import json
# from decimal import Decimal
# https://pythonspot.com/en/json-encoding-and-decoding-with-python/

n_filename = "nome.txt"
d_filename = "descricao.txt"
json_list = []

'''
'f' - retorna lista de arquivos
'd' - retorna lista de diretórios
'booth' - retorna dicionário de ambos
'''
def separateFilesDirectories(elem,path):
	directories = []
	files = []

	dir_files_list = path
	for d in dir_files_list:
		if os.path.isdir(d) == True:
			directories.append(d)
		else:
			files.append(d)

	booth = {'files':files, 'directories':directories}

	if elem == 'booth':
		return booth
	elif elem == 'files':
		return booth['files']
	elif elem =='directories':
		return booth['directories']
	else:
		print("type 'directories', 'files' or 'booth'")

# print(separateFilesDirectories('files',os.listdir()))

index_path = os.listdir()

for imagem in separateFilesDirectories('directories',index_path):
	name_path = imagem + '/' + n_filename
	name = open(name_path, 'r').read()

	description_path = imagem + '/' + d_filename
	description = open(description_path, 'r').read()

	png=[]
	path_list = os.listdir(imagem)

	for file_item in path_list:
		file_name, file_extension = os.path.splitext(file_item)

		if file_extension=='.png':
			png.append(file_item)

	json_list.append({'folder':imagem,'name':name,'description':description, 'png':png})

print(json_list)
base = open('base.js','w')
json_list_as_string = str(json_list)

for entry in json_list:
	entry_str = str(entry)
	if entry==json_list[-1]:
		base.write(entry_str+'\n')
	else:
		base.write(entry_str+','+'\n')
base.close()