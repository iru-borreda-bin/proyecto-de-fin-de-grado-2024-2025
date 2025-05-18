# Python 3.13.3
# kivy 2.3.1
# kivymd 1.2.0

from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton, MDTextButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.textfield import MDTextField

from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.metrics import dp
from kivymd.uix.widget import MDWidget

from Modelo.ddbb import Firebase
from Modelo.envVar import LoggedinStatus


class SignupUI (Popup, Widget):
    """
        Card de registración de usuarios
    """
    controller = ObjectProperty
    model = ObjectProperty

    def __init__(self, model, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.wrap = MDFloatLayout()
        self.add_widget(self.wrap)

        self.central_card = MDCard()
        self.central_card.size_hint = 0.6, 1
        self.central_card.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.central_card.elevation = 3
        self.central_card.padding = dp(25)
        self.central_card.spacing = dp(20)
        self.central_card.orientation = 'vertical'
        self.wrap.add_widget(self.central_card)

        self.txt_signup = MDLabel()
        self.txt_signup.text = "Bienvenido al Registro de Camisetas Custom!"
        self.txt_signup.font_size = dp(20)
        self.txt_signup.halign = 'center'
        self.txt_signup.size_hint_y = 0.2
        self.txt_signup.padding_y = dp(10)
        self.central_card.add_widget(self.txt_signup)

        self.txtF_email = MDTextField(hint_text="Email",
                                      text='',
                                      mode="rectangle",
                                      size_hint_x=.9,
                                      size_hint_y=None,
                                      height=dp(37.5),
                                      font_size=dp(17.5),
                                      padding_y=dp(10),
                                      pos_hint={"center_x": 0.5, "center_y": 0.5}
                                      )
        self.txtF_email.bind(text=self.set_view_signup_email)

        self.txtF_passwd = MDTextField(hint_text="Contraseña",
                                       text='',
                                       mode="rectangle",
                                       size_hint_x=.9,
                                       size_hint_y=None,
                                       height=dp(37.5),
                                       font_size=dp(17.5),
                                       pos_hint={"center_x": 0.5, "center_y": 0.5},
                                       password=True
                                       )
        self.txtF_passwd.bind(text=self.set_view_signup_passwd)

        self.txtF_confpasswd = MDTextField(hint_text="Confirme Contraseña",
                                       text='',
                                       mode="rectangle",
                                       size_hint_x=.9,
                                       size_hint_y=None,
                                       height=dp(37.5),
                                       font_size=dp(17.5),
                                       pos_hint={"center_x": 0.5, "center_y": 0.5},
                                       password=True
                                       )
        self.txtF_confpasswd.bind(text=self.set_view_signup_confpasswd)

        self.txtF_nombre = MDTextField(hint_text="Nombre",
                                      text='',
                                      mode="rectangle",
                                      size_hint_x=.9,
                                      size_hint_y=None,
                                      height=dp(37.5),
                                      font_size=dp(17.5),
                                      padding_y=dp(10),
                                      pos_hint={"center_x": 0.5, "center_y": 0.5}
                                      )
        self.txtF_nombre.bind(text=self.set_view_signup_nombre)

        self.txtF_apellidos = MDTextField(hint_text="Apellido",
                                      text='',
                                      mode="rectangle",
                                      size_hint_x=.9,
                                      size_hint_y=None,
                                      height=dp(37.5),
                                      font_size=dp(17.5),
                                      padding_y=dp(10),
                                      pos_hint={"center_x": 0.5, "center_y": 0.5}
                                      )
        self.txtF_apellidos.bind(text=self.set_view_signup_apellido)

        self.central_card.add_widget(self.txtF_email)
        self.central_card.add_widget(self.txtF_passwd)
        self.central_card.add_widget(self.txtF_confpasswd)
        self.central_card.add_widget(self.txtF_nombre)
        self.central_card.add_widget(self.txtF_apellidos)

        self.buttonBox = MDBoxLayout()
        self.buttonBox.orientation = "vertical"
        self.buttonBox.pos_hint = {'center_x': .5, 'center_y': .5}
        self.buttonBox.haling = 'center'
        self.buttonBox.padding = dp(15)
        self.buttonBox.padding_y = dp(15)
        self.buttonBox.spacing = dp(10)
        self.central_card.add_widget(self.buttonBox)

        self.buttonGrid = MDGridLayout()
        self.buttonGrid.cols = 3

        self.b_signup = MDRectangleFlatButton(text="Registrarse",
                                             font_size="20dp",
                                             size=("200dp", "50dp"),
                                             size_hint=(None, None),
                                             pos_hint={'center_x': .5, 'center_y': .5},
                                             on_press=self.on_SignUpAttempt)
        self.b_clear = MDTextButton(text="[b][u]Borrar campos[/u][/b]",
                                    markup=True,
                                    font_size="15dp",
                                    size=("200dp", "50dp"),
                                    size_hint=(None, None),
                                    pos_hint={'center_x': .5, 'center_y': .5},
                                    color=[74, 136, 237, 1],
                                    on_press=self.clearFields)
        self.b_cancel = MDRectangleFlatButton(text="Cancelar",
                                              font_size="20dp",
                                              size=("200dp", "50dp"),
                                              size_hint=(None, None),
                                              pos_hint={'center_x': .5, 'center_y': .5},
                                              on_press=self.closeSignUp4button)
        self.bufferWidget = MDWidget()
        self.bufferWidget.size_hint = .6, .1

        self.buttonBox.add_widget(self.b_clear)

        self.buttonBox.add_widget(self.buttonGrid)
        self.buttonGrid.add_widget(self.b_cancel)
        self.buttonGrid.add_widget(self.bufferWidget)
        self.buttonGrid.add_widget(self.b_signup)

    def clearFields(self):
        self.txtF_email.text = ''
        self.controller.signup_email('')
        self.txtF_passwd.text = ''
        self.controller.signup_passwd('')
        self.txtF_confpasswd.text = ''
        self.controller.signup_confpasswd('')
        self.txtF_nombre.text = ''
        self.controller.signup_nombre('')
        self.txtF_apellidos.text = ''
        self.controller.signup_apellido('')

    def set_view_signup_email(self, instance, text):
        self.txtF_email.text = f'{text}'
        self.controller.set_signup_email(text)

    def set_view_signup_passwd(self, instance, text):
        self.txtF_passwd.text = f'{text}'
        self.controller.set_signup_passwd(text)

    def set_view_signup_confpasswd(self, instance, text):
        self.txtF_confpasswd.text = f'{text}'
        self.controller.set_signup_confpasswd(text)

    def set_view_signup_nombre(self, instance, text):
        self.txtF_nombre.text = f'{text}'
        self.controller.set_signup_nombre(text)

    def set_view_signup_apellido(self, instance, text):
        self.txtF_apellidos.text = f'{text}'
        self.controller.set_signup_apellido(text)

    def return_model(self):
        return self.model

    def return_controller(self):
        return self.controller

    def on_SignUpAttempt (self, event):
        validado = self.controller.signup_validaciones()
        if validado:
            print(' ===== VALIDADO ===== ')
            self.controller.signup_to_modelo()
            self.controller.push_upload_cliente()
            MDSnackbar(
                MDLabel(text="Datos subidos satisfactoriamente"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()
            self.closeSignUp()
        else:
            MDSnackbar(
                MDLabel(text="Error. Asegúrese de que los datos están correctos y pruebe de nuevo"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()

    def closeSignUp4button (self, obj):
        self.closeSignUp()

    def closeSignUp(self):
        self.dismiss()

class LoginUI (MDFloatLayout):
    """
    UI del Login
    """
    controller = ObjectProperty
    model = ObjectProperty

    dialog_login_success = None
    def __init__(self, model, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model = model

        self.grid = MDGridLayout()
        self.cols = 1
        self.add_widget(self.grid)

        self.central_card = MDCard()
        self.central_card.size_hint = 0.5, 0.65
        self.central_card.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.central_card.elevation = 3
        self.central_card.padding = dp(25)
        self.central_card.spacing = dp(20)
        self.central_card.orientation = 'vertical'
        self.add_widget(self.central_card)

        self.txt_login = MDLabel()
        self.txt_login.text = "Bienvenido al Login de Camisetas Custom!"
        self.txt_login.font_size = dp(20)
        self.txt_login.halign = 'center'
        self.txt_login.size_hint_y = 0.2
        self.txt_login.padding_y = dp(10)
        self.central_card.add_widget(self.txt_login)

        self.txtF_email = MDTextField(hint_text = "Email",
                                      text = '',
                                      mode = "rectangle",
                                      size_hint_x = .9,
                                      size_hint_y = None,
                                      height = dp(37.5),
                                      font_size = dp(17.5),
                                      padding_y = dp(10),
                                      pos_hint = {"center_x": 0.5, "center_y": 0.5}
                                      )
        self.txtF_email.bind(text = self.set_view_login_email)

        self.txtF_passwd = MDTextField(hint_text = "Contraseña",
                                       text = '',
                                       mode = "rectangle",
                                       size_hint_x = .9,
                                       size_hint_y = None,
                                       height = dp(37.5),
                                       font_size = dp(17.5),
                                       pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                       password = True
                                       )
        self.txtF_passwd.bind(text=self.set_view_login_passwd)

        self.central_card.add_widget(self.txtF_email)
        self.central_card.add_widget(self.txtF_passwd)

        self.buttonBox = MDBoxLayout()
        self.buttonBox.orientation = "vertical"
        self.buttonBox.pos_hint = {'center_x': .5, 'center_y': .5}
        self.buttonBox.haling = 'center'
        self.buttonBox.padding = dp(15)
        self.buttonBox.padding_y = dp(15)
        self.buttonBox.spacing = dp(10)
        self.central_card.add_widget(self.buttonBox)

        self.buttonGrid = MDGridLayout()
        self.buttonGrid.cols = 3

        self.b_logIn = MDRectangleFlatButton(text="Entrar",
                                             font_size="20dp",
                                             size=("200dp", "50dp"),
                                             size_hint=(None, None),
                                             pos_hint={'center_x': .5, 'center_y': .5},
                                             on_press=self.on_logInAttempt)
        self.b_clear = MDTextButton(text="[b][u]Borrar campos[/u][/b]",
                                         markup = True,
                                         font_size="15dp",
                                         size=("200dp", "50dp"),
                                         size_hint=(None, None),
                                         pos_hint={'center_x': .5, 'center_y': .5},
                                         color= [74, 136, 237, 1],
                                         on_press=self.clearFields)
        self.b_signUp = MDRectangleFlatButton(text="Registrarse",
                                             font_size="20dp",
                                             size=("200dp", "50dp"),
                                             size_hint=(None, None),
                                             pos_hint={'center_x': .5, 'center_y': .5},
                                             on_press=self.signup_popup_open)
        self.bufferWidget = MDWidget()
        self.bufferWidget.size_hint = .6, .1

        self.buttonBox.add_widget(self.b_clear)

        self.buttonBox.add_widget(self.buttonGrid)
        self.buttonGrid.add_widget(self.b_signUp)
        self.buttonGrid.add_widget(self.bufferWidget)
        self.buttonGrid.add_widget(self.b_logIn)

    def clearFields(self):
        self.txtF_email.text = ''
        self.controller.login_email('')
        self.txtF_passwd.text = ''
        self.controller.login_passwd('')

    def set_view_login_email(self, instance, text):
        self.txtF_email.text = f'{text}'
        self.controller.set_login_email(text)
    def set_view_login_passwd(self, instance, text):
        self.txtF_passwd.text = f'{text}'
        self.controller.set_login_passwd(text)
    def set_view_login_confpasswd(self, instance, text):
        self.txtF_confpasswd.text = f'{text}'
        self.controller.set_login_confpasswd(text)

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller

    def signup_popup_open(self, event):
        Factory.SignupUI(controller=self.return_controller(), model=self.return_model()).open()

    def on_logInAttempt (self, event):
        validado = self.controller.login_validaciones()
        doc_cli =  self.controller.cli_get_data()

        if validado:
            print(' ===== VALIDADO ===== ')
            self.controller.set_cod_cli()
            self.controller.set_last_con_cli()
            # self.controller.get_main_screen()
            LoggedinStatus.set_logged_in(True)
            self.dialog_login_success = MDDialog(
                title=f"Bienvenido {doc_cli['c_nombre']} {doc_cli['c_apellido']}",
                text=f"Con el código de cliente {doc_cli['a_cod_cli']}. ¿Es usted este usuario?",
                buttons=[
                    MDFlatButton(
                        text='Cancelar',
                        on_press=self.closeDialog,
                    ),
                    MDFlatButton(
                        text='Confirmar',
                        on_press=self.closeLogin,
                    ),
                ],
            )
            self.dialog_login_success.open()
        else:
            MDSnackbar(
                MDLabel(text="Credenciales incorrectas. Asegúrese de que los datos están correctos y pruebe de nuevo"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()

    def closeDialog(self, obj):
        self.dialog_login_success.dismiss()

    def closeLogin(self, obj):
        MDApp.get_running_app().stop()

class LoginScreen(MDScreen, Widget): # Ventana Principal
    """
    Pantalla de login
    """
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, model, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model

        self.wrap = LoginUI(self.model, self.controller)
        self.add_widget(self.wrap)

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller