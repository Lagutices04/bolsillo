
class bolsillo:
 def crearbolsillo(self):
  self.nombre=input("ingrese el nombre ")
  self.idbolsillo=int(input("ingrese el id de su bolsillo"))
  self.saldobolsillo=int(input("ingrese su saldo"))
  self. numCelularr=int(input("ingrese su telefono"))
  self. clavebolsilloo=int(input("ingrese su clave"))
  self.estadobolsillo=bool(input("ingrese el estado de su bolsillo"))
 
 def entrarbolsillo(self):
     numCelular=int(input("ingrese el numero de telefono"))
     clavebolsillo=int(input("ingrese la clave"))
    
     if self.clavebolsilloo == clavebolsillo and self.numCelularr == numCelular:
            print("El número de celular y la contraseña son válidos. Puedes ingresar a Nequi.")
     else:
            print("El número y contraseña ingresados no son válidos. No puedes ingresar a Nequi.")
            return 
        
    
     
            
            
     
 def consultarSaldo(self): 
       print("tu saldo actual es de ",self.saldobolsillo)
       
 def recargarSaldo(self):
    p=int(input("desea recargar su bolsillo, 1 para si,2 para no"))
    if(p==1):
        ingreSaldo=int(input("ingrese su saldo actual"))
       
        self.saldobolsillo+=ingreSaldo
        print("tu saldo actual es de",self.saldobolsillo)
    elif(p==2):
        print("no vas a recargar nada ")
#def sacarPlata(self,saldoBolsillo):
        #p=int(input("desea recargar su bolsillo, 1 para si,2 para no"))
        #if(p==1):
            #ingreSaldo=int(input("ingrese su saldo actual"))
        #elif(saldoBolsillo>=100000):
            #saldoActual=saldoBolsillo-saldoActual
            #print("como acabas de retirar ahora tu saldo actual es de",saldoActual)
        #else:
            #print("saldo insuficiente para retirar ")


    
    

    
     

     
    
 

 
 
 

      