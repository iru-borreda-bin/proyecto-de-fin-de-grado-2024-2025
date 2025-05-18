# Python 3.13.3
# kivy 2.3.1
# kivymd 1.2.0
import re
from datetime import datetime

from Modelo.ddbb import Firebase
from Modelo.modelo import Modelo
from Vista.vista import AppMainMenu, MainMenuBox, EditorPopup, DataTable
from Vista.login import LoginScreen

class Controlador:
    def __init__(self):
        # Inicializamos el Modelo
        self.modelo = Modelo(controller=self)

        # Inicializamos las pantallas
        self.main_view = AppMainMenu(model=self.modelo, controller=self)
        self.main_menu = MainMenuBox(model=self.modelo, controller=self)
        self.table = DataTable(model=self.modelo, controller=self)
        self.screen_editor = EditorPopup(model=self.modelo, controller=self)
        self.login_view = LoginScreen(model=self.modelo, controller=self)

        # Inicializamos los datos
        self.loaded_cod_cli = 0

        self.login_email = ''
        self.login_passwd = ''

        self.signup_email = ''
        self.signup_passwd = ''
        self.signup_confpasswd = ''
        self.signup_nombre = ''
        self.signup_apellido = ''

        self.shirt_tam = ''
        self.shirt_des = '===='
        self.shirt_col_base = ''
        self.shirt_col_des = '===='

        self.shirt_txt_cont = '===='
        self.shirt_txt_pos = '===='
        self.shirt_txt_tam = '===='
        self.shirt_txt_col = '===='
        self.shirt_txt_tip = '===='

        self.shirt_logo = '===='
        self.shirt_logo_pos = '===='
        self.shirt_logo_tam = '===='
        self.shirt_logo_elev = '===='

    # Llamamos a estos datos para fijar las variables
    def set_login_email(self, email):
        self.login_email = email
#         print(f'{email}')
    def set_login_passwd(self, passwd):
        self.login_passwd = passwd
#         print(f'{passwd}')

    def set_signup_email(self, email):
        self.signup_email = email
        # print(f'{email}')
    def set_signup_passwd(self, passwd):
        self.signup_passwd = passwd
#         print(f'{passwd}')
    def set_signup_confpasswd(self, passwd):
        self.signup_confpasswd = passwd
#         print(f'{passwd}')
    def set_signup_nombre(self, nom):
        self.signup_nombre = nom
#         print(f'{nom}')
    def set_signup_apellido(self, ape):
        self.signup_apellido = ape
#         print(f'{ape}')

    def set_shirt_tam(self, tam):
        self.shirt_tam = tam
#         print(f'{tam}')
    def set_shirt_des(self, des):
        self.shirt_des = des
#         print(f'{des}')
    def set_shirt_col_base(self, col_base):
        self.shirt_col_base = col_base
#         print(f'{col_base}')
    def set_shirt_col_des(self, col_des):
        self.shirt_col_des = col_des
#         print(f'{col_des}')

    def set_shirt_txt_cont(self, cont):
        self.shirt_txt_cont = cont
#         print(f'{cont}')
    def set_shirt_txt_pos(self, pos):
        self.shirt_txt_pos = pos
#         print(f'{pos}')
    def set_shirt_txt_tam(self, tam):
        self.shirt_txt_tam = tam
#         print(f'{tam}')
    def set_shirt_txt_col(self, col):
        self.shirt_txt_col = col
#         print(f'{col}')
    def set_shirt_txt_tip(self, tip):
        self.shirt_txt_tip = tip
#         print(f'{tip}')

    def set_shirt_logo(self, logo):
        self.shirt_logo = logo
#         print(f'{logo}')
    def set_shirt_logo_pos(self, pos):
        self.shirt_logo_pos = pos
#         print(f'{pos}')
    def set_shirt_logo_tam(self, tam):
        self.shirt_logo_tam = tam
#         print(f'{tam}')
    def set_shirt_logo_elev(self, elev):
        self.shirt_logo_elev = elev
