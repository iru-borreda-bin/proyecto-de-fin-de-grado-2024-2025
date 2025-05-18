# Python 3.13.3
# kivy 2.3.1
# kivymd 1.2.0

from Modelo.ddbb import Firebase
from Vista.vista import AppMainMenu, MainMenuBox, EditorPopup, DataTable

class Modelo:
    def __init__(self, controller):
        # Inicializamos las variables
        self.controller = controller

        # Las vistas
        self.main_view = AppMainMenu(model=self, controller=self.controller)
        self.main_menu = MainMenuBox(model=self, controller=self.controller)
        self.table = DataTable(model=self, controller=self.controller)
        self.editor_view = EditorPopup(model = self, controller = self.controller)

        # Las Variables
        self._login_cod_cli = 0

        self._signup_email = ''
        self._signup_passwd = ''
        self._signup_nombre = ''
        self._signup_apellido = ''

        self._shirt_tam = ''
        self._shirt_des = ''
        self._shirt_col_base = ''
        self._shirt_col_des = ''

        self._shirt_txt_cont = ''
        self._shirt_txt_pos = ''
        self._shirt_txt_tam = ''
        self._shirt_txt_col = ''
        self._shirt_txt_tip = ''

        self._shirt_logo = ''
        self._shirt_logo_pos = ''
        self._shirt_logo_tam = ''
        self._shirt_logo_elev = ''

    # Inicializamos las propidades de la clase incluyendo sus setters
    @property
    def login_cod_cli(self):
        return self._login_cod_cli
    @property
    def signup_email(self):
        return self._signup_email
    @property
    def signup_passwd(self):
        return self._signup_passwd
    @property
    def signup_nombre(self):
        return self._signup_nombre
    @property
    def signup_apellido(self):
        return self._signup_apellido

    @property
    def shirt_tam(self):
        return self._shirt_tam
    @property
    def shirt_des(self):
        return self._shirt_des
    @property
    def shirt_col_base(self):
        return self._shirt_col_base
    @property
    def shirt_col_des(self):
        return self._shirt_col_des

    @property
    def shirt_txt_cont(self):
        return self._shirt_txt_cont
    @property
    def shirt_txt_pos(self):
        return self._shirt_txt_pos
    @property
    def shirt_txt_tam(self):
        return self._shirt_txt_tam
    @property
    def shirt_txt_col(self):
        return self._shirt_txt_col
    @property
    def shirt_txt_tip(self):
        return self._shirt_txt_tip

    @property
    def shirt_logo(self):
        return self._shirt_logo
    @property
    def shirt_logo_pos(self):
        return self._shirt_logo_pos
    @property
    def shirt_logo_tam(self):
        return self._shirt_logo_tam
    @property
    def shirt_logo_elev(self):
        return self._shirt_logo_elev

    @login_cod_cli.setter
    def login_cod_cli(self, cod_cli):
        self._login_cod_cli = cod_cli

    @signup_email.setter
    def signup_email(self, email):
        self._signup_email = email
    @signup_passwd.setter
    def signup_passwd(self, passwd):
        self._signup_passwd = passwd
    @signup_nombre.setter
    def signup_nombre(self, nombre):
        self._signup_nombre = nombre
    @signup_apellido.setter
    def signup_apellido(self, apellido):
        self._signup_apellido = apellido

    @shirt_tam.setter
    def shirt_tam(self, tam):
        self._shirt_tam = tam
    @shirt_des.setter
    def shirt_des(self, des):
        self._shirt_des = des
    @shirt_col_base.setter
    def shirt_col_base(self, col_base):
        self._shirt_col_base = col_base
    @shirt_col_des.setter
    def shirt_col_des(self, col_des):
        self._shirt_col_des = col_des

    @shirt_txt_cont.setter
    def shirt_txt_cont(self, cont):
        self._shirt_txt_cont = cont
    @shirt_txt_pos.setter
    def shirt_txt_pos(self, pos):
        self._shirt_txt_pos = pos
    @shirt_txt_tam.setter
    def shirt_txt_tam(self, tam):
        self._shirt_txt_tam = tam
    @shirt_txt_col.setter
    def shirt_txt_col(self, col):
        self._shirt_txt_col = col
    @shirt_txt_tip.setter
    def shirt_txt_tip(self, tipo):
        self._shirt_txt_tip = tipo

    @shirt_logo.setter
    def shirt_logo(self, logo):
        self._shirt_logo = logo
    @shirt_logo_pos.setter
    def shirt_logo_pos(self, pos):
        self._shirt_logo_pos = pos
    @shirt_logo_tam.setter
    def shirt_logo_tam(self, tam):
        self._shirt_logo_tam = tam
    @shirt_logo_elev.setter
    def shirt_logo_elev(self, elev):
        self._shirt_logo_elev = elev

    def cli_data_to_dict (self):
        datos = {'b_email': self.signup_email,
                 'b_passwd': self.signup_passwd,
                 'c_apellido': self.signup_apellido,
                 'c_nombre': self.signup_nombre
                 }
        return datos

    def ped_data_to_dict (self):
        datos = {'b_tamano': self.shirt_tam,
                 'b_diseno': self.shirt_des,
                 'b_col_base': self.shirt_col_base,
                 'b_col_des': self.shirt_col_des,
                 'c_txt_cont': self.shirt_txt_cont,
                 'c_txt_pos': self.shirt_txt_pos,
                 'c_txt_tam': self.shirt_txt_tam,
                 'c_txt_col': self.shirt_txt_col,
                 'c_txt_tip': self.shirt_txt_tip,
                 'd_logo': self.shirt_logo,
                 'd_logo_pos': self.shirt_logo_pos,
                 'd_logo_tam': self.shirt_logo_tam,
                 'd_logo_elev': self.shirt_logo_elev
                 }
        return datos

    # Comandos ddbb

    def cli_get_items_dbbb (self):
        docs = Firebase.cli_getAll_items('foo')
        return docs

    def cli_push_item_ddbb (self):
        datos = self.cli_data_to_dict()
        Firebase.cli_push_item(datos)
        print('item pushed')

    def cli_update_item_ddbb (self, cod_cli):
        datos = self.ped_data_to_dict()
        Firebase.ped_update_item(datos, cod_cli)
        print('item modified')

    def cli_delete_item_ddbb (self, cod_ped):
        Firebase.ped_delete_item(cod_ped)

    def ped_push_item_ddbb (self):
        datos = self.ped_data_to_dict()
        Firebase.ped_push_item(datos, self.login_cod_cli)
        print('item pushed')

    def ped_update_item_ddbb (self, cod_ped):
        datos = self.ped_data_to_dict()
        Firebase.ped_update_item(datos, cod_ped)
        print('item modified')

    def ped_delete_item_ddbb (self, cod_ped):
        Firebase.ped_delete_item(cod_ped)

    def ped_get_items_dbbb (self):
        docs = Firebase.ped_getAll_items('foo')
        return docs