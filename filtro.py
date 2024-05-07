import json
def abrirArchivo():
    datos=[]
    with open("archivo.json", encoding="utf-8") as openfile:
        datos=json.load(openfile)
        return datos
    
def guardararchivo(midato):
    with open("archivo.json", "w") as mifile:
        json.dump(midato,mifile)

#miArchivo=abrirArchivo()
#nombre=input("nombre")
#miArchivo["nombre"]=nombre
#guardararchivo(miArchivo)

def menu():
    print("////////////// MENÚ //////////////\n"
          "\n"
          "1 agregar nuevo cliente\n")
def clienteOdaministrador():
    print("\n"
          "1 continuar como administrador\n"
          "2 continuar como cliente\n"
          "3 salir\n")
    
def servicios():
    print("eston son os servicios que tenemos para ti\n"
          "\n"
          "1 Internet de Fibra Óptica\n"
          "2 planes pospago\n"
          "3 prepago\n"
          "4 salir\n")

def pospago():
    print("    PLANES POSPAGO     \n"
          "1: un mes con 50GB por 50000$\n"
          "2: un mes con 70GB por 70000$\n"
          "3: un mes con 100GB por 90000$\n"
          "4: salir\n")
    
def prepago():
    print("     PREPAGO     \n"
          "1: 4GB por 7 dias\n"
          "2: 4GB por 7 dias\n"
          "3: 4GB por 7 dias\n"
          "4: salir\n")
    
miArchivo=abrirArchivo()
clienteOdaministrador()

verdadero=True
while verdadero==True:
    try:
        opc=int(input("escoje una opción:\n"))
        if opc==1:
            x1=True
            while x1==True:
                miArchivo=abrirArchivo()
                user=input("ingresa tu nombre de usuario (presiona enter si lo que quieres es salir)")
                if user!="":
                    contraseña=input("ingresa tu contraseña")
                else:
                    x1=False
            if user==miArchivo[1]["admin"] and contraseña==miArchivo[1]["contraseña"]:
                menu()
                v1=True
                while v1==True:
                    try:
                        opcadmin=int(input("escoje una opcion"))
                        if opcadmin==1:
                            print("ingresa sus datos")
                            nombre=input("nombre:  ")
                            apellido=input("apellido:  ")
                            direccion=input("direccion:  ")
                            v2=True
                            while v2==True:
                                try:
                                    contacto=int(input("contacto"))
                                except ValueError:
                                    print("ingresa una opción valida")
                            miArchivo[0]["clientes"].append({"nombre": nombre, "apellido": apellido, "direccion":direccion, "contacto": contacto, "categoria": "", "servicios": {}})
                    except ValueError:
                        print("ingresa una opción valida")
            clienteOdaministrador()
        if opc==2:
            x1=True
            while x1==True:
                miArchivo=abrirArchivo()
                user=input("ingresa tu nombre de usuario (presiona enter si lo que quieres es salir)")
                if user!="":
                    contraseña=input("ingresa tu contraseña")
                else:
                    x1=False
                for i in miArchivo[0]["clientes"]:
                    if i["user"]==user and i["contraseña"]==contraseña:
                        print("   bienvenido", i["nombre"])
                        servicios()
                        x2=True
                        while x2==True:
                            try:
                                opcplanes=int(input("escoje una opción\n"))
                                if opcplanes==1:
                                    print("el plan de fibra óptica cuesta 150000 al mes")
                                    siono=input("quieres adquirir el servicio?  (si)\n"
                                                "si no quieres presiona enter\n")
                                    if siono=="si":
                                        if "fibra óptica" not in i["servicios"]:
                                            i["servicios"]["fibra óptica"]=150000
                                        if "fibra óptica" in i["servicios"]:
                                            print("ya cuentas con este servicio")
                                            leer=input("deseas cancelar el servicio (si)"
                                                       "si no quieres presiona enter\n")
                                            if leer=="si":
                                                del i["servicios"]["fibra óptica"]
                                    servicios()
                                if opcplanes==2:
                                    pospago()
                                    x3=True
                                    while x3==True:
                                        try:
                                            pospa=int(input("escoje un plan\n"))
                                            if pospa==1:
                                                siono=input("estas seguro de comprar este plan (si)"
                                                            "presiona enter para cancelar")
                                                if siono=="si":
                                                    if "un mes con 70GB" not in i["servicios"] and "un mes con 100GB" not in i["servicios"]:
                                                        if "un mes con 50GB" not in i["servicios"]:
                                                            i["servicios"]["un mes con 50GB"]=50000
                                                        if "un mes con 50GB" in i["servicios"]:
                                                            print("ya cuentas con este servicio")
                                                            leer=input("deseas cancelar el servicio (si)"
                                                                    "si no quieres presiona enter\n")
                                                            if leer=="si":
                                                                del i["servicios"]["un mes con 50GB"]
                                            if pospa==2:
                                                siono=input("estas seguro de comprar este plan (si)"
                                                            "presiona enter para cancelar")
                                                if siono=="si":
                                                    if "un mes con 50GB" not in i["servicios"] and "un mes con 100GB" not in i["servicios"]:
                                                        if "un mes con 70GB" not in i["servicios"]:
                                                            i["servicios"]["un mes con 70GB"]=70000
                                                        if "un mes con 70GB" in i["servicios"]:
                                                            print("ya cuentas con este servicio")
                                                            leer=input("deseas cancelar el servicio (si)"
                                                                    "si no quieres presiona enter\n")
                                                            if leer=="si":
                                                                del i["servicios"]["un mes con 70GB"]
                                            if pospa==3:
                                                siono=input("estas seguro de comprar este plan (si)"
                                                            "presiona enter para cancelar")
                                                if siono=="si":
                                                    if "un mes con 70GB" not in i["servicios"] and "un mes con 50GB" not in i["servicios"]:
                                                        if "un mes con 100GB" not in i["servicios"]:
                                                            i["servicios"]["un mes con 100GB"]=90000
                                                        if "un mes con 100GB" in i["servicios"]:
                                                            print("ya cuentas con este servicio")
                                                            leer=input("deseas cancelar el servicio (si)"
                                                                    "si no quieres presiona enter\n")
                                                            if leer=="si":
                                                                del i["servicios"]["un mes con 100GB"]
                                            if pospa==4:
                                                x3=False
                                            if pospa<1 or pospa>4:
                                                print("ingresa una opción valida")
                                        except ValueError:
                                            print("ingresa una opción valida")

                                if opcplanes==4:
                                    x2==False
                            except ValueError:
                                print("ingresa una opción valida")
            clienteOdaministrador()
        
        if opc==3:
            verdadero=False
        if opc<1 or opc>3:
            print("ingresa una opción valida")
    except ValueError:
        print("ingresa una opción valida")