# Python 3.13.3
# kivy 2.3.1
# kivymd 1.2.0
from time import sleep

from Modelo.envVar import LoggedinStatus
from Modelo.envVar import root_dir
from Controlador.controlador import Controlador

from pathlib import Path
from kivymd.app import MDApp

class EditorApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controlador()
        self.logged_in = LoggedinStatus()

    def build(self):
        return self.controller.get_login_screen()


class EditorApp2(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controlador()

    def build(self):
        return self.controller.get_main_screen()

# Importamos los archivos por separado y los ejecutamos secuencialmente
EditorApp.kv_file = str(Path(root_dir, "Vista", "login.kv"))
EditorApp().run()
print ("CERRANDO APP 1")

print(f'{LoggedinStatus.get_logged_in('foo')}')

if LoggedinStatus.get_logged_in('foo'):
    print("USUARIO HA INICIADO SESIÓN, ABRIENDO APP 2")
    EditorApp2.kv_file = str(Path(root_dir, "Vista", "vista.kv"))
    EditorApp2().run()
