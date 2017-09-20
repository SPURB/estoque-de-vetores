import os
import struct
import imghdr

def get_image_size(fname):#http://stackoverflow.com/questions/8032642/ddg#20380514
		'''Determine the image type of fhandle and return its size.
		from draco'''
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


encoding='UTF8'
n_filename = "nome.txt"
d_filename = "descricao.txt"
have_full_img = False
json_list = []
index_path = os.listdir()

for imagem in index_path:
	name_path = imagem + '/' + n_filename
	desc_path = imagem + '/' +d_filename
	if os.path.isdir(imagem) and os.path.isfile(name_path) and os.path.isfile(desc_path):
		name = open(name_path,'r', encoding=encoding).read()
		description = open(desc_path,'r', encoding=encoding).read()

		path_list = os.listdir(imagem)
		valid_extensions = [
		'.jpg',
		'.png',
		'.gif',
		'.pdf',
		'.svg',
		'.eps',
		'.ai,',
		'.psd',
		'.skp',
		'.dwg',
		'.dxf']

		valid_files = []

		for file_item in path_list:
			file_name, file_extension = os.path.splitext(file_item)

			if file_name.lower().endswith('th') or file_name.lower().endswith('thumb'):
				thumb = file_item
				thumb_height = get_image_size(imagem+'/'+file_item)[0]
				thumb_width = get_image_size(imagem+'/'+file_item)[1]

			elif file_name.lower().endswith('fl') or file_name.lower().endswith('full'):
				full = file_item
				full_height = get_image_size(imagem+'/'+file_item)[0]
				full_width = get_image_size(imagem+'/'+file_item)[1]
				have_full_img = True

			for valid in valid_extensions:
				if file_extension == valid:
					if file_name.lower().endswith('th')==False and file_name.lower().endswith('thumb')==False:
						valid_files.append(file_item)
					elif have_full_img==False:
						valid_files.append(file_item)

		if have_full_img == False:
			full = False
			full_height = False
			full_width = False

		json_list.append({
			'folder':imagem,
			'name':name,
			'description':description, 
			'thumb':{
				'name':thumb,
				'height':thumb_height,
				'width':thumb_width
				},
			'full':{
				'name':full,
				'height':full_height,
				'width':full_width
				},
				'files':valid_files
		})
	# else:
	# 	print(imagem, " 'sem nome.txt'")

base = open('base.js','w', encoding=encoding)
json_list_as_string = str(json_list)

for entry in json_list:
	entry_str = str(entry)
	if entry==json_list[-1]:
		base.write(entry_str+'\n')
	else:
		base.write(entry_str+','+'\n')

base.close()