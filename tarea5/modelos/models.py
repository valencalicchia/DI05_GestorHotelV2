class TipoCocinaModel:
    def __init__(self, tipo_cocina_id, nombre):
        self.tipo_cocina_id = tipo_cocina_id  # ID único del tipo de cocina
        self.nombre = nombre  # Nombre del tipo de cocina

    def __repr__(self):
        return f"TipoCocina(tipo_cocina_id={self.tipo_cocina_id}, nombre='{self.nombre}')"


class SalonModel:
    def __init__(self, salon_id, nombre):
        self.salon_id = salon_id  # ID único del salón
        self.nombre = nombre  # Nombre del salón

    def __repr__(self):
        return f"Salon(salon_id={self.salon_id}, nombre='{self.nombre}')"


class TipoReservaModel:
    def __init__(self, tipo_reserva_id, nombre, requiere_jornadas, requiere_habitaciones):
        self.tipo_reserva_id = tipo_reserva_id  # ID único del tipo de reserva
        self.nombre = nombre  # Nombre del tipo de reserva
        self.requiere_jornadas = requiere_jornadas  # Si se requieren jornadas
        self.requiere_habitaciones = requiere_habitaciones  # Si se requieren habitaciones

    def __repr__(self):
        return (f"TipoReserva(tipo_reserva_id={self.tipo_reserva_id}, nombre='{self.nombre}', "
                f"requiere_jornadas={self.requiere_jornadas}, requiere_habitaciones={self.requiere_habitaciones})")


class ReservaModel:
    def __init__(self, reserva_id, tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones=0):
        self.reserva_id = reserva_id  # ID único de la reserva
        self.tipo_reserva_id = tipo_reserva_id  # ID del tipo de reserva
        self.salon_id = salon_id  # ID del salón reservado
        self.tipo_cocina_id = tipo_cocina_id  # ID del tipo de cocina asociado
        self.id_cliente = id_cliente  # ID del cliente que realizó la reserva
        self.fecha = fecha  # Fecha y hora de la reserva
        self.ocupacion = ocupacion  # Número de personas en la reserva
        self.jornadas = jornadas  # Número de jornadas (días)
        self.habitaciones = habitaciones  # Número de habitaciones (por defecto 0 si no aplica)

    def __repr__(self):
        return (f"Reserva(reserva_id={self.reserva_id}, tipo_reserva_id={self.tipo_reserva_id}, "
                f"salon_id={self.salon_id}, tipo_cocina_id={self.tipo_cocina_id}, "
                f"id_cliente={self.id_cliente}, fecha='{self.fecha}', ocupacion={self.ocupacion}, "
                f"jornadas={self.jornadas}, habitaciones={self.habitaciones})")


class ClienteModel:
    def __init__(self, id, nombre, apellidos, num_identificacion, fec_nac, pais, telefono, email, sexo, menores):
        self.id = id  # ID único del cliente
        self.nombre = nombre  # Nombre del cliente
        self.apellidos = apellidos  # Apellidos del cliente
        self.num_identificacion = num_identificacion  # Número de identificación único
        self.fec_nac = fec_nac  # Fecha de nacimiento del cliente
        self.pais = pais  # País del cliente
        self.telefono = telefono  # Teléfono del cliente
        self.email = email  # Correo electrónico del cliente
        self.sexo = sexo  # Sexo del cliente (puede ser 'H', 'M', o 'N')
        self.menores = menores  # Cantidad de menores asociados al cliente

    def __repr__(self):
        return (f"Cliente(id={self.id}, nombre='{self.nombre}', apellidos='{self.apellidos}', "
                f"num_identificacion='{self.num_identificacion}', fec_nac='{self.fec_nac}', "
                f"pais='{self.pais}', telefono='{self.telefono}', email='{self.email}', "
                f"sexo='{self.sexo}', menores={self.menores})")
