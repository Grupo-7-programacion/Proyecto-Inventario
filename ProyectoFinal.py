#Crear base de datos tabla
import os
import sqlite3
import time #para obtener la fecha del sistema
global ejecutivo,precioejecutivo,tradicional,preciotradicional,economico,precioeconomico
ejecutivo="Menu Ejecutivo"
precioejecutivo=200
tradicional="Menu Tradicional"
preciotradicional=100
economico="Menu Economico"
precioeconomico=50
# Definimos como variables globales los anteriormente mencionados

#Creamos la base de datos de los productos
try:# porque intentara volver a crear la tabla y nos dara un error y con estre try nos 
    #Establecemos conexion
    miconexion=sqlite3.connect('Inventario.db')
    micursor=miconexion.cursor()

    micursor.execute('''create table productos
                    (CODIGO int not null,
                    PRODUCTO text not null,
                    UNIDADES int not null,
                    PRECIO_DE_COMPRA real not null,
                    TOTAL real not null,
                    EXISTENCIA int not null,
                    FECHA_DE_COMPRA text not null)''')
    miconexion.close()
except Exception as e:
    print(e)    
    input()

#Creamos la base de datos de las ventas
try:
    conexion=sqlite3.connect("Ventas.db")
    cursor=conexion.cursor()
    #print("La base de datos se abrio correctamente")
    cursor.execute('''create table ventas
                    (ID_CLIENTE CHAR(4) PRIMARY KEY,
                    CLIENTE CHAR(20),
                    NIT CHAR(20),
                    MENU TEXT,
                    PRECIO REAL,
                    CANTIDAD INT,
                    TOTAL REAL)''')
    #print("Tabla creada con exito")
    conexion.close()
except Exception as e:
    print(e)    
    input()    




