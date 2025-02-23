import mysql.connector
from modelos.models import TipoCocinaModel, TipoReservaModel, SalonModel, ReservaModel, ClienteModel
from modelos.config import DBConfig

class BaseDAO:
    def __init__(self):
        config = DBConfig.get_config()

        db = config.get("db")
        user = config.get("user")
        psw = config.get("psw")
        port = config.get("port")
        host = config.get("host")

        if not all([db, user, psw, port, host]):
            raise ValueError("Faltan datos de conexión a la BD.")

        self.conn = mysql.connector.connect(
            user=user, password=psw, port=port, host=host, database=db
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute_query(self, query, params=None, fetch_one=False):
        self.cursor.execute(query, params or ())
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
        

class TiposCocinaDAO(BaseDAO):
    def get(self, tipo_cocina_id):
        query = "SELECT * FROM tipos_cocina WHERE tipo_cocina_id = %s"
        row = self.execute_query(query, (tipo_cocina_id,), fetch_one=True)
        if row:
            return TipoCocinaModel(row['tipo_cocina_id'], row['nombre'])
        return None

    def get_all(self):
        query = "SELECT * FROM tipos_cocina"
        rows = self.execute_query(query)
        return [TipoCocinaModel(row['tipo_cocina_id'], row['nombre']) for row in rows]


class SalonesDAO(BaseDAO):
    def get(self, salon_id):
        query = "SELECT * FROM salones WHERE salon_id = %s"
        row = self.execute_query(query, (salon_id,), fetch_one=True)
        if row:
            return SalonModel(row['salon_id'], row['nombre'])
        return None

    def get_all(self):
        query = "SELECT * FROM salones"
        rows = self.execute_query(query)
        return [SalonModel(row['salon_id'], row['nombre']) for row in rows]


class TiposReservasDAO(BaseDAO):
    def get(self, tipo_reserva_id):
        query = "SELECT * FROM tipos_reservas WHERE tipo_reserva_id = %s"
        row = self.execute_query(query, (tipo_reserva_id,), fetch_one=True)
        if row:
            return TipoReservaModel(row['tipo_reserva_id'], row['nombre'], row['requiere_jornadas'], row['requiere_habitaciones'])
        return None
    
    def get_all(self):
        query = "SELECT * FROM tipos_reservas"
        rows = self.execute_query(query)
        return [TipoReservaModel(row['tipo_reserva_id'], row['nombre'], row['requiere_jornadas'], row['requiere_habitaciones']) for row in rows]


class ReservasDAO(BaseDAO):
    def get(self, reserva_id):
        query = "SELECT * FROM reservas WHERE reserva_id = %s"
        row = self.execute_query(query, (reserva_id,), fetch_one=True)
        if row:
            return ReservaModel(
                row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                row['id_cliente'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
            )
        return None
    
    def checkFechaOcupada(self, fecha, salon_id, reserva_id):
        query = "SELECT * FROM reservas WHERE fecha = %s AND salon_id = %s AND reserva_id != %s"
        row = self.execute_query(query, (fecha, salon_id, reserva_id), fetch_one=True)
        return True if row else False
    
    def get_by_salon_id(self, salon_id):
        query = "SELECT * FROM reservas WHERE salon_id = %s ORDER BY fecha"
        rows = self.execute_query(query, (salon_id,))
        if rows:
            return [
                ReservaModel(
                    row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                    row['id_cliente'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
                ) for row in rows
            ]
        return None

    def get_all(self):
        query = "SELECT * FROM reservas"
        rows = self.execute_query(query)
        return [
            ReservaModel(
                row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                row['id_cliente'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
            ) for row in rows
        ]

    def create(self, reserva: ReservaModel):
        query = """
        INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        reserva_id = self.execute_query(query, (
            reserva.tipo_reserva_id, reserva.salon_id, reserva.tipo_cocina_id,
            reserva.id_cliente, reserva.fecha, reserva.ocupacion, reserva.jornadas, reserva.habitaciones
        ))
        return self.get(reserva_id)

    def update(self, reserva: ReservaModel):
        query = """
        UPDATE reservas 
        SET tipo_reserva_id = %s, salon_id = %s, tipo_cocina_id = %s, id_cliente = %s, fecha = %s, 
            ocupacion = %s, jornadas = %s, habitaciones = %s
        WHERE reserva_id = %s
        """
        self.execute_query(query, (
            reserva.tipo_reserva_id, reserva.salon_id, reserva.tipo_cocina_id, reserva.id_cliente,
            reserva.fecha, reserva.ocupacion, reserva.jornadas, reserva.habitaciones, reserva.reserva_id
        ))
        return self.get(reserva.reserva_id)
    
    def delete(self, reserva_id):
        query = "DELETE FROM reservas WHERE reserva_id = %s"
        self.execute_query(query, (reserva_id,))

    def delete_by_cliente(self, cliente_id):
        query = "DELETE FROM reservas WHERE id_cliente = %s"
        self.execute_query(query, (cliente_id,))
    

class ClientesDAO(BaseDAO):
    def get(self, cliente_id):
        query = "SELECT * FROM clientes WHERE Id = %s"
        row = self.execute_query(query, (cliente_id,), fetch_one=True)
        if row:
            return ClienteModel(
                row['Id'], row['Nombre'], row['Apellidos'], row['Num_Identificacion'], row['Fec_Nac'],
                row['Pais'], row['Telefono'], row['email'], row['Sexo'], row['Menores']
            )  # Devuelve un objeto ClienteModel
        return None
    
    def get_all(self):
        query = "SELECT * FROM clientes"
        rows = self.execute_query(query)
        return [
            ClienteModel(
                row['Id'], row['Nombre'], row['Apellidos'], row['Num_Identificacion'], row['Fec_Nac'],
                row['Pais'], row['Telefono'], row['email'], row['Sexo'], row['Menores']
            ) for row in rows
        ]  # Devuelve una lista de objetos ClienteModel

    def create(self, cliente: ClienteModel):
        query = """
        INSERT INTO clientes (Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cliente_id = self.execute_query(query, (
            cliente.nombre, cliente.apellidos, cliente.num_identificacion, cliente.fec_nac, cliente.pais,
            cliente.telefono, cliente.email, cliente.sexo, cliente.menores
        ))
        return self.get(cliente_id)  # Devuelve el objeto ClienteModel con los datos del nuevo cliente
    
    def update(self, cliente: ClienteModel):
        query = """
        UPDATE clientes 
        SET Nombre = %s, Apellidos = %s, Num_Identificacion = %s, Fec_Nac = %s, Pais = %s, Telefono = %s, 
            email = %s, Sexo = %s, Menores = %s 
        WHERE Id = %s
        """
        self.execute_query(query, (
            cliente.nombre, cliente.apellidos, cliente.num_identificacion, cliente.fec_nac, cliente.pais,
            cliente.telefono, cliente.email, cliente.sexo, cliente.menores, cliente.id
        ))
        return self.get(cliente.id)  # Devuelve el objeto ClienteModel del cliente actualizado
    
    def delete(self, cliente_id):
        query = "DELETE FROM clientes WHERE Id = %s"
        self.execute_query(query, (cliente_id,))

    def checkDniExiste(self, dni, cliente_id):
        query = "SELECT * FROM clientes WHERE Num_Identificacion = %s AND Id != %s"
        row = self.execute_query(query, (dni, cliente_id), fetch_one=True)
        return True if row else False


class UsuariosDAO(BaseDAO):
    def check_credentials(self, usuario, contrasenia):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND contrasenia = %s"
        row = self.execute_query(query, (usuario, contrasenia), fetch_one=True)
        return row is not None  # Devuelve True si existe el usuario con la contraseña correcta, False si no
