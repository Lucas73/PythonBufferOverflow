#!/usr/bin/python
# coding: utf-8

import sys,socket

if len(sys.argv) != 5:
  print ("\nUso Correcto: python " + sys.argv[0] + " <dirección-ip>" + " <Port>" + " <Número-de-bytes>" + " <Nombre-de-archivo-de-salida>\n")
  sys.exit(0)

buffer = ["A"]
# overflow = "\xef\xbe\xad\xde"
ipAddress = sys.argv[1]
results = []

port = int(sys.argv[2])
contador = 1

while len(buffer) < int(sys.argv[3])+1:
  buffer.append("A"*contador)
  contador += 1
for strings in buffer:
  try:
    print ("Enviando %s bytes..." % len(strings))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("ENTRA") 
    s.connect((ipAddress, port))   
    s.recv(1024)
    s.send(strings + '\r\n')
    data = s.recv(1024)
    if data not in results: 
        print("DATA:",data) 
        variable = str((len(strings)))
        results.append(variable + ' Bytes\"A\" ' + data)
        print(results)
    else:
        print(results)
    s.close()
  except:
    print ("\nError de conexión...\n")
    sys.exit(0)

sys.stdout = open(str(sys.argv[4]), "w")
for index in results:
        print(index)
sys.stdout.close()

