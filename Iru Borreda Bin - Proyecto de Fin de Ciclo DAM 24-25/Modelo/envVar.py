from pathlib import Path

# Aquí establecemos el directorio root del proyecto una vez que se ejecuta la aplicación.
root_dir = Path(__file__).resolve().parent.parent

# Esta clase nos dirá si el usuario ha iniciado sesión correctamente
user_has_logged_in = False

class LoggedinStatus:

    def set_logged_in(bool):
        globals()['user_has_logged_in'] = bool

    def get_logged_in(self):
        return globals()['user_has_logged_in']