def compras():
    def ingreso_productos():
        
        continuar="s"
        
        while continuar=="s":
            os.system("cls")
            os.system("color 02") #primr numero es para pantalla y el segundo para la letra

            print("========================")
            print("= Ingreso de productos =")
            print("========================")
            
            
            miconexion=sqlite3.connect('Inventario.db')
            micursor=miconexion.cursor()

            codigo=int(input("DIjite el codigo del producto a ingresar "))  
            ingreso=(input("Digie el nombre del producto a ingresar "))
            costo=float(input("Costo de compra "))
            unidades=int(input("Ingrese cuantas unidades desea adquirir "))
            
            fecha=time.strftime("%d/%m/%Y")
            total=costo*unidades
            existencias=unidades
            os.system("cls")
            print("===================")
            print("= Ingreso exitoso =")
            print("===================")


            #Insertamos datos a la tabla
            micursor.execute('''insert into productos(CODIGO,PRODUCTO,UNIDADES,PRECIO_DE_COMPRA,TOTAL,EXISTENCIA,FECHA_DE_COMPRA)
                            values('%s', '%s', '%s', '%s','%s','%s','%s')''' % (codigo,ingreso,unidades,costo,total,existencias,fecha))
            miconexion.commit()
            miconexion.close()  

            continuar=input("Desea  continuar[s/n] ")
    def mostrar_prouctos():
        os.system("cls")
        print("==============================================")
        print("= LISTADO DE TODOS LOS PRODUCTOS REGISTRADOS =")
        print("==============================================")
        miConexion=sqlite3.connect("Inventario.db")
        miCursor=miConexion.cursor()

        miCursor.execute("Select * from productos")#order by PRODUCTO
        
        listado=miCursor.fetchall()
        from tabulate import tabulate
       
        print(tabulate(listado,headers=["CODIGO"," PRODUCTO","UNIDADES","PRECIO_DE_COMPRA","TOTAL","EXISTENCIA","FECHA_DE_COMPRA"],tablefmt="fancy_grid"))
        os.system("pause")
    def mostrar_productos_criterio():
        os.system("cls")
        print("==============================")
        print("= Mostrar datos por criterio =")
        print("==============================")
        
        miConexion=sqlite3.connect("Inventario.db")
        miCursor=miConexion.cursor()

        buscar=input("Digite el codigo que sea buscar  ")

        miCursor.execute(f"Select CODIGO,PRODUCTO,UNIDADES,PRECIO_DE_COMPRA,TOTAL,EXISTENCIA,FECHA_DE_COMPRA from productos where CODIGO=={ buscar}")# el where realiza una busqueda en la base de datos
        mostrar=miCursor.fetchall()
        from tabulate import tabulate
       
        print(tabulate(mostrar,headers=["CODIGO"," PRODUCTO","UNIDADES","PRECIO_DE_COMPRA","TOTAL","EXISTENCIA","FECHA_DE_COMPRA"],tablefmt="fancy_grid"))     
        os.system("pause")
    def modificar_datos():
        opcion=0        
        while opcion!=4:
            
            os.system("cls")
            print("=========================")
            print("= Modificacion de Datos =")
            print("=========================")
            print("Que desea modificar")
            print("1. Prodcuto")
            print("2. Precio de compra")
            print("3. Unnidades")
            print("4. Regresar")
            opcion=int(input("Digite una opcion "))
            if opcion==1:
                os.system("cls")
                codigo=int(input("Digite el codigo del producto a modificar "))
                producto=input("Digite el producto nuevo ")
                
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set PRODUCTO='%s' where CODIGO='%s'" %(producto,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Producto Modificado =")
                print("=======================")
                os.system("pause")       
            elif opcion==2:
                os.system("cls")
                codigo=int(input("DIgite el codigo del producto a modificar "))
                nuevo_precio=input("Digite el nuevo precio ")
                
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set PRECIO_DE_COMPRA='%s' where CODIGO='%s'" %(nuevo_precio,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Precio Modificado =")
                print("=======================")
                os.system("pause")  

            elif opcion==3:
                os.system("cls")
                codigo=int(input("DIgite el codigo del producto a modificar "))
                uni=input("Digite la cantidad de unidades ")
                
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set UNIDADES='%s' where CODIGO='%s'" %(uni,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Cantidad Modificado =")
                print("=======================")
                os.system("pause")
            elif opcion==4:
                break
    def eliminar_productos():
        os.system("cls")
        print("============================")
        print("= Eliminacion de productos =")
        print("============================")
        codigo=int(input("DIgite el codigo del producto a eliminar"))
        
    
        miconexion=sqlite3.connect('Inventario.db')
        micursor=miconexion.cursor()
        #eliminamos datos
        micursor.execute("delete from productos where CODIGO=:codigo ",
        {"codigo":codigo})

        miconexion.commit() #Guardamaos cambio
        miconexion.close()#cerramos la conexion
        os.system("cls")
        print("=======================")
        print("= Producto eliminado =")
        print("=======================")
        os.system("pause")

    opcion=0
    while opcion!=6:
        os.system("cls")
        print("=====================================")
        print("= Bienvenido al sistema de  Compras =")
        print("=====================================")
        print("1. Ingresar Productos")
        print("2. Mostrar datos")
        print("3. Mostrar datos por criterio")
        print("4. Modificar productos")
        print("5. Eliminar productos")
        print("6. Regresar")
        opcion=int(input("Seleccione una opcion ")) 
        if opcion==1:
            ingreso_productos()
        elif opcion==2:
            mostrar_prouctos()   
        elif opcion==3:
            mostrar_productos_criterio()    
        elif opcion==4:
            modificar_datos()
        elif opcion==5:
            eliminar_productos() 
        elif opcion==6:
            break    





