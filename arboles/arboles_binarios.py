class NodoArbol:
    def __init__( self , value , left=None , right=None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert( self , value ):
        #Regla 1
        if self.__root == None:
            self.__root = NodoArbol( value, None , None)
        #Regla 2
        else:
            self.__insert__( self.__root ,  value)

    def __insert__( self , nodo , value ):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            #Regla 1
            if nodo.left == None:
                nodo.left=NodoArbol(value)
            #Regla 2
            else:
                self.__insert__( nodo.left , value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol( value )
            else:
                self.__insert__(nodo.right , value)

    def __recorrido_in( self , nodo
        if nodo !==None:
            self.__recorrido_in(nodo.left)
            print(nodo.data , end = " , ")
            self.__recorrido_in(nodo.right)
