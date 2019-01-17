#!/usr/bin/python
import os, struct, imghdr, json
from .folder_name import folder_name
from .valid_extensions import valid_extensions
from .hostname import get_host_url

hosturl = get_host_url('./host-public-folders.txt')

encoding='UTF8'

def get_image_size(fname):#http://stackoverflow.com/questions/8032642/ddg#20380514

		'''Determine the image type of fhandle and return its size. from draco'''
		with open(fname, 'rb') as fhandle:
				head = fhandle.read(24)
				if len(head) != 24:
						return
				if imghdr.what(fname) == 'png':
						check = struct.unpack('>i', head[4:8])[0]
						if check != 0x0d0a1a0a:
								return
						width, height = struct.unpack('>ii', head[16:24])
				elif imghdr.what(fname) == 'gif':
						width, height = struct.unpack('<HH', head[6:10])
				elif imghdr.what(fname) == 'jpeg':
						try:
								fhandle.seek(0) # Read 0xff next
								size = 2
								ftype = 0
								while not 0xc0 <= ftype <= 0xcf:
										fhandle.seek(size, 1)
										byte = fhandle.read(1)
										while ord(byte) == 0xff:
												byte = fhandle.read(1)
										ftype = ord(byte)
										size = struct.unpack('>H', fhandle.read(2))[0] - 2
								# We are at a SOFn block
								fhandle.seek(1, 1)	# Skip `precision' byte.
								height, width = struct.unpack('>HH', fhandle.read(4))
						except Exception: #IGNORE:W0703
								return
				else:
						return
				return width, height

def create_base(local):
	# have_full_img = False
	json_list = []
	items = os.listdir(local)
	index_paths = list(map(lambda item: local + '/' + item, items))
	nome_pagina = "'" + local.replace('./public/','')+ "'"
	nome_pagina = nome_pagina.title()

	for folder in index_paths:
		if os.path.isdir(folder):
			files_paths_list = os.listdir(folder)
			folder_absolute_path = hosturl + local.replace('./public/', '') + '/' + folder_name(folder)
			valid_files = []

			for file_item in files_paths_list:
				file_name, file_extension = os.path.splitext(file_item)

				if file_name.lower().endswith('_th') or file_name.lower().endswith('thumb'):
					thumb = file_item
					thumb_height = get_image_size(folder + '/'+file_item)[0]
					thumb_width = get_image_size(folder + '/'+file_item)[1]

				elif file_name.lower().endswith('_fl') or file_name.lower().endswith('_full'):
					full = file_item
					full_height = get_image_size(folder + '/'+ file_item)[0]
					full_width = get_image_size(folder + '/'+ file_item)[1]
					# have_full_img = True

				for valid in valid_extensions:
					if file_extension == valid:
						valid_files.append(file_item)

			try:
				json_list.append({
					"folder": folder_absolute_path,
					"thumb":{
						"name": thumb,
						"height": thumb_height,
						"width": thumb_width
					}
					, "full":{
						"name": full,
						"height": full_height,
						"width": full_width
						},
					"files": valid_files
				})
			except UnboundLocalError:
				json_list.append({
					"folder": folder_absolute_path,
					"thumb":{
						"name": thumb,
						"height": thumb_height,
						"width": thumb_width
					},
					"files": valid_files
				})

	file_name = nome_pagina.replace("'", '').lower()
	file_path = './public/_data/' + file_name +'.json'
	base = open(file_path,'w', encoding=encoding)
	# json_output = json.dumps(json_list, indent = 4 , sort_keys=True , ensure_ascii = False) # identado
	json_output = json.dumps(json_list, sort_keys=True , ensure_ascii = False)
	base.write(json_output)
	base.close()

	print(file_name + ' atualizado em ' + file_path)
	print('+---------------------------------------------------------------------------+')


def create_bases(directories_list):
	for directory in directories_list:
		create_base('./public/' + directory)

def sections(base_folder):
	valid_dirs = os.listdir(base_folder)
	valid_dirs.remove('_data')
	valid_dirs.remove('README.md')

	section_data = []

	for section in valid_dirs:
		home_images = base_folder + section
		files = os.listdir(home_images)
		section_images = list(filter(lambda file: file.lower().endswith(('.png', '.jpg', '.gif')), files))

		if len(section_images) == 0: 
			print("***IMPORTANTE***: Inclua uma imagem em (preferencialmente ): /public/" + section)
			print('+---------------------------------------------------------------------------+')

		section_images_obj = []

		for image in section_images:

			path = base_folder + section + '/' + image
			width = get_image_size(path)[0]
			height = get_image_size(path)[1]

			section_images_obj.append({
				'file': image,
				'width': width,
				'height': height
			})

		section_data.append({
			'name': section,
			'folder': hosturl + section,
			'images': section_images_obj
		})

	file_path = './public/_data/sections.json'
	base = open(file_path, 'w', encoding=encoding)
	# json_output = json.dumps(section_data, indent = 4 , sort_keys=True , ensure_ascii = False) # identado
	json_output = json.dumps(section_data, sort_keys=True , ensure_ascii = False) 
	base.write(json_output)
	base.close()
	print('secoes atualizadas em ' + file_path)
	print('+---------------------------------------------------------------------------+')
