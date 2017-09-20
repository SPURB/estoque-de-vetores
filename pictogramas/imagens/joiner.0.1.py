import os

n_filename = "nome.txt"
d_filename = "descricao.txt"
json_list = []

index_path = os.listdir()

for imagem in index_path:
	name_path = imagem + '/' + n_filename
	desc_path = imagem + '/' +d_filename
	if os.path.isdir(imagem) and os.path.isfile(name_path) and os.path.isfile(desc_path):
		name = open(name_path,'r', encoding='UTF8').read()
		description = open(desc_path,'r', encoding='UTF8').read()

		png=[]
		path_list = os.listdir(imagem)

		for file_item in path_list:
			file_name, file_extension = os.path.splitext(file_item)

			if file_extension=='.png':
				png.append(file_item)

		json_list.append({'folder':imagem,'name':name,'description':description, 'png':png})
	else:
		print(imagem, " 'sem nome.txt'")

base = open('base.js','w', encoding='UTF8')
json_list_as_string = str(json_list)

for entry in json_list:
	entry_str = str(entry)
	if entry==json_list[-1]:
		base.write(entry_str+'\n')
	else:
		base.write(entry_str+','+'\n')

base.close()