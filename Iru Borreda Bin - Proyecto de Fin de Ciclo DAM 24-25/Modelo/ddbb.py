# firebase admin email: editorcamisetas4dmin@gmail.com
# firebase admin passw: A1B2C3D4!
# firebase project: editor-camisetas-data
# Video I am following: https://youtu.be/FR1hLBRYj0o?si=pYEFoI0VukyR42jq

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import Increment
from google.cloud.firestore_v1 import FieldFilter, aggregation

# Cargamos nuestras credenciales
firebase_sdk = credentials.Certificate('Modelo/editor-camisetas-data-firebase-adminsdk-fbsvc-f42974823d.json')

# Hacemos referencia a la base de datos
app = firebase_admin.initialize_app(firebase_sdk)

# Inicializamos la cuenta de servicio
db = firestore.client()

# Contamos el número de documentos que hay en la colección de firestore para definir un código simple
def gen_ped_id():
    # query = db.collection('pedidos').where(filter=FieldFilter('cod_ped', '>', '0'))
    # ped_aggregate_query = aggregation.AggregationQuery(query)
    # ped_aggregate_query.count(alias="all")
    #
    # results = ped_aggregate_query.get()
    # for result in results:
    #     print(f"numero de docs {result[0].value}")
    #     return int(result[0].value) + 1
    # return None

    ref = db.collection('0-contadores').document("id_counters")
    doc = ref.get().to_dict()
    ped_id = doc.get('ped_id')
    return ped_id

def gen_cli_id():
    # query = db.collection('clientes').where(filter=FieldFilter('cod_cli', '>', '0'))
    # cli_aggregate_query = aggregation.AggregationQuery(query)
    # cli_aggregate_query.count(alias="all")
    #
    # results = cli_aggregate_query.get()
    # for result in results:
    #     print(f"numero de docs {result[0].value}")
    #     return int(result[0].value) + 1
    # return None

    ref = db.collection('0-contadores').document("id_counters")
    doc = ref.get().to_dict()
    cli_id = doc.get('cli_id')
    return cli_id

class Firebase:

# Metodos para clientes
    def cli_push_item(datos):
        print(datos)
        datos['a_cod_cli'] = gen_cli_id()
        db.collection('1-cuentas').document(f"cliente_{gen_cli_id()}").set(datos)
        db.collection('1-cuentas').document(f"cliente_{gen_cli_id()}").update(
            {"a_timestamp": firestore.SERVER_TIMESTAMP, "a_timestamp_ult_con": firestore.SERVER_TIMESTAMP})
        db.collection('0-contadores').document("id_counters").update({"cli_id": Increment(1)})

    def login_cli_find(email):
        # print(f'Email en ddbb: {email}')
        docs_ref = (db.collection('1-cuentas')
                   .where(filter=FieldFilter("b_email", "==", f'{email}'))
                   # .where(filter=FieldFilter("b_passwd", "==", f'{passwd}'))
                   .stream())
        # print(f'Cli Doc: {docs_ref}')
        doc = []
        if docs_ref:
            docs_dict = {doc.id:doc.to_dict() for doc in docs_ref}

            for item in docs_dict:
                doc = docs_dict[item]

        print(f'Cli Doc: {doc}')
        for field in doc:
            print(f'---{field} : {doc[field]}')
        return doc

    def login_cli_passwd_confirm(email, passwd):
        doc = Firebase.login_cli_find(email)
        if doc['b_passwd'] == passwd:
            return True
        else:
            return False

    def cli_getAll_items (foo):
        docs = (db.collection('1-cuentas')
                .where(filter=FieldFilter("a_cod_cli", ">", 0))
                .stream())
        docs_dict = {doc.id:doc.to_dict() for doc in docs}
        return docs_dict

    def cli_update_login_time (email):
        doc = Firebase.login_cli_find(email)

        cli_doc_id = doc['a_cod_cli']

        if cli_doc_id == 0:
            db.collection('1-cuentas').document(f"admin_0").update(
                {"a_timestamp_ult_con": firestore.SERVER_TIMESTAMP})
        else:
            db.collection('1-cuentas').document(f"cliente_{cli_doc_id}").update(
                            {"a_timestamp_ult_con": firestore.SERVER_TIMESTAMP})

# Metodos para pedidos
    # Metodo para introducir nuevos pedidos
    def ped_push_item (datos, cod_cli):
        datos['a_cod_ped']= gen_ped_id()
        datos['a_state'] = 'En Espera'
        db.collection('2-pedidos').document(f"[cod-cli]_pedido_{gen_ped_id()}").set(datos)
        db.collection('2-pedidos').document(f"[cod-cli]_pedido_{gen_ped_id()}").update({"a_timestamp": firestore.SERVER_TIMESTAMP, "a_timestamp_last_update": firestore.SERVER_TIMESTAMP})
        db.collection('0-contadores').document("id_counters").update({"ped_id": Increment(1)})
        # return datos

    # Metodo para modificar pedidos
    def ped_update_item (new_datos, cod_ped):
        db.collection('2-pedidos').document(f"[cod-cli]_pedido_{cod_ped}").update(new_datos)
        db.collection('2-pedidos').document(f"[cod-cli]_pedido_{cod_ped}").update({"a_timestamp_last_update": firestore.SERVER_TIMESTAMP})
        print(f"[cod-cli]_pedido_{cod_ped} Actualizado")

    # Metodo para borrar un pedido
    def ped_delete_item (cod_ped):
        db.collection('2-pedidos').document(f"[cod-cli]_pedido_{cod_ped}").delete()
        print(f"[cod-cli]_pedido_{cod_ped} Borrado")

    # Metodo para cargar los datos de los pedidos de la ddbb en la lista
    def ped_getAll_items (foo):
        docs = (db.collection('2-pedidos')
                .where(filter=FieldFilter("a_cod_ped", ">=", 0))
                .stream())
        docs_dict = {doc.id:doc.to_dict() for doc in docs}

        # print(f'Ped Cod: {docs_dict}')
        # for doc in docs_dict:
        #     print(f'---{doc} : {docs_dict[doc]}')

        return docs_dict

    def ped_getCli_items (cod_cli):
        docs = (db.collection('2-pedidos')
                .where(filter=FieldFilter("a_cod_cli", "==", cod_cli))
                .stream())
        docs_dict = {doc.id:doc.to_dict() for doc in docs}

        # print(f'Ped Cod: {docs_dict}')
        # for doc in docs_dict:
        #     print(f'---{doc} : {docs_dict[doc]}')

        return docs_dict

    def ped_getDoc(doc_id):
        doc_ref = db.collection('2-pedidos').document(doc_id)
        doc = doc_ref.get().to_dict()
        return doc