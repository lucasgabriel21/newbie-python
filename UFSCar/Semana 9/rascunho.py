arquivo = open('notas_estudantes.dat','w')
lista = ['Jose 10 15 20 30 40\n','Pedro 23 16 19 22\n','Suzana 8 22 17 14 32 17 24 21 2 9 11 17\n',
         'Gisela 12 28 21 45 26 10\n','Joao 14 32 25 16 89']
arquivo.writelines(lista)
arquivo.close()