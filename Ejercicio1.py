# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s8zZ7Y414B7SH-2vaLA5eggQKgLWNX8I
"""

def convertir_tiempo(segundos):
  horas = segundos // 3600
  minutos = (segundos - (horas *3600)) // 60
  segundos = segundos - (horas * 3600) - (minutos * 60)

  print(f"Horas: {horas}")
  print(f"Minutos: {minutos}")
  print(f"Segundos: {segundos}")

try:
  segundos = int(input("Ingrese cantidad de segundos"))

  convertir_tiempo(segundos)
except:
  print("Datos incorrectos")