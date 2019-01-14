import os
#!/usr/bin/python
# return clean folder name 
# imagem './public/blocos/arvore_01' return 'arvore_01'

def folder_name(imagem):
	sections = os.listdir('./public/')
	sections.remove('_data')

	for section in sections:
		if imagem.find(section) is not -1: 
			folder_name = imagem.replace('./public/', '').replace(section, '').replace('/','')
			return folder_name