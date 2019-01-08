#!/usr/bin/python
import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .joiner import create_base

class Watcher:
	def __init__(self):
		print('watching files...')
		self.observerPictogramas = Observer()
		self.observerBlocos = Observer()
		self.observerInfograficos = Observer()

	def run(self):
		pictogramas_evt_handler = Handler()
		self.observerPictogramas.schedule(pictogramas_evt_handler, './pictogramas/', recursive=True)
		self.observerPictogramas.start()

		blocos_evt_handler = Handler()
		self.observerBlocos.schedule(blocos_evt_handler, './blocos/', recursive=True)
		self.observerBlocos.start()

		infograficos_evt_handler = Handler()
		self.observerInfograficos.schedule(infograficos_evt_handler, './infograficos/', recursive=True)
		self.observerInfograficos.start()

		try:
			while True:
				time.sleep(5)
		except:
			self.observerPictogramas.stop()
			self.observerBlocos.stop()
			self.observerInfograficos.stop()
			print("stopped")

		self.observerPictogramas.join()
		self.observerBlocos.join()
		self.observerInfograficos.join()

class Handler(FileSystemEventHandler):
	@staticmethod
	def on_any_event(event):
		evt = event.event_type # created, moved, deleted or modified

		if (evt == 'created' or evt == 'deleted' or evt == 'moved'):
			parent_folder = os.path.dirname(event.src_path) + '/'
			grand_parent = os.path.dirname(os.path.dirname(event.src_path)) + '/'
			# print(grand_parent)

			if(parent_folder == './pictogramas/' or parent_folder == './blocos/' or parent_folder == './infograficos/'):
				create_base(parent_folder)
				# print('pai: ' + parent_folder)

			elif(grand_parent == './pictogramas/' or grand_parent == './blocos/' or grand_parent == './infograficos/'):
				create_base(grand_parent)
				# print('vô: ' + grand_parent)
		else:
			return None