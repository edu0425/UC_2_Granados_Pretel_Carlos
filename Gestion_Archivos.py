# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:30:18 2022

@author: carlo
"""

import os
def crear_archivo(nombre, contenido):
    archivo=open(nombre, "wt")
    archivo.write(contenido)
    archivo.close()

    
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido_archivo(nombre, contenido):
    archivo=open(nombre, "at")
    archivo.write("\n"+contenido)
    
def leer_archivo(nombre):
    archivo=open(nombre, "rt", encoding='utf8')
    contenido=archivo.read()
    return contenido