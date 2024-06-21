from tkinter import *

#funciones útiles
def escribir( elemento ):
    """
    Closure generador de funciones que escriben sobre la pantalla
    """
    def func():
        contenido_str.set( contenido_str.get() + str( elemento ) )

    return func


def escribir_teclado( event ):
    if event.char == "\r":
        calcular()
    elif ( event.char.isalnum() ) or ( event.char in [ "+" , "-" , "*" , "/" , "." ] ):
        contenido_str.set( contenido_str.get() + str( event.char ) )
    elif event.char == "\x08" :
        borrar()    


def calcular():
    try:
        resultado = eval( contenido_str.get() )
        contenido_str.set( str( resultado ) )
    except:
        contenido_str.set( "Error" )


def borrar():
    """
    Borra un caracter de la pantalla o toda la pantalla si hay un error
    """
    if contenido_str.get() == "Error":
        contenido_str.set( "" )
    elif contenido_str.get() != "" :
        contenido_str.set( contenido_str.get()[ 0 : -1 ] )


#inicio y configuración inicial de la app
app = Tk()
app.geometry( "320x490+0+0" )
app.resizable( False , False )
app.title( "Calculadora by Gerabytes" )
icon = PhotoImage( file = "./assets/icons/calculadora.png" )
app.iconphoto( True , icon )


#panel contenedor, da el tamaño ppal de la app
panel = Frame( app , width = 640 , height = 480  )
panel.pack( )


#pantalla y su contenido
contenido_str = StringVar()
contenido_str.set( "" )
pantalla = Entry( panel , width = 35 , state = "disabled" , justify = "right" , bg = "white" , 
                textvariable = contenido_str ) 
pantalla.grid( row = 0 , column = 0 , columnspan = 4  , padx = 20 , pady = 20 )


#posiciones de los botones numéricos
buttons_list = []
buttons_numeric_position = [ ( 4 , 0 ) , ( 3 , 0 ) , ( 3 , 1 ) , ( 3 , 2 ) , 
                            ( 2 , 0 ) , ( 2 , 1 ) , ( 2 , 2 ) ,
                             ( 1 , 0 ) , ( 1 , 1 ) , ( 1 , 2 ) ]


for i in range( 10 ):
    buttons_list.append( Button( panel , 
                                width = 3 ,
                                height = 2 ,
                                text = str(i) , 
                                font = ( "Verdana" , 24 )  ,
                                command = escribir( i ) ) )
    buttons_list[ i ].grid( row = buttons_numeric_position[ i ][ 0 ] ,
                           column = buttons_numeric_position[ i ][ 1 ] )
    
    
#Se lee cualquier pulsación y se manda a la función escribir teclado para filtrar los eventos
app.bind( "<Key>" , escribir_teclado )


#Botones de operaciones
boton_plus = Button( panel , text = "+" , command = escribir( "+" ) ,
                    font = ( "Verdana" , 24 ) , width = 3 , height = 2 )
boton_plus.grid( row = 3 , column = 3 )

boton_minus = Button( panel , text = "-" , command = escribir( "-" ),
                    font = ( "Verdana" , 24 ) , width = 3 , height = 2  )
boton_minus.grid( row = 4 , column = 3 )

boton_times = Button( panel , text = "x" , command = escribir( "*" ),
                     font = ( "Verdana" , 24 ) , width = 3 , height = 2  )
boton_times.grid( row = 2 , column = 3 )

boton_divided = Button( panel , text = "/" , command = escribir( "/" ),
                       font = ( "Verdana" , 24 ) , width = 3 , height = 2  )
boton_divided.grid( row = 1 , column = 3 )

boton_equals = Button( panel , text = "=" , command = calcular , 
                      font = ( "Verdana" , 24 ) , width = 3 , height = 2  )
boton_equals.grid( row = 4 , column = 2 )

boton_dot = Button( panel , text = "." , command = escribir( "." ) ,
                   font = ( "Verdana" , 24 ) , width = 3 , height = 2 )
boton_dot.grid( row = 4 , column = 1  )

app.mainloop()