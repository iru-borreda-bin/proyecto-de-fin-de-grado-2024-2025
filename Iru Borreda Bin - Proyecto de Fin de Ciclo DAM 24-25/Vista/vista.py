# Python 3.13.3
# kivy 2.3.1
# kivymd 1.2.0

from Modelo.ddbb import Firebase

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.widget import MDWidget
from kivymd.uix.list.list import BaseListItem, TwoLineListItem
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.tab import MDTabsBase
# from kivymd.uix.spinner import MDSpinner
from kivymd.uix.toolbar import MDTopAppBar

from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.metrics import dp

glob_cod_ped = 0
def set_glob_cod_ped (cod_ped_new):
    globals()['glob_cod_ped'] = int(cod_ped_new)
glob_loaded_cli = []
def set_glob_loaded_cli (new_cli):
    globals()['glob_loaded_cli'] = new_cli

class ModifyPopup(Popup, MDWidget):
    model = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.setDocData()

    def get_tamanos(self):
        tamanos = ['S', 'M', 'L', 'X', 'XL', 'XXL']
        return tamanos

    def get_disenos(self):
        disenos = ['Camuflaje', 'Cuadrados', 'Rayas', 'Polka']
        return disenos

    def get_colores(self):
        colores = ['Blanco', 'Negro', 'Rojo', 'Azul', 'Verde']
        return colores

    def get_posiciones(self):
        posiciones = ['Superior Izquierda', 'Superior Centro', 'Superior Derecha',
                   'Central Izquierda', 'Central Centro', 'Central Derecha',
                   'Inferior Izquierda', 'Inferior Centro', 'Inferior Derecha']
        return posiciones

    def get_txt_tamanos(self):
        tamanos = ['9', '11', '15', '20', '24', '26']
        return tamanos

    def get_txt_tipo(self):
        tipos = ['Arial', 'Impact', 'Comic Sans', 'Calibri']
        return tipos

    def get_logos(self):
        tipos = ['Logo1', 'Logo2', 'Logo3', 'Logo4']
        return tipos

    def get_logos(self):
        tipos = ['Logo1', 'Logo2', 'Logo3', 'Logo4']
        return tipos

    def get_logo_tamanos(self):
        tamanos = ['Pequeño', 'Medio', 'Grande', 'Extra Grande']
        return tamanos

    # Recoge los datos
    def set_tam(self, value):
        self.ids.spin_tam.text = f'{value}'
        self.controller.set_shirt_tam(value)
    def set_des(self, value):
        self.ids.spin_des.text = f'{value}'
        self.controller.set_shirt_des(value)
    def set_col_base(self, value):
        self.ids.spin_col_base.text = f'{value}'
        self.controller.set_shirt_col_base(value)
    def set_col_des(self, value):
        self.ids.spin_col_des.text = f'{value}'
        self.controller.set_shirt_col_des(value)

    def set_txt_cont(self, value):
        self.ids.txtf_txt_cont.text = f'{value}'
        self.controller.set_shirt_txt_cont(value)
    def set_txt_pos(self, value):
        self.ids.spin_txt_pos.text = f'{value}'
        self.controller.set_shirt_txt_pos(value)
    def set_txt_tam(self, value):
        self.ids.spin_txt_tam.text = f'{value}'
        self.controller.set_shirt_txt_tam(value)
    def set_txt_col(self, value):
        self.ids.spin_txt_col.text = f'{value}'
        self.controller.set_shirt_txt_col(value)

    def set_txt_tip(self, value):
        self.ids.spin_txt_tipo.text = f'{value}'
        self.controller.set_shirt_txt_tip(value)
    def set_logo(self, value):
        self.ids.spin_logo.text = f'{value}'
        self.controller.set_shirt_logo(value)
    def set_logo_pos(self, value):
        self.ids.spin_logo_pos.text = f'{value}'
        self.controller.set_shirt_logo_pos(value)
    def set_logo_tam(self, value):
        self.ids.spin_logo_tam.text = f'{value}'
        self.controller.set_shirt_logo_tam(value)
    def set_logo_elev(self, value):
        self.ids.spin_logo_elev.text = f'{value}'
        self.controller.set_shirt_logo_elev(value)

    def on_chk_des(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.spin_des.disabled = True
            self.ids.spin_col_des.disabled = True

            self.controller.set_shirt_des('====')
            self.controller.set_shirt_col_des('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.spin_des.disabled = False
            self.ids.spin_col_des.disabled = False

            self.controller.set_shirt_des('')
            self.controller.set_shirt_col_des('')
            # print(f'{checkbox.state}')

    def on_chk_txt(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.txtf_txt_cont.disabled = True
            self.ids.spin_txt_pos.disabled = True
            self.ids.spin_txt_tam.disabled = True
            self.ids.spin_txt_col.disabled = True
            self.ids.spin_txt_tipo.disabled = True

            self.controller.set_shirt_txt_cont('====')
            self.controller.set_shirt_txt_pos('====')
            self.controller.set_shirt_txt_tam('====')
            self.controller.set_shirt_txt_col('====')
            self.controller.set_shirt_txt_tip('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.txtf_txt_cont.disabled = False
            self.ids.spin_txt_pos.disabled = False
            self.ids.spin_txt_tam.disabled = False
            self.ids.spin_txt_col.disabled = False
            self.ids.spin_txt_tipo.disabled = False

            self.controller.set_shirt_txt_cont('')
            self.controller.set_shirt_txt_pos('')
            self.controller.set_shirt_txt_tam('')
            self.controller.set_shirt_txt_col('')
            self.controller.set_shirt_txt_tip('')
            # print(f'{checkbox.state}')

    def on_chk_logo(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.spin_logo.disabled = True
            self.ids.spin_logo_pos.disabled = True
            self.ids.spin_logo_tam.disabled = True
            self.ids.spin_logo_elev.disabled = True

            self.controller.set_shirt_txt_cont('====')
            self.controller.set_shirt_txt_pos('====')
            self.controller.set_shirt_txt_tam('====')
            self.controller.set_shirt_txt_col('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.spin_logo.disabled = False
            self.ids.spin_logo_pos.disabled = False
            self.ids.spin_logo_tam.disabled = False
            self.ids.spin_logo_elev.disabled = False

            self.controller.set_shirt_logo('')
            self.controller.set_shirt_logo_pos('')
            self.controller.set_shirt_logo_tam('')
            self.controller.set_shirt_logo_elev('')
            # print(f'{checkbox.state}')

    def on_conf_diseno(self):
        validado = self.controller.ped_validaciones()
        if validado:
            self.controller.ped_push_to_modelo()
            self.controller.push_update_shirt(glob_cod_ped)
            MDSnackbar(
                MDLabel(text="Recuerde refrescar la tabla para ver los nuevos datos"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()
            self.dismiss()
        else:
            MDSnackbar(
                MDLabel(text="Asgúrese de que todos los campos habilitados hallán sido llenados"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()

    # Pone los datos del pedido original
    def setDocData(self):
        doc = self.controller.ped_get_data(glob_cod_ped)

        self.set_tam(f'{doc['b_tamano']}')
        self.set_des(f'{doc['b_diseno']}')
        self.set_col_base(f'{doc['b_col_base']}')
        self.set_col_des(f'{doc['b_col_des']}')
        self.set_txt_cont(f'{doc['c_txt_cont']}')
        self.set_txt_pos(f'{doc['c_txt_pos']}')
        self.set_txt_tam(f'{doc['c_txt_tam']}')
        self.set_txt_col(f'{doc['c_txt_col']}')
        self.set_txt_tip(f'{doc['c_txt_tip']}')
        self.set_logo(f'{doc['d_logo']}')
        self.set_logo_pos(f'{doc['d_logo_pos']}')
        self.set_logo_tam(f'{doc['d_logo_tam']}')
        self.set_logo_elev(f'{doc['d_logo_elev']}')

class InfoPopup(Popup, MDWidget):
    model = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.displayData()

    def displayData(self):
        doc = self.controller.ped_get_data(glob_cod_ped)

        self.ids.txtinfo_pedido_docid.text = f'[cod-cli]_{doc['a_cod_ped']}'
        self.ids.txtinfo_pedido_ped_cod.text = f'{doc['a_cod_ped']}'
        self.ids.txtinfo_pedido_ped_cli.text = '[a_cod-cli]' #f'{doc['cod_cli']}'
        self.ids.txtinfo_pedido_ped_fecha.text = f'{doc['a_timestamp']}'
        self.ids.txtinfo_pedido_ped_fecha_act.text = f'{doc['a_timestamp_last_update']}'
        self.ids.txtinfo_pedido_estado.text = f'{doc['a_state']}'

        self.ids.txtinfo_shirt_tam.text = f'{doc['b_tamano']}'
        self.ids.txtinfo_shirt_col_base.text = f'{doc['b_col_base']}'
        self.ids.txtinfo_shirt_des.text = f'{doc['b_diseno']}'
        self.ids.txtinfo_shirt_col_des.text = f'{doc['b_col_des']}'

        self.ids.txtinfo_shirt_txt_cont.text = f'{doc['c_txt_cont']}'
        self.ids.txtinfo_shirt_txt_col.text = f'{doc['c_txt_col']}'
        self.ids.txtinfo_shirt_txt_pos.text = f'{doc['c_txt_pos']}'
        self.ids.txtinfo_shirt_txt_tam.text = f'{doc['c_txt_tam']}'
        self.ids.txtinfo_shirt_txt_tip.text = f'{doc['c_txt_tip']}'

        self.ids.txtinfo_shirt_logo.text = f'{doc['d_logo']}'
        self.ids.txtinfo_shirt_logo_pos.text = f'{doc['d_logo_pos']}'
        self.ids.txtinfo_shirt_logo_tam.text = f'{doc['d_logo_tam']}'
        self.ids.txtinfo_shirt_txt_elev.text = f'{doc['d_logo_elev']}'

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller

    # def openModifyPopup(self):
    #     self.dismiss()
    #     Factory.ModifyPopup(controller=self.return_controller(), model=self.return_model()).open()

class TabOpcion(MDFloatLayout, MDTabsBase):
    """Implementa contenido para cada tab"""

class EditorPopup(Popup, MDWidget):
    """
    Formulario de camisetas
    """
    model = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, model, controller,  **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller

# Formulario
    # Recoge la lista para los Spinners
    def get_tamanos(self):
        tamanos = ['S', 'M', 'L', 'X', 'XL', 'XXL']
        return tamanos
    def get_disenos(self):
        disenos = ['Camuflaje', 'Cuadrados', 'Rayas', 'Polka']
        return disenos
    def get_colores(self):
        colores = ['Blanco', 'Negro', 'Rojo', 'Azul', 'Verde']
        return colores
    def get_posiciones(self):
        posiciones = ['Superior Izquierda', 'Superior Centro', 'Superior Derecha',
                   'Central Izquierda', 'Central Centro', 'Central Derecha',
                   'Inferior Izquierda', 'Inferior Centro', 'Inferior Derecha']
        return posiciones
    def get_txt_tamanos(self):
        tamanos = ['9', '11', '15', '20', '24', '26']
        return tamanos
    def get_txt_tipo(self):
        tipos = ['Arial', 'Impact', 'Comic Sans', 'Calibri']
        return tipos
    def get_logos(self):
        tipos = ['Logo1', 'Logo2', 'Logo3', 'Logo4']
        return tipos
    def get_logos(self):
        tipos = ['Logo1', 'Logo2', 'Logo3', 'Logo4']
        return tipos
    def get_logo_tamanos(self):
        tamanos = ['Pequeño', 'Medio', 'Grande', 'Extra Grande']
        return tamanos

    # Recoge los datos
    def set_tam(self, value):
        self.ids.spin_tam.text = f'{value}'
        self.controller.set_shirt_tam(value)
    def set_des(self, value):
        self.ids.spin_des.text = f'{value}'
        self.controller.set_shirt_des(value)
    def set_col_base(self, value):
        self.ids.spin_col_base.text = f'{value}'
        self.controller.set_shirt_col_base(value)
    def set_col_des(self, value):
        self.ids.spin_col_des.text = f'{value}'
        self.controller.set_shirt_col_des(value)

    def set_txt_cont(self, value):
        self.ids.txtf_txt_cont.text = f'{value}'
        self.controller.set_shirt_txt_cont(value)
    def set_txt_pos(self, value):
        self.ids.spin_txt_pos.text = f'{value}'
        self.controller.set_shirt_txt_pos(value)
    def set_txt_tam(self, value):
        self.ids.spin_txt_tam.text = f'{value}'
        self.controller.set_shirt_txt_tam(value)
    def set_txt_col(self, value):
        self.ids.spin_txt_col.text = f'{value}'
        self.controller.set_shirt_txt_col(value)
    def set_txt_tip(self, value):
        self.ids.spin_txt_tipo.text = f'{value}'
        self.controller.set_shirt_txt_tip(value)

    def set_logo(self, value):
        self.ids.spin_logo.text = f'{value}'
        self.controller.set_shirt_logo(value)
    def set_logo_pos(self, value):
        self.ids.spin_logo_pos.text = f'{value}'
        self.controller.set_shirt_logo_pos(value)
    def set_logo_tam(self, value):
        self.ids.spin_logo_tam.text = f'{value}'
        self.controller.set_shirt_logo_tam(value)
    def set_logo_elev(self, value):
        self.ids.spin_logo_elev.text = f'{value}'
        self.controller.set_shirt_logo_elev(value)

    def on_chk_des(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.spin_des.disabled = True
            self.ids.spin_col_des.disabled = True

            self.controller.set_shirt_des('====')
            self.controller.set_shirt_col_des('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.spin_des.disabled = False
            self.ids.spin_col_des.disabled = False

            self.controller.set_shirt_des('')
            self.controller.set_shirt_col_des('')
            # print(f'{checkbox.state}')

    def on_chk_txt(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.txtf_txt_cont.disabled = True
            self.ids.spin_txt_pos.disabled = True
            self.ids.spin_txt_tam.disabled = True
            self.ids.spin_txt_col.disabled = True
            self.ids.spin_txt_tipo.disabled = True

            self.controller.set_shirt_txt_cont('====')
            self.controller.set_shirt_txt_pos('====')
            self.controller.set_shirt_txt_tam('====')
            self.controller.set_shirt_txt_col('====')
            self.controller.set_shirt_txt_tip('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.txtf_txt_cont.disabled = False
            self.ids.spin_txt_pos.disabled = False
            self.ids.spin_txt_tam.disabled = False
            self.ids.spin_txt_col.disabled = False
            self.ids.spin_txt_tipo.disabled = False

            self.controller.set_shirt_txt_cont('')
            self.controller.set_shirt_txt_pos('')
            self.controller.set_shirt_txt_tam('')
            self.controller.set_shirt_txt_col('')
            self.controller.set_shirt_txt_tip('')
            # print(f'{checkbox.state}')

    def on_chk_logo(self, checkbox):
        if checkbox.state == 'normal':
            self.ids.spin_logo.disabled = True
            self.ids.spin_logo_pos.disabled = True
            self.ids.spin_logo_tam.disabled = True
            self.ids.spin_logo_elev.disabled = True

            self.controller.set_shirt_txt_cont('====')
            self.controller.set_shirt_txt_pos('====')
            self.controller.set_shirt_txt_tam('====')
            self.controller.set_shirt_txt_col('====')
            # print(f'{checkbox.state}')
        else:
            self.ids.spin_logo.disabled = False
            self.ids.spin_logo_pos.disabled = False
            self.ids.spin_logo_tam.disabled = False
            self.ids.spin_logo_elev.disabled = False

            self.controller.set_shirt_logo('')
            self.controller.set_shirt_logo_pos('')
            self.controller.set_shirt_logo_tam('')
            self.controller.set_shirt_logo_elev('')
            # print(f'{checkbox.state}')

    def on_conf_diseno(self):
        validado = self.controller.ped_validaciones()
        if validado:
            self.controller.ped_push_to_modelo()
            self.controller.push_upload_shirt()
            MDSnackbar(
                MDLabel(text="Recuerde refrescar la tabla para ver los nuevos datos"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()
            self.dismiss()
        else:
            MDSnackbar(
                MDLabel(text="Asgúrese de que todos los campos habilitados hallán sido llenados"),
                snackbar_x="10dp",
                snackbar_y="10dp",
                pos_hint={"center_x": 0.5, "y": 0},
                size_hint_x=0.7,
            ).open()

class DataTable(MDGridLayout):
    controller = ObjectProperty()
    model = ObjectProperty()

    dialog_main = None
    dialog_del_conf = None
    def __init__(self, model, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.doc_ref = self.model.ped_get_items_dbbb()

        self.cols = 1

        self.table = MDDataTable(pos_hint={'center_y': 0.5, 'center_x': 0.5},
                                 size_hint=(1.75, 0.8),
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Documento", dp(30)),
                                     ("Pedido", dp(15)),
                                     ("Cliente", dp(15)),
                                     ("Estado", dp(20)),
                                     ("Fecha de subida", dp(35)),
                                     ("Última actualización", dp(35)),
                                     ("Tamaño", dp(20)),
                                     ("Diseño", dp(20)),
                                     ("Colores", dp(25)),
                                     ("Texto", dp(25)),
                                     ("Logo", dp(15))],
                                 row_data=self.add_table_data(self.doc_ref),
                                 rows_num=10,
                                 sorted_on="Código de Pedido")
        self.table.bind(on_row_press=self.on_row_press)
        self.table.bind(on_row_press= self.shirtActions)
        self.add_widget(self.table)

        MDSnackbar(
            MDLabel(
                text=f"Cargándo los datos de admin-{glob_loaded_cli['a_cod_cli']}. Bienvenido {glob_loaded_cli['c_nombre']} {glob_loaded_cli['c_apellido']}"),
            snackbar_x="10dp",
            snackbar_y="10dp",
            pos_hint={"center_x": 0.5, "y": 0.1},
            size_hint_x=0.7,
        ).open()

    def add_table_data(self, docs):
        table_list = []
        doc = []
        for item in docs:
            doc = docs[item]
            fecha_ped = doc['a_timestamp'].strftime("%Y/%m/%d %H:%M")
            fecha_act = doc['a_timestamp_last_update'].strftime("%Y/%m/%d %H:%M")
            doc['a_timestamp'] = fecha_ped
            doc['a_timestamp_last_update'] = fecha_act

            datos_list = []
            datos_list.append(f'[cod-cli]_{doc['a_cod_ped']}')
            datos_list.append(doc['a_cod_ped'])
            datos_list.append('[cod_cli]')
            datos_list.append(doc['a_state'])
            datos_list.append(doc['a_timestamp'])
            datos_list.append(doc['a_timestamp_last_update'])

            datos_list.append(doc['b_tamano'])
            datos_list.append(doc['b_diseno'])
            datos_list.append(f'Base: {doc['b_col_base']}\n Diseño: {doc["b_col_des"]}')
            datos_list.append(doc['c_txt_cont'])
            datos_list.append(doc['d_logo'])
            table_list.append(datos_list)
        return table_list

    # Debido a que DataTable no es un elemento dinámico, cada vez que se añade o se borra un dato hay que regenerar la tabla
    def regen_table(self):
        self.remove_widget(self.table)
        docs = self.model.ped_get_items_dbbb()
        self.table = MDDataTable(pos_hint={'center_y': 0.5, 'center_x': 0.5},
                                 size_hint=(1.75, 0.8),
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Documento", dp(30)),
                                     ("Pedido", dp(15)),
                                     ("Cliente", dp(15)),
                                     ("Estado", dp(20)),
                                     ("Fecha de subida", dp(35)),
                                     ("Última actualización", dp(35)),
                                     ("Tamaño", dp(20)),
                                     ("Diseño", dp(20)),
                                     ("Colores", dp(25)),
                                     ("Texto", dp(25)),
                                     ("Logo", dp(15))],
                                 row_data=self.add_table_data(docs),
                                 rows_num=10,
                                 sorted_on="Código de Pedido"
                                 )
        self.table.bind(on_row_press=self.on_row_press)
        self.table.bind(on_row_press=self.shirtActions)
        self.add_widget(self.table)

        # for doc in docs:
        #     print (f'Doc: {doc}')
        #     for field in docs[doc]:
        #         print (f'---{field} : {docs[doc][field]}')
        #     print("===========")
        #     print(" ")
        # print("Tabla refrescada")

    # Para saber qué row está elegido y de manera que solo haya un row elegida en cada momento
    def on_row_press(self, instance_table, instance_row):
        index = instance_row.index
        cols_num = len(instance_table.column_data)
        row_num = int(index / cols_num)
        col_num = index % cols_num
        cell_row = instance_table.table_data.view_adapter.get_visible_view(row_num * cols_num)
        if cell_row.ids.check.state == 'normal':
            instance_table.table_data.select_all('normal')
            cell_row.ids.check.state = 'down'
        else:
            cell_row.ids.check.state = 'normal'
        instance_table.table_data.on_mouse_select(instance_row)

    # Dialog de acciones con los datos
    def shirtActions(self, instance_table, instance_row):
        num_row = int(instance_row.index / len(instance_table.column_data))
        row_data = instance_table.row_data[num_row]
        set_glob_cod_ped(row_data[1])
        # if not self.dialog:
        self.dialog_main = MDDialog(
            title=f"¿Qué quiere hacer con el pedido {glob_cod_ped}",
            buttons=[
                MDFlatButton(
                    text='Cancelar',
                    on_press=self.closeDialog,
                ),
                MDFlatButton(
                    text='Examinar',
                    on_press=self.openInfoPopup,
                ),
                MDFlatButton(
                    text='Editar',
                    on_press=self.openModifyPopup,
                ),
                MDFlatButton(
                    text='Borrar',
                    on_press=self.openDeleteDialog,
                ),
            ],
        )
        self.dialog_main.open()

    def openInfoPopup (self, obj):
        self.dialog_main.dismiss()
        Factory.InfoPopup(controller=self.return_controller(), model=self.return_model()).open()

    def openModifyPopup(self, obj):
        self.dialog_main.dismiss()
        Factory.ModifyPopup(controller=self.return_controller(), model=self.return_model()).open()

    def openDeleteDialog(self, obj):
        self.dialog_main.dismiss()
        self.dialog_del_conf = MDDialog(
            title=f"¿Está seguro/a que quiere borrar el pedido {glob_cod_ped}?",
            text="Este proceso es irreversible",
            buttons=[
                MDFlatButton(
                    text='Cancelar',
                    on_press=self.exitDeleteConf,
                ),
                MDFlatButton(
                    text='Confirmar',
                    on_press=self.deleteConf,
                ),
            ],
        )
        self.dialog_del_conf.open()

    def deleteConf(self, obj):
        Firebase.ped_delete_item(glob_cod_ped)
        self.regen_table()
        self.dialog_del_conf.dismiss()

    def exitDeleteConf(self, obj):
        self.dialog_del_conf.dismiss()

    def closeDialog(self, obj):
        self.dialog_main.dismiss()

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller

    # [OLD] funciones de la tabla
    # def add_row(self, row):
    #     # last_num_row = int(self.table.row_data[0][0])
    #     # print(f'{last_num_row}')
    #     # self.table.add_row((str(last_num_row + 1), row['cod_ped'],
    #     #                                             row['tamano'],
    #     #                                             row['diseno'],
    #     #                                             row['txt_cont'],
    #     #                                             row['logo']))
    #     self.regen_table()
    # def update_row(self, row) -> None:
    #     self.table.update_row('placeholder')
    #
    # def delete_row(self, codigo) -> None:
    #     self.table.remove_row('placeholder')


# class ItemConfirm:
#     pass


class MainMenuBox(MDBoxLayout): # Elementos del Menú principal
    controller = ObjectProperty()
    model = ObjectProperty()

    dialog_cli_info = None
    dialog_exit = None
    dialog_cli_list = None
    def __init__(self, model, controller, **kwargs):
        super(MainMenuBox, self).__init__(**kwargs)
        self.controller = controller
        self.model = model

        self.orientation = 'vertical'
        # self.active_spinner = False

        self.selected_cli_cod = 0

        self.size_hint = (1, 1)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.grid = MDGridLayout()
        self.grid.cols = 2

        self.table = DataTable(model=self.model, controller=self.controller)
        self.table.size_hint = (1.75, 0.8)

        self.buttonGrid = MDGridLayout()

        self.buttonGrid.cols = 1
        self.buttonGrid.spacing = "15 dp"
        self.buttonGrid.padding = "10 dp", "10 dp", "10 dp", "10 dp"
        self.buttonGrid.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # self.loading_Spinner = MDSpinner()
        # self.loading_Spinner.size = ("15dp", "15dp")
        # self.loading_Spinner.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        # self.loading_Spinner.line_width = "3.5dp"
        # self.loading_Spinner.active = True if self.active_spinner else False
        # self.buttonGrid.add_widget(self.loading_Spinner)

        self.b_refreshTable = MDRectangleFlatButton(text="Refrescar Tabla",
                                                    font_size="25dp",
                                                    size=("250dp", "75dp"),
                                                    size_hint=(None, None),
                                                    pos_hint={'center_x': .5, 'center_y': .5},
                                                    on_press=self.progRegen)
        self.b_createShirt = MDRectangleFlatButton(text="Crear una Camiseta",
                                                   font_size="25dp",
                                                   size=("250dp", "75dp"),
                                                   size_hint=(None, None),
                                                   pos_hint={'center_x': .5, 'center_y': .5},
                                                   on_press=self.createShirt)
        self.b_showAccInfo = MDRectangleFlatButton(text="Enseñar info de cuenta",
                                                   font_size="25dp",
                                                   size=("250dp", "75dp"),
                                                   size_hint=(None, None),
                                                   pos_hint={'x': .5, 'center_y': .5},
                                                   on_press=self.open_info_dialog)
        self.b_closeApp = MDRectangleFlatButton(text="Salir",
                                                   font_size="25dp",
                                                   size=("250dp", "75dp"),
                                                   size_hint=(None, None),
                                                   pos_hint={'center_x': .5, 'center_y': .5},
                                                   on_press=self.open_exit_dialog)


        # self.load_context_menu()
        self.topbar = MDTopAppBar()
        self.topbar.title = "Menú Principal"
        self.topbar.elevation = "0"
        self.topbar.md_bg_color = "#4956cc"
        # self.topbar.left_action_items = [["menu", lambda x: self.callback(x)]]

        # self.sideButtons = MDBoxLayout()
        # self.sideButtons.orientation = 'vertical'

        self.add_widget(self.topbar)
        self.add_widget(self.grid)
        self.grid.add_widget(self.table)
        self.buttonGrid.add_widget(self.b_refreshTable)
        self.buttonGrid.add_widget(self.b_createShirt)
        self.buttonGrid.add_widget(self.b_showAccInfo)
        self.buttonGrid.add_widget(self.b_closeApp)
        # self.load_debugButtons()

        self.grid.add_widget(self.buttonGrid)


    # def load_debugButtons(self):
    #     self.debugButtons = MDGridLayout()
    #     self.debugButtons.cols = 1
    #     self.buttonGrid.add_widget(self.debugButtons)
    #
    #     self.txt_debugheader = MDLabel(
    #         text="Debug/Admin",
    #         text_size=self.size,
    #         font_size=dp(20),
    #         halign='left',
    #         size_hint_y=0.2,
    #         padding_y=dp(10)
    #     )
    #     # self.emptyWid = MDWidget()
    #     self.b_showAccInfoOther = MDRectangleFlatButton(text="Mirar info otro",
    #                                                font_size="25dp",
    #                                                size=("250dp", "75dp"),
    #                                                size_hint=(None, None),
    #                                                pos_hint={'center_x': .5, 'center_y': .5},
    #                                                on_press= self.mirar_info_otra_cuenta())
    #     self.b_changeAcc = MDRectangleFlatButton(text="Cambiar a otra cuenta",
    #                                                font_size="25dp",
    #                                                size=("250dp", "75dp"),
    #                                                size_hint=(None, None),
    #                                                pos_hint={'center_x': .5, 'center_y': .5},
    #                                                 )#on_press=self.open_exit_dialog)
    #     self.b_borrarCli = MDRectangleFlatButton(text="Borrar un cliente",
    #                                                font_size="25dp",
    #                                                size=("250dp", "75dp"),
    #                                                size_hint=(None, None),
    #                                                pos_hint={'center_x': .5, 'center_y': .5},
    #                                              )#on_press=self.open_exit_dialog)
    #     self.b_deletePedidos = MDRectangleFlatButton(text="Limpiar datos",
    #                                                font_size="25dp",
    #                                                size=("250dp", "75dp"),
    #                                                size_hint=(None, None),
    #                                                pos_hint={'center_x': .5, 'center_y': .5},
    #                                                  )#on_press=self.open_exit_dialog)
    #
    #     self.debugButtons.add_widget(self.txt_debugheader)
    #     # self.debugButtons.add_widget(self.emptyWid)
    #     self.debugButtons.add_widget(self.b_showAccInfoOther)
    #     self.debugButtons.add_widget(self.b_changeAcc)
    #     self.debugButtons.add_widget(self.b_borrarCli)
    #     self.debugButtons.add_widget(self.b_deletePedidos)

    def gen_menu_admin(self):
        pass

    def gen_menu_cliente(self):
        pass

    # Abre EditorPopup
    def createShirt(self, event):
        Factory.EditorPopup(controller=self.return_controller(), model=self.return_model()).open()

    #Regenera la tabla
    def progRegen(self,event):
        # self.active_spinner = True
        # print("progBar active")
        self.table.regen_table()
        # self.active_spinner = False
        # print("progBar inactive")

    def set_selected_cli_cod (self, cli_cod):
        self.selected_cli_cod = cli_cod

    # def open_cli_list_dialog(self):
    #     cli_docs = self.model.cli_get_items_dbbb()
    #     doc = []
    #
    #     print("estoy abriendo la lista")
    #     print(f"{cli_docs}")
    #
    #     self.dialog_cli_list = MDDialog(
    #         title="Lista de usuarios",
    #         type="custom",
    #         items=[
    #             # {
    #             #     # ItemConfirm(text=f"{doc}", secondary_text=f"email: {cli_docs[doc]['b_email']}",
    #             #     #             on_release=lambda x=cli_docs[doc]['a_cod_cli']: self.set_selected_cli_cod(x))
    #             #     "text" : f"{doc}",
    #             #     "viewclass" : "TwoLineListItem",
    #             #     "secondary_text" : f"email: {cli_docs[doc]['b_email']}",
    #             #     "on_release" : lambda x=cli_docs[doc]['a_cod_cli']: self.set_selected_cli_cod(x)
    #             # } for doc in cli_docs
    #             ItemConfirm(text="Cliente 1", secondary_text="email: cliente1@email.com",
    #                         on_release=lambda x=1: self.set_selected_cli_cod(x)),
    #             ItemConfirm(text="Cliente 2", secondary_text="email: cliente2@email.com",
    #                         on_release=lambda x=2: self.set_selected_cli_cod(x))
    #         ],
    #         buttons=[
    #             MDFlatButton(
    #                 text='Cancelar',
    #                 on_press=self.closeListDialogCancel,
    #             ),
    #             MDFlatButton(
    #                 text='Confirmar',
    #                 on_press=self.closeListDialog,
    #             )
    #         ]
    #     )
    #     self.dialog_cli_list.open()

    # def mirar_info_otra_cuenta(self, event):
    #     pass

    def open_info_dialog(self, event):
        self.info_dialog(glob_loaded_cli)

    def info_dialog(self,cli_info):
        self.dialog_cli_info = MDDialog(
            title=f"Información del usuario {cli_info['a_cod_cli']}",
            text= f"Código: {cli_info['a_cod_cli']} \n"
                  f"Nombre y Apellido(s): {cli_info['c_nombre']} {cli_info['c_apellido']} \n"
                  f"Email: {cli_info['b_email']} \n"
                  f"Creado en: {cli_info['a_timestamp']} \n"
                  f"Última Conexión: {cli_info['a_timestamp']}",
            buttons=[
                MDFlatButton(
                    text='Cerrar',
                    on_press=self.closeInfoDialog,
                )
            ],
        )
        self.dialog_cli_info.open()

    def open_exit_dialog(self,event):
        self.dialog_exit = MDDialog(
            title=f"¿Quiere salir de la aplicación?",
            buttons=[
                MDFlatButton(
                    text='Salir',
                    on_press=self.closeApp,
                ),
                MDFlatButton(
                    text='Cancelar',
                    on_press=self.closeExitDialog,
                )
            ],
        )
        self.dialog_exit.open()

    # def menu_callback(self):
    #     pass
    #
    # def gen_cliUI(self):
    #     pass

    def closeInfoDialog(self, obj):
        self.dialog_cli_info.dismiss()

    def closeExitDialog(self, obj):
        self.dialog_exit.dismiss()

    # def closeListDialogCancel(self, obj):
    #     self.set_selected_cli_cod(0)
    #     self.dialog_cli_list.dismiss()
    #
    # def closeListDialog(self, obj):
    #     self.dialog_cli_list.dismiss()

    def closeApp(self,event):
        MDApp.get_running_app().stop()

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller

class ItemConfirm(TwoLineListItem):
    """Objeto para la lista de usuarios"""

class AppMainMenu(MDScreen, Widget): # Ventana Principal
    """
    Pantalla principal del programa
    """
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, model, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model

        set_glob_loaded_cli(self.controller.load_cli("Admin2025@email.com"))
        self.model.login_cod_cli = glob_loaded_cli['a_cod_cli']

        self.wrap = MDFloatLayout()
        self.add_widget(self.wrap)

        self.MainMenuBox = MainMenuBox(self.model, self.controller)
        self.wrap.add_widget(self.MainMenuBox)

    # Son llamados cuando se inicializan los popups
    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller
