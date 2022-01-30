def leer_frase():
    global txt
    txt= (input("Ingrese arreglo de palabras: ")).lower()

def contar_letra_ingresada():
    letra = (input("Ingrese arreglo de palabras: ")).lower()
    conta = 0
    for i in txt:
        if(i.isalpha()):
            if(letra==i):
                conta+=1
    print(conta," ",len(txt))
leer_frase()
contar_letra_ingresada()
