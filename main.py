from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kevarebri:qwFQguiHJ258wM0h@primeatlasplus.83ygb2v.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["sample_mflix"]

def menu_login():
    num: int = int(input ("Que quieres hacer???\n(1) Iniciar Sesion\n(2) Registrarse\n(0) Salir\n--> "))
    if num ==1:
        login()
    elif num ==2:
        registro(0)
    elif num ==0:
        print("Saliendo de la aplicacion")
    else:
        print("Opcion no valida\n")
        menu_login()

def login():
    autorizo = False
    print("INICIAR SESION")
    usuario = input("\tUsuario: ")
    contras = input("\tContraseña: ")
    try:
        comprobar_user = db["users"].find_one({"name":usuario, "password":contras})
        if(comprobar_user):
            autorizo = True
            print("Sesion iniciada como",usuario)
            if usuario == "admin" and contras == "admin":
                menuAdmin()
            else:
                pass   
    finally:
        pass
    
 

def registro(num:int):

    print("REGISTRAR USUARIO")
    
    usuario = input("Introduce el nombre de usuario: ")
    correo = input("Introduce el correo electronico: ")
    contrasenya = input("Introduce la contraseña: ")
    comp_contrasenya = input("Vuelve a introducir la contraseña: ")
    while (contrasenya != comp_contrasenya):
        print("Las contrasenyas no coinciden")
        contrasenya = input("Introduce la contraseña: ")
        comp_contrasenya = input("Vuelve a introducir la contraseña: ")
    try:
        user = {"name":usuario,"email":correo,"password":contrasenya}

        db["users"].insert_one(user)
    except Exception as e:
        print(e)
    
    print("\nUsuario registrado correctamente\n")
    if num == 0:
        menu_login()
    else:
        menuAdmin()
        

def menuAdmin():    
    print("Has entrado como administrador")
    num: int = int(input ("Que quieres hacer???\n(1) Crear usuario\n(2) Eliminar usuario\n(3) Añadir pelicula\n(4) Actualizar pelicula\n(0) Cerrar sesión\n--> "))
    if num == 1:
        registro(1)
    elif num == 0:
        menu_login()
    else:
        print("Numero no valido, intentelo nuevamente")
        menuAdmin()
    

def eliminarUsuario():
    print("ELIMINAR USUARIO")
    usuario = input("\tUsuario: ")
    contras = input("\tContraseña: ")
    try:
        db["users"].delete_one({"name":usuario, "password":contras})
    finally:
        pass
    print("Usuario eliminado")
    menuAdmin()
 

menu_login()