#!/usr/bin/python
from .readdata import read

def names():
    section_content = read('sections')
    output = []

    for section in section_content:
        output.append(section['name'])

    return output