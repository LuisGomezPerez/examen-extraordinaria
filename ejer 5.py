def hijosSinAmor(mochila,iteracion=0):
    if not mochila:
        print("Mochila vacía")
    if (mochila[iteracion]=="anillo de poder"):
        objetos= iteracion+1
        print("Si que contiene un anillo de poder, se ha conseguido sacar tras sacar " + str(objetos)  + " objetos")

    elif ((iteracion+1)== len(mochila)):
        print("No encontado")
        return encontrado,iteracion
    else:
        hijosSinAmor(mochila,iteracion+1)


mochila=["H","H","anillo de poder","H"]
mochila2=["H","H","w","H"]

encontrado= hijosSinAmor(mochila)
encontrado= hijosSinAmor(mochila2)