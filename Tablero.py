import os

J1="O"
lapiz="✎"
pase_escolar="✉" 
cuaderno="🀆"
telefono="☎" 
Mochila="M"

Tabla=[[0,10,20,30,40],[1,11,21,31,41],[2,12,22,32,42],[3,13,23,33,43],[4,14,24,34,44]]

juego=[[J1," "," "," ",Mochila],[" "," "," "," ",lapiz],[" ",pase_escolar," "," "," "],[" ",cuaderno," "," "," "],[" "," ",telefono," "," "]]

      
def mostrar(juego):
    
    print("---------------------")  
    print("|",juego[0][0],"|",juego[0][1],"|",juego[0][2],"|",juego[0][3],"|",juego[0][4],"|")
    print("---------------------")  
    print("|",juego[1][0],"|",juego[1][1],"|",juego[1][2],"|",juego[1][3],"|",juego[1][4],"|")
    print("---------------------")  
    print("|",juego[2][0],"|",juego[2][1],"|",juego[2][2],"|",juego[2][3],"|",juego[2][4],"|")
    print("---------------------")
    print("|",juego[3][0],"|",juego[3][1],"|",juego[3][2],"|",juego[3][3],"|",juego[3][4],"|")
    print("---------------------")  
    print("|",juego[4][0],"|",juego[4][1],"|",juego[4][2],"|",juego[4][3],"|",juego[4][4],"|")
    print("---------------------")

def posicion(x):
    for i in range(5):
        for c in range(5):
            n=juego[i][c]
            if (n==x):
                
                return Tabla[i][c]
def pi(x):
    for i in range(5):
        for c in range(5):
            n=juego[i][c]
            if (n==x):
                
                return i
def pc(x):
    for i in range(5):
        for c in range(5):
            n=juego[i][c]
            if (n==x):
                
                return c


def movimiento(J1):

    x=0
    while(x<1):
        mostrar(juego)
        a=str(input("¿A que direccion quieres ir? "))
        if((a=="w") or (a=="a") or (a=="s") or (a=="d")):
            l=pi(J1)
            c=pc(J1)
            if(a=="w"):
                if(l-1<0):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l-1][c]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="s"):
                if(l+1>4):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l+1][c]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="a"):
                if(c-1<0):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l][c-1]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="d"):
                if(c+1>4):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l][c+1]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
        else:
            os.system ("cls")
            print("Elija una tecla valida")
            
    
    



movimiento(J1)
