Descripción del proyecto:

app/models.py: 
class DAO_Product: conecta con la base de datos y nos genera una lista de diccionarios con toda la información de los productos, también la usamos para verificar que el id del producto que el usuario inserte está en esta base de datos, devolviendo un diccionario con la información del producto.

class Ticket: contiene 3 funciones para agregar, obtener subtotal por producto, actualizar las cantidades en el ticket y una pata el total de la compra.

app/fronting.py: contiene 3 clases, class TitleView para "pintar" el título del programa, class ProductsView para obtener la lista de todos los productos disponibles y una última class TicketView que gestiona la compra, con la información que el usuario vaya insertando.

data/create_database.py: Contiene el código para la creación de la base de datos desde un archivo .csv, al cual he llamado "products".

Tests del proyecto:

test_models.py: En este archivo están todos los tests realizados para "verificar" el funcionamiento de cada una de las clases.
pre_views.py: En este archivo están las pruebas de visualización.

Requirement.txt: Contiene todas las dependencias que necesitan instalarse para gestionar este proyecto.

Estatus del proyecto:

 el "back" necesario considero lo tengo terminado, pero estoy teniendo problemas con la vizualización de lista completa de los productos en class ProductsView (app/fronting.py), sólo me "pinta" el primer producto de la lista de 10, he intentado y buscado en ChatGPT, COPILOT pero no consigo el error en el bucle, por eso he pedido tu ayuda.

 Observaciones: Creo que entendí mal el ejercicio, pensé que se tenía que listar los productos y luego generar por separado un ticket con los productos comprados, de eso me acabo de dar cuenta, no sé si eso podría tener un gran impacto en la evaluación o podría ser aceptable, cuando se haga la prueba de vistas, tal cual como está hora podra ver la intención de mi visualización.

