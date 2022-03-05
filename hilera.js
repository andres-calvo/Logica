/*Logica 2

Hileras

Representacion en vectores
Metodos a definir,  replace , borrado


Empezar definiendo el metodo posicion
*/
/*
    Posicion:
    iterar sobre la string
    si chartAt i == letra
    return i
    else return 0

sea s la String original
int posicion(String c)
    i=1
    n= c.longitud()
    while(i<= n) do
        char = s.subhilera(i,1)
        if(char == c)
            return i
        end(if)
        if(i == n)
            return 0
        end(if)
    end(while)

end(posicion)
*/

/*
/*
void agregar(String c)
    if(c.longitud() != 1)
        escriba("La longitud debe ser 1, no puede ser 0 ni mayor a 1")
    end(if)
    // Agregar el caracter c, al final del vector
    n = longitud()  // Longitud de mi hilera
    this.V[n + 1] = c  
end(agregar)
*/
/*

String subHilera(int i, int j)          // i es la posicion inicial
    n = this.longitud()                 // j es el número de caracteres a copiar
    if (i < 1  or  i > n) then
        escriba(“parámetro i errado”)
        return  null
    end(if)
    if (j < 0  or j > n – i + 1) then
        escriba(“parámetro j errado”)
        return null
    end(if)
    hilera  b = new hilera(j)
    for (k = i; k < i + j; k++) do
       b.agregar(this.V[k])
    end(for)
    b.V[0] = j                          // Aqui guardamos la longitud de la hilera
    return b

end(subHilera)

*/

/*
String concat(String t)
    String copy = this
    lt = t.longitud()
    ls = longitud()
    i = 1
    for (i; i<= lt ; i++) do
        copy.agregar(t.V[i])
    end(for)
    copy.V[0] = lt + ls
    return copy
end(concat)
*/

/*
void insert(String t, int i)
    if(i <= 0)
        escriba("Posicion negativa o fuera de rango")
        return
    end(if)
    if(i> this.V[0])    // Preguntar por esto
        escriba("No hay")
    end(if)
    primeraParte = this.subHilera(1,i)
    segundaParte = this.subHilera(i+1, longitud() )
    nuevaPrimeraParte = primeraParte.concat(t)
    final = nuevaPrimeraParte.concat(segundaParte)
    this = final  // Modificar la string original, reemplazandola con la final
end(insert)

*/

/*
// i posicion inicial
// j cuantos caracteres a partir de i
// t hilera a reemplazar en la hilera que invoca el metodo
void replace(int i, int j , String t)
    n=longitud() // 6
    if(i <= 0 or j <=0)
        escriba("Parametros i o j invalidos")
        return
    end(if)
    if(i == 1)
        partefinal = subHilera(j,longitud()-j)
        this = t.concat(partefinal)
        return 
    end(if)
    parte1 = subHilera(1,i) // "T"
    parte2 = subHilera(i+j,longitud()-i-j) 
    union = parte1.concat(t)
    final = union.concat(parte2)
    this = final

end(replace)

s = "Toloza" --> oloz
parte1 = T
parte2 = a --> index = 6 --> extrae de i+j = 2+ 4 = 6 hasta el final de la string, final de string seria longitud() - 6
t= "andresFelipe"
s.replace(2,4,"andresFelipe")
// TandresFelipe


*/

/*
// i Posicion inicial
// j cantidad de caracteres a borrar
// Modifica la hilera que lo invoca
void borrar(int i, int j)
    this.replace(i,j,"")
end(borrar)
*/



/*
posicion:
1)itero sobre el string
2)si i == a la letra:
return i


def posicion(a,string):
string=string.lower()
longitudStr=longitud(string)
for i in range(longitudStr):
    if string[i] == a:
        return i


def subHilera(posicionInicial,posicionFinal,string):
    posicionInicial=int(posicionInicial)
    posicionFinal=posicionInicial+posicionFinal
    s=""
        for i in range(posicionInicial,posicionFinal ):
            s=s+string[i]

    return s




# deben venir como vectores
def concatenar(stringUno,stringDos):
    vector=[]
    longitudUno=longitud(stringUno)-1
    longitudDos=longitud(stringDos)-1

    #Lleno el vector con los valores del primer string
    for i in range(longitudUno):
        vector[i]=stringUno[i]

    #Lleno el vector con los valores del segundo string
    for i in range (longitudUno,longitudDos):
        vector[i]=stringDos[i]
     
        
    return vector


string="pepito"
insertar(1,string,"hola")  
print(string) // pholaepito  

def insertar(posicion, string,subString):
    vectorAnterior=subHilera(0,posicion,string)
    longitudStr=longitud(string)
    vectorDespues=subHilera(posicion+1,longitudStr,string)

    unionUno=concatenar(vectorAnterior,subString)
    string=concatenar(unionUno,vectorDespues)
    
    return 


def reemplazar()


*/
