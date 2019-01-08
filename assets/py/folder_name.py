#!/usr/bin/python
# return clean folder name

def folder_name(imagem):
	sections = [ 'blocos', 'pictogramas', 'infograficos' ]
	for section in sections:
		if imagem.find(section) is not -1: 
			folder_name = imagem.replace('./', '').replace(section, '').replace('/','')
			return folder_name