#         print(f'{elev}')

    # Enseña la pantalla principal
    def get_main_screen(self):
        return self.main_view

    # Enseña la pantalla de login
    def get_login_screen(self):
        return self.login_view

    # Manejo de datos de clientes
    def signup_validaciones (self):
        doc_cli = Firebase.login_cli_find(self.signup_email)

        print(f'{doc_cli}')
        print('He entrado en la función')
        if not self.signup_email or not self.signup_passwd or not self.signup_confpasswd or not self.signup_nombre or not self.signup_apellido:
            print('He devuelto False en espacios en blanco!')
            return False
        elif not self.validador_email(self.signup_email):
            print('He devuelto False en formato de email no correcto!')
            return False
        elif not self.signup_passwd == self.signup_confpasswd:
            print('He devuelto False en contraseñas no son iguales!')
            return False
        elif doc_cli:
            print('He devuelto False ya existe!')
            return False
        else:
            print('He devuelto True!')
            return True

    def login_validaciones (self):
        doc_cli = Firebase.login_cli_find(self.login_email)
        same_passwd = Firebase.login_cli_passwd_confirm (self.login_email, self.login_passwd)
        print(f'{doc_cli}')
        print('He entrado en la función')
        if not self.login_email or not self.login_passwd:
            print('He devuelto False en espacios en blanco!')
            return False
        elif not doc_cli:
            print('He devuelto False en usuario no existe!')
            return False
        elif not same_passwd:
            print('He devuelto False en contraseña no correcta!')
            return False
        else:
            print('He devuelto True!')
            return True

    def load_cli(self, email):
        doc = Firebase.login_cli_find(f"{email}")
        fecha_ped = doc['a_timestamp'].strftime("%Y/%m/%d %H:%M")
        fecha_act = doc['a_timestamp_ult_con'].strftime("%Y/%m/%d %H:%M")

        doc['a_timestamp'] = fecha_ped
        doc['a_timestamp_ult_con'] = fecha_act

        return doc

    def set_cod_cli(self):
        doc = Firebase.login_cli_find(self.login_email)
        self.modelo._login_cod_cli = doc['a_cod_cli']
        # print(f'Código de cliente: {doc['a_cod_cli']}')
        # print(f'Código de cliente en el Modelo: {self.modelo._login_cod_cli}')

    def set_last_con_cli(self):
        Firebase.cli_update_login_time(self.login_email)

    def signup_to_modelo (self):
        self.modelo.signup_email = self.signup_email
        self.modelo.signup_passwd = self.signup_passwd
        self.modelo.signup_nombre = self.signup_nombre
        self.modelo.signup_apellido = self.signup_apellido

        self.signup_email = ''
        self.signup_passwd = ''
        self.signup_nombre = ''
        self.signup_apellido = ''

    def cli_get_data(self):
        doc = Firebase.login_cli_find(f"{self.login_email}")

        fecha_ped = doc['a_timestamp'].strftime("%Y/%m/%d %H:%M")
        fecha_act = doc['a_timestamp_ult_con'].strftime("%Y/%m/%d %H:%M")

        doc['a_timestamp'] = fecha_ped
        doc['a_timestamp_ult_con'] = fecha_act

        # print(f'Doc: {doc}')
        # for field in doc:
        #     print(f'---{field} : {doc[field]}')
        # print(" ")
        # print("Datos recogidos")
        # print(" ")
        return doc

    def push_upload_cliente(self):
        self.modelo.cli_push_item_ddbb()
    # def push_update_cliente(self, cod_ped):
    #     self.modelo.ped_update_item_ddbb(cod_ped)
    # def push_delete_cliente(self, cod_ped):
    #     self.modelo.ped_delete_item_ddbb(cod_ped)

    # Manejo de datos de pedidos
    def ped_validaciones (self):
        print('He entrado en la función')
        if not self.shirt_tam or not self.shirt_col_base :
            print('He devuelto False en Obligatorio!')
            return False
        elif not self.shirt_des or not self.shirt_col_des :
            print('He devuelto False en Diseño!')
            return False
        elif not self.shirt_txt_cont or not self.shirt_txt_pos or not self.shirt_txt_tam or not self.shirt_txt_col or not self.shirt_txt_tip :
            print('He devuelto False en Texto!')
            return False
        elif not self.shirt_logo or not self.shirt_logo_pos or not self.shirt_logo_tam or not self.shirt_logo_elev :
            print('He devuelto False en Logo!')
            return False
        else:
            print('He devuelto True!')
            return True

    def ped_push_to_modelo(self):
        self.modelo.shirt_tam = self.shirt_tam
        self.modelo.shirt_des = self.shirt_des
        self.modelo.shirt_col_base = self.shirt_col_base
        self.modelo.shirt_col_des = self.shirt_col_des

        self.modelo.shirt_txt_cont = self.shirt_txt_cont
        self.modelo.shirt_txt_pos = self.shirt_txt_pos
        self.modelo.shirt_txt_tam = self.shirt_txt_tam
        self.modelo.shirt_txt_col = self.shirt_txt_col
        self.modelo.shirt_txt_tip = self.shirt_txt_tip

        self.modelo.shirt_logo = self.shirt_logo
        self.modelo.shirt_logo_pos = self.shirt_logo_pos
        self.modelo.shirt_logo_tam = self.shirt_logo_tam
        self.modelo.shirt_logo_elev = self.shirt_logo_elev

        self.shirt_tam = ''
        self.shirt_des = '===='
        self.shirt_col_base = ''
        self.shirt_col_des = '===='
        self.shirt_txt_cont = '===='
        self.shirt_txt_pos = '===='
        self.shirt_txt_tam = '===='
        self.shirt_txt_col = '===='
        self.shirt_txt_tip = '===='
        self.shirt_logo = '===='
        self.shirt_logo_pos = '===='
        self.shirt_logo_tam = '===='
        self.shirt_logo_elev = '===='

    def ped_get_data(self, cod_ped):
        doc = Firebase.ped_getDoc(f"[cod-cli]_pedido_{cod_ped}")
        
        fecha_ped = doc['a_timestamp'].strftime("%Y/%m/%d %H:%M")
        fecha_act = doc['a_timestamp_last_update'].strftime("%Y/%m/%d %H:%M")
        
        doc['a_timestamp'] = fecha_ped
        doc['a_timestamp_last_update'] = fecha_act
        
        # print(f'Doc: {doc}')
        # for field in doc:
        #     print(f'---{field} : {doc[field]}')
        # print(" ")
        # print("Datos recogidos")
        # print(" ")
        return doc

    def push_upload_shirt(self):
        self.modelo.ped_push_item_ddbb()
    def push_update_shirt(self, cod_ped):
        self.modelo.ped_update_item_ddbb(cod_ped)
    def push_delete_shirt(self, cod_ped):
        self.modelo.ped_delete_item_ddbb(cod_ped)

    # Patrón para reconocer si un email está bien escrito
    def validador_email (self, email):
        pattern = (r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
                   r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
        return re.match(pattern, email) is not None