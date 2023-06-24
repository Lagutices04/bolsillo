from Bolsillo import bolsillo
usuario=bolsillo()

class usuario(bolsillo):
    def recargarSaldo(self):
     p=int(input("desea recargar su bolsillo, 1 para si,2 para no"))
     if(p==1):
        ingreSaldo=int(input("ingrese su saldo actual"))
       
        self.saldobolsillo+=ingreSaldo
        print("tu saldo actual es de",self.saldobolsillo)
     elif(p==2):
        print("no vas a recargar nada ")

