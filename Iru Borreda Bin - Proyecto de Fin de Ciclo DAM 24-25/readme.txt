
Guía que utilizé para instalarme Kivy: 

1. Descárgue en instale la versión más reciente de Python: https://www.python.org/downloads/release/python-3133/

2. Una vez hecho, dentro de la consola de Pycharm o Visual Studio Code, instale Kivy utilizando el comando abajo

pip install kivy

Para comprobar que ha sido instalado de forma correcta, deberá poder ver que Kivy está entre los paquetes cuando ejecute 
pip list

IMPORTANTE: Si quiere ejecutar la el código fuente en VSCode, asegúrese de instalarse la extensión intérprete de Python. debería poder encontrarlo fácilmente con solo buscar "Python"

3. Para descargarse la versión 1.2.0 de KivyMD para que la tabla del menú principal funcione, escriba lo siguiente en la consola

pip install kivymd==1.2.0

4. Finalmente, debe descargarse el módulo de firebase-admin para que así la aplicación pueda conectarse a la base de datos.

pip install --upgrade firebase-admin

Las credenciales que están dentro del proyecto deberían seguir sirviendo para acceder a al DDBB