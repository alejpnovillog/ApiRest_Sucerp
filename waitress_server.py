try:
    # package python
    from waitress import serve
    import socket
    import logging

    # Libreria de la Aplicacion
    from app_App import app

except Exception as e:
    print(f'Falta algun modulo en waitress_server {e}')

# envia al  log
logging.basicConfig(level=logging.WARNING, filename='appwarning.log', filemode='a')

# Obtiene el Nombre del Host 
hostname = socket.gethostname()

# Obtiene la informacion de Red del Host
lista = socket.getaddrinfo(hostname, 5100)

# Obtiene el Ultimo valor de la Tupla
for x in lista[-1] :
    s = x

# Obtiene la direccion IP 
IP = s[0]
print(f'El servidor {IP}  ha inicicado...........')

# Levantar el servidor
serve(app.app, host=IP, port=5100)
