#!/usr/bin/python
from .sections import names

'''
List with all endpoints
'''
def get_all_endpoints(baseUrl):
	# list of sections endponints
	sectionsUrls = list(map(lambda item: baseUrl + item, names()))
	
	return {
		'/':{
			'url': baseUrl,
			'description': "base public folder's content"
		},
		'/valid-sections': {
			'url': baseUrl + 'valid-sections', 
			'description': 'list of sections'
		},
		'/:section':{ 
			'urls': sectionsUrls,
			'description': 'section content'
		}
	}
