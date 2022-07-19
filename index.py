from flask import Flask, render_template 
app = Flask(__name__) # Le decimos a Flask que es nuestro archivo principal que vamos arrancar la aplicacion
                      # El objeto que devuelva Flask lo ponemos en variable app
# Esa variable la vamos a utilizar para poder crear las rutas del servidor,nuestras urls y demas.
# Para crear una ruta usamos un "decorador" con el metodo route le decimos la url principal que vera el usuario al arrancar.
@app.route('/')  # iniciamos el servidor.Podemos crear mas rutas tambien:
def home():      # esta funcion va a retornar al navegador en este caso un texto.
    #return 'Home Page'
    return render_template('home.html')

@app.route('/about')    
def about():
    #return 'About Page'
    return render_template('about.html')    

# Necesitamos que nuestra aplicacion del servidor se quede "escuchando", para ello preguntamos si estamos al inicio de
# de nuestra aplicacion. De ser cierto lo ejecutamos con run()
if __name__== '__main__':
    app.run(debug=True)   # Ponemos en modo prueba para no reiniciar cada vez que hay cambios




    