def ventas():
    def menu_de_platillos():
        menu=0
        while menu!=4:
            
            import os 
            os.system("cls")
            # Limpiamos pantalla
            print("=====================")
            print("= Menu de platillos =")
            print("=====================")
            print("1. Menu Ejecutivo    Q.200.00")
            print("2. Menu Tradicional  Q.100.00")
            print("3. Menu Economico    Q.50.00")
            print("4. Regresar")
            menu=int(input("Seleccione el menu a adquirir "))
            if menu==1:
                menu_ejecutivo()

            if menu==2:
                pass
                menu_tradicional()

            if menu==3:
                pass
                menu_economico()
            elif menu==4:
                break    
            # Según la opción electa se realizará la acción correspondiente.

    def menu_ejecutivo():

        
        os.system("cls")
        # Limpiamos pantalla
        print("==================")
        print("= Menu Ejecutivo =")
        print("==================")
    
        print("Descripcion" )
        print("Filete termino medio, porcion de arroz, salsa blanca y copa de vino blanco,")
        print("Trozo de pai de queso, banana split y dulce de leche")
        
        

        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion a la base de datos
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
    
        idventaejecutivo=int(input("Ingrese ID del Cliente "))
        nombreejecutivo=input("Ingrese el nombre del comprador ")
        nit=input("Ingrese su nit ")
        cantidadejecutivo=int(input("Ingrese la cantidad de platillos "))
        os.system("cls")
        print("==================")
        print("= Compra exitosa =")
        print("==================")
        os.system("pause")

        totalejecutivo=int(precioejecutivo * cantidadejecutivo)

        cursor.execute('''insert into ventas(ID_CLIENTE,CLIENTE,NIT,MENU,PRECIO,CANTIDAD,TOTAL)
                    values('%s','%s','%s','%s','%s','%s','%s')''' % (idventaejecutivo,nombreejecutivo,nit,ejecutivo,precioejecutivo,cantidadejecutivo,totalejecutivo))
        # Agregamos información a nuestra base de datos
        conexion.commit()
        # Guardamos cambios
        conexion.close()
        # Cerramos la conexion

        def facturacion():

            os.system("cls")
            contador=0
            fecha=time.strftime("%d/%m/%Y")
            hora=time.strftime("%H:%M") #damos un formato a lo que etamos obteniendo
            print("\t\t\t==========================")
            print("\t\t\t= RESTUARANTE LA REUNION =")
            print("\t\t\t==========================")
                  
            print("============================\t\t---------------------------------------")
            print(f"= Factura Electronica No.{contador} =\t\t- Fecha de emision  {fecha}  {hora} -")
            print("============================\t\t---------------------------------------\n")
            contador+=1
           

            precioejecutivo=200
            totalejecutivo=float(precioejecutivo * cantidadejecutivo)
            
            print("---Datos del cliente---")  
            print(f"ID del cliente: {idventaejecutivo}")
            print(f"Nombre: {nombreejecutivo}")
            print(f"Nit: {nit}\n")
            print("---Detalle de factura---") 
            print("-------------------------------------------------------")
            print("Cantidad     Descripcion          Precio         Total")
            print("-------------------------------------------------------\n")
            print(cantidadejecutivo,"\t    ",ejecutivo,"     ",precioejecutivo,"\t\tQ.",totalejecutivo)
            print("\n\t\t ========================")
            print("\t\t = GACIAS POR SU COMPRA =")
            print("\t\t ========================")
            os.system("pause")


        facturacion()
    def menu_tradicional():
        import os
        os.system("cls")
        # Limpiamos pantalla
        print("=====================")
        print("= Menu Tradiccional =")
        print("=====================")

        print("Descripcion:")
        print("Filete termino medio, porcion de arroz, ensalada y agua gaseosa")
        print("Trozo de pastel de 3 leches y banana split")

        
        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion a la base de datos
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
        
        idventatradicional=int(input("Ingrese ID del Cliente "))
        nombretradicional=input("Ingrese le nombre del comprador ")
        nit=input("Ingrese su nit ")
        cantidadtradicional=int(input("Ingrese la cantidad de platillos "))
        os.system("cls")
        print("==================")
        print("= Compra exitosa =")
        print("==================")
        os.system("pause")

        totaltradicional=int(preciotradicional * cantidadtradicional)
        cursor.execute('''insert into ventas(ID_CLIENTE,CLIENTE,NIT,MENU,PRECIO,CANTIDAD,TOTAL)
                    values('%s', '%s', '%s', '%s','%s','%s','%s')''' % (idventatradicional,nombretradicional,nit,tradicional,preciotradicional,cantidadtradicional,totaltradicional))
        # Agregamos información a nuestra base de datos
        conexion.commit()
        # Guardamos cambios
        conexion.close()
        # Cerramos la conexion  

        def facturacion():

            os.system("cls")
            contador=0
            fecha=time.strftime("%d/%m/%Y")
            hora=time.strftime("%H:%M") #damos un formato a lo que etamos obteniendo
            print("\t\t\t==========================")
            print("\t\t\t= RESTUARANTE LA REUNION =")
            print("\t\t\t==========================")
                  
            print("============================\t\t---------------------------------------")
            print(f"= Factura Electronica No.{contador} =\t\t- Fecha de emision  {fecha}  {hora} -")
            print("============================\t\t---------------------------------------\n")
            contador+=1
           

            precioejecutivo=200
            totalejecutivo=float(precioejecutivo * cantidadtradicional)
            
            print("---Datos del cliente---")  
            print(f"ID del cliente: {idventatradicional}")
            print(f"Nombre: {nombretradicional}")
            print(f"Nit: {nit}\n")
            print("---Detalle de factura---") 
            print("-------------------------------------------------------")
            print("Cantidad     Descripcion            Precio       Total")
            print("-------------------------------------------------------\n")
            print(cantidadtradicional,"\t    ",tradicional,"     ",precioejecutivo,"\tQ.",totalejecutivo)
            print("\n\t\t ========================")
            print("\t\t = GACIAS POR SU COMPRA =")
            print("\t\t ========================")
            os.system("pause")


        facturacion()
    def menu_economico():
        import os
        os.system("cls")
        # Limpiamos pantalla
        print("==================")
        print("= Menu Ecomonico =")
        print("==================")

        print("Descripcion:")
        print("Pieza de pollo horneado, porcion de arroz y jugo de frutas")
        print("Banana split")

       
        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion a la base de datos
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
        
        idventaeconomico=int(input("Ingrese ID del Cliente "))
        nombreeconomico=input("Ingrese el nombre del comprador ")
        nit=input("Ingrese su nit ")
        cantidadeconomico=int(input("Ingrese la cantidad de platillos "))
        os.system("cls")
        print("==================")
        print("= Compra exitosa =")
        print("==================")
        os.system("pause")

        
        totaleconomico=int(precioeconomico * cantidadeconomico)
        cursor.execute('''insert into ventas(ID_CLIENTE,CLIENTE,NIT,MENU,PRECIO,CANTIDAD,TOTAL)
                    values('%s', '%s', '%s', '%s','%s','%s','%s')''' % (idventaeconomico,nombreeconomico,nit,economico,precioeconomico,cantidadeconomico,totaleconomico))
        # Agregamos información a nuestra base de datos
        conexion.commit()
        # Guardamos cambios
        conexion.close()
        # Cerramos la conexion

        def facturacion():

            os.system("cls")
            contador=0
            fecha=time.strftime("%d/%m/%Y")
            hora=time.strftime("%H:%M") #damos un formato a lo que etamos obteniendo
            print("\t\t\t==========================")
            print("\t\t\t= RESTUARANTE LA REUNION =")
            print("\t\t\t==========================")
                  
            print("============================\t\t---------------------------------------")
            print(f"= Factura Electronica No.{contador} =\t\t- Fecha de emision  {fecha}  {hora} -")
            print("============================\t\t---------------------------------------\n")
            contador+=1
           

            precioejecutivo=200
            totalejecutivo=float(precioejecutivo * cantidadeconomico)
            
            print("---Datos del cliente---")  
            print(f"ID del cliente: {idventaeconomico}")
            print(f"Nombre: { nombreeconomico}")
            print(f"Nit: {nit}\n")
            print("---Detalle de factura---") 
            print("-------------------------------------------------------")
            print("Cantidad     Descripcion          Precio         Total")
            print("-------------------------------------------------------\n")
            print(cantidadeconomico,"\t    ",economico,"     ",precioejecutivo,"\t\tQ.",totalejecutivo)
            print("\n\t\t ========================")
            print("\t\t = GACIAS POR SU COMPRA =")
            print("\t\t ========================")
            os.system("pause")


        facturacion()

    def platillos_vendidos():
        
        os.system("cls")
        # Limpiamos pantalla
        print("Listado de ventas realizadas")
       
        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion 
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
        cursor.execute("Select * from ventas")
        # Seleccionamos todos los elementos en la tabla venta
        lista_venta=cursor.fetchall()
        # Se convierten en listas los registros
        from tabulate import tabulate
        # Importamos la funcion tabulate
        print(tabulate(lista_venta,headers=["ID_CLIENTE","CLIENTE","NIT","MENU","PRECIO","CANTIDAD","TOTAL"],tablefmt="fancy_grid"))
        # Imprimimos los elementos de manera tabulada, agregando como encabezado las llaves
        # y usando un formato de tabla para mejorar la presentacion
        os.system("pause")
        # Pausamos hasta que el usuario presione una tecla
    def busqueda_criterio():
        
        os.system("cls")
        # Limpiamos pantalla
        print("===============================")
        print("= Busqueda datos por criterio =")
        print("===============================")

        print("Ingrese el nombre del cliente a busqueda ")
        criterionombre=input()
        os.system("pause")
        # Pausamos hasta que el usuario presione una tecla
        
        os.system("cls")
        # Limpiamos pantalla
        print("Listado de ventas realizadas")
        
        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion 
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
        sentencia="SELECT * FROM ventas WHERE CLIENTE LIKE ?;"
        # Seleccionamos todos los elementos en la tabla venta, columna CLIENTE ingresado por el usuario finalizando con LIKE
        cursor.execute(sentencia,["%{}%".format(criterionombre)])
        # Los caracteres de porcentaje(%) son para encontrar una coincidencia con el nombre digitado
        lista_venta=cursor.fetchall()
        # Se convierten en listas los registros
        from tabulate import tabulate
        # Importamos la funcion tabulate
        print(tabulate(lista_venta,headers=["ID_CLIENTE","CLIENTE","NIT","MENU","PRECIO","CANTIDAD","TOTAL"],tablefmt="fancy_grid"))
        # Imprimimos los elementos de manera tabulada, agregando como encabezado las llaves
        # y usando un formato de tabla para mejorar la presentacion
        
        os.system("pause")
        # Pausamos hasta que el usuario presione una tecla
    def modificar_datos():
        opcion1=0        
        while opcion1!=5:
            
            os.system("cls")
            print("=========================")
            print("= Modificacion de Datos =")
            print("=========================")
            print("Que desea modificar")
            print("1. Cliente")
            print("2. Nit")
            print("3. Menu")
            print("4. Cantidad de platillos")
            print("5. Regresar")
            opcion1=int(input("Digite una opcion "))
            if opcion1==1:
                os.system("cls")
                ID=int(input("Digite el ID del cliente a modificar "))
                nombre=input("Digite el nuevo nombre ")
                  
                miconexion=sqlite3.connect('Ventas.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update ventas set CLIENTE='%s' where ID_CLIENTE='%s'" %(nombre,ID))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Cliente Modificado =")
                print("=======================")
                os.system("pause")     

            elif opcion1==2:
                os.system("cls")
                ID=int(input("Digite el ID del cliente a modificar "))
                nuevo_nit=input("Digite el nuevo Nit")
                
                    

                    
                miconexion=sqlite3.connect('Ventas.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update ventas set NIT='%s' where ID_CLIENTE='%s'" %(nuevo_nit,ID))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Nit Modificado =")
                print("=======================")
                os.system("pause")  

            elif opcion1==3:
                menu=0
                while menu!=4:

                    os.system("cls")
                    # Limpiamos pantalla
                    
                    print("1. Menu Ejecutivo  Q.200.00")
                    print("2. Menu Tradicional  Q.100.00")
                    print("3. Menu Economico  Q.50.00")
                    print("4. Regresar")
                    
                    menu=int(input("Seleccione el nuevo menu "))
                    
                    if menu==1:
                        os.system("cls")
                        ID=int(input("Digite el ID del cliente a modificar "))
                        miconexion=sqlite3.connect('Ventas.db')
                        micursor=miconexion.cursor()
                        
                        
                        #Acutallizamos datos
                        micursor.execute("update ventas set MENU='%s' where ID_CLIENTE='%s'" %(ejecutivo,ID))
                        micursor.execute("update ventas set PRECIO='%s' where ID_CLIENTE='%s'" %(precioejecutivo,ID))
                        miconexion.commit() #Guardamos cambios
                        miconexion.close()#cerramos la conexion
                        os.system("cls")
                        print("===================")
                        print("= Menu Modificado =")
                        print("===================")
                        os.system("pause")

                    if menu==2:
                        os.system("cls")
                        ID=int(input("Digite el ID del cliente a modificar "))
                        miconexion=sqlite3.connect('Ventas.db')
                        micursor=miconexion.cursor()
                        #Acutallizamos datos
                        micursor.execute("update ventas set MENU='%s' where ID_CLIENTE='%s'" %(tradicional,ID))
                        micursor.execute("update ventas set PRECIO='%s' where ID_CLIENTE='%s'" %(preciotradicional,ID))
                        miconexion.commit() #Guardamos cambios
                        miconexion.close()#cerramos la conexion
                        os.system("cls")
                        print("===================")
                        print("= Menu Modificado =")
                        print("===================")
                        os.system("pause")

                    if menu==3:
                        os.system("cls")
                        ID=int(input("Digite el ID del cliente a modificar "))
                        miconexion=sqlite3.connect('Ventas.db')
                        micursor=miconexion.cursor()
                        #Acutallizamos datos
                        micursor.execute("update ventas set MENU='%s' where ID_CLIENTE='%s'" %(economico,ID))
                        micursor.execute("update ventas set PRECIO='%s' where ID_CLIENTE='%s'" %(precioeconomico,ID))
                        miconexion.commit() #Guardamos cambios
                        miconexion.close()#cerramos la conexion
                        os.system("cls")
                        print("===================")
                        print("= Menu Modificado =")
                        print("===================")
                        os.system("pause")   
            elif opcion1==4:
                os.system("cls")
                ID=int(input("Digite el ID del cliente a modificar "))
                nueva_cantidad=input("Digite la nueva cantidad de platillos ")
                
                    
                miconexion=sqlite3.connect('Ventas.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update ventas set CANTIDAD='%s' where ID_CLIENTE='%s'" %(nueva_cantidad,ID))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("====================================")
                print("= Cantidad de platillos Modificado =")
                print("====================================")
                os.system("pause")     
                        
            elif opcion1==5:
                break
    def eliminar_datos():
        import os
        os.system("cls")
        # Limpiamos pantalla
        print("Ingrese el ID del Cliente ")
        idclienteeliminar=input()
        os.system("cls")
        # Limpiamos pantalla
       
        conexion=sqlite3.connect("Ventas.db")
        # Realizamos la conexion a la base de datos
        cursor=conexion.cursor()
        # Situamos el cursor donde corresponde
        orden="DELETE FROM ventas WHERE rowid=?;"
        # Orden para eliminar
        cursor.execute(orden,[idclienteeliminar])
        # Eliminar registro
        conexion.commit()
        # Guardamos cambios
        conexion.close()
        # Cerramos la conexion
        os.system("cls")
        print("====================")
        print("= Datos Eliminados =")
        print("====================")
        os.system("pause")

    opcion1=0
    while opcion1!=6: # Ciclo repetitivo hasta que la opción electa sea 3.
        
        os.system("cls")
        # Limpiamos pantalla
        print("===================================")
        print("= Bienvenido al sistema de ventas =")
        print("===================================")

        print("1. Menu de platillos")
        print("2. Platillos vendidos")
        print("3. Busqueda por criterio")
        print("4. Modificar datos")
        print("5. Eliminar registro")
        print("6. Regresar")
        print("Seleccione una opcion")
        opcion1=int(input())
        if opcion1==1:
            menu_de_platillos()
        if opcion1==2:
           platillos_vendidos()
        if opcion1==3:
            busqueda_criterio()
        if opcion1==4:
            modificar_datos()
        if opcion1==5:
            eliminar_datos()
        if opcion1==6:
            break
        # Según la opción electa se realizará la acción correspondiente    



def inventario():
    def ingreso():
        
        continuar="s"
        
        while continuar=="s":
            os.system("cls")

            print("========================")
            print("= Ingreso de productos =")
            print("========================")
            
            
            miconexion=sqlite3.connect('Inventario.db')
            micursor=miconexion.cursor()

            codigo=int(input("DIjite el codigo del producto a ingresar "))  
            ingreso=(input("Digie el nombre del producto a ingresar "))
            costo=float(input("Costo de compra "))
            unidades=int(input("Ingrese cuantas unidades desea adquirir "))
            os.system("cls")
            print("===================")
            print("= Ingreso exitoso =")
            print("===================")
            total=costo*unidades
            existencias=unidades
            fecha=time.strftime("%d/%m/%Y")
            #Insertamos datos a la tabla
            micursor.execute('''insert into productos(CODIGO,PRODUCTO,UNIDADES,PRECIO_DE_COMPRA,TOTAL,EXISTENCIA,FECHA_DE_COMPRA)
                            values('%s', '%s', '%s', '%s', '%s', '%s', '%s')''' % (codigo,ingreso,unidades,costo,total,existencias,fecha))
            miconexion.commit()
            miconexion.close()


            continuar=input("Desea  continuar[s/n] ")
    def mostrar():
        os.system("cls")
        print("==============================================")
        print("= LISTADO DE TODOS LOS PRODUCTOS REGISTRADOS =")
        print("==============================================")
        miConexion=sqlite3.connect("Inventario.db")
        miCursor=miConexion.cursor()

        miCursor.execute("Select * from productos")
        
        listado=miCursor.fetchall()

        from tabulate import tabulate
       
        
        print(tabulate(listado,headers=["CODIGO"," PRODUCTO","UNIDADES","PRECIO_DE_COMPRA","Total","EXISTENCIA","FECHA_DE_COMPRA"],tablefmt="fancy_grid"))
        os.system("pause")           
    def mostrar_criterio():
        os.system("cls")
        print("============================")
        print("= Mostrar datos por codigo =")
        print("============================")
        
        miConexion=sqlite3.connect("Inventario.db")
        miCursor=miConexion.cursor()

        buscar=input("Digite el codigo que sea buscar  ")

        miCursor.execute(f"Select CODIGO,PRODUCTO,UNIDADES,PRECIO_DE_COMPRA,TOTAL,EXISTENCIA,FECHA_DE_COMPRA from productos where CODIGO=={ buscar}")# el where realiza una busqueda en la base de datos
        mostrar=miCursor.fetchall()
        from tabulate import tabulate
       
        print(tabulate(mostrar,headers=["CODIGO"," PRODUCTO","UNIDADES","PRECIO_DE_COMPRA","Total","EXISTENCIA","FECHA_DE_COMPRA"],tablefmt="fancy_grid"))     
        os.system("pause")    
    def modificar():         
        opcion4=0        
        while opcion4!=4:
            
            os.system("cls")
            print("=============================")
            print("= Modificacion de productos =")
            print("=============================")
            print("Que desea modificar")
            print("1. Prodcuto")
            print("2. Precio de compra")
            print("3. Unidades")
            print("4. Regresar")
            opcion4=int(input("Digite una opcion "))
            if opcion4==1:
                producto=input("Digite el producto nuevo")
                codigo=int(input("DIgite el codigo del producto a modificar"))
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set PRODUCTO='%s' where CODIGO='%s'" %(producto,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Producto Modificado =")
                print("=======================")
                os.system("pause")
                    
            elif opcion4==2:

                nuevo_precio=input("Digite el nuevo precio")
                codigo=int(input("DIgite el codigo del producto a modificar"))
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set PRECIO_DE_COMPRA='%s' where CODIGO='%s'" %(nuevo_precio,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Producto Modificado =")
                print("=======================")
                os.system("pause")  
            elif opcion4==3:

                uni=input("Digite la cantidad de unidades")
                codigo=int(input("DIgite el codigo del producto a modificar"))
                    

                    
                miconexion=sqlite3.connect('Inventario.db')
                micursor=miconexion.cursor()
                #Acutallizamos datos
                micursor.execute("update productos set UNIDADES='%s' where CODIGO='%s'" %(uni,codigo))
                miconexion.commit() #Guardamos cambios
                miconexion.close()#cerramos la conexion
                os.system("cls")
                print("=======================")
                print("= Producto Modificado =")
                print("=======================")
                os.system("pause")
            elif opcion4==4:
                break    
    def eliminar():
        os.system("cls")
        print("============================")
        print("= Eliminacion de productos =")
        print("============================")
        codigo=int(input("DIgite el codigo del producto a eliminar"))
        
    
        miconexion=sqlite3.connect('Inventario.db')
        micursor=miconexion.cursor()
        #eliminamos datos
        micursor.execute("delete from productos where CODIGO=:codigo ",
        {"codigo":codigo})

        miconexion.commit() #Guardamaos cambio
        miconexion.close()#cerramos la conexion
        os.system("cls")
        print("=======================")
        print("= Producto eliminado =")
        print("=======================")
        os.system("pause")

    opcion4=0
    while opcion4!=6:
        os.system("cls")
        print("============================")
        print("= Vienvenido al Inventario =")
        print("============================")

        print("1. Ingreso")
        print("2. Mostrar datos")
        print("3. Mostrar datos por criterio")
        print("4. Modificar")
        print("5. Eliminar productos")
        print("6. Regresar")
        opcion4=int(input("Digite una opcion " ))
        if opcion4==1:
            ingreso()
        elif opcion4==2:
            mostrar() 
        elif opcion4==3:
            mostrar_criterio()  
        elif opcion4==4:
            modificar() 
        elif opcion4==5:
            eliminar()  
        elif opcion4==6:
            break    
             



def menu_Principal():
    selecc=0
    while selecc!=4:
        os.system("cls")
        os.system("color 02") #primer numero es para pantalla y el segundo para la letra
        print("==========================")
        print("= RESTUARANTE LA REUNION =")
        print("==========================")
        print("1. Compra")
        print("2. Venta")
        print("3. Inventario")
        print("4. Salir")      #la factura y los clientes, las funciones estan implementadas dentro de la venta
        selecc=int(input("Seleccione una opcion"))
        if selecc==1:
            compras()
        elif selecc==2:
            ventas()
        elif selecc==3:
            inventario()
        elif selecc==4:
            break
                       
menu_Principal()



 