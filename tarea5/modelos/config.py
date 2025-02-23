class DBConfig:
    _config = {}  # Diccionario privado para la configuración

    @classmethod
    def set_config(cls, config):
        """Guarda la configuración de la base de datos."""
        cls._config = config

    @classmethod
    def get_config(cls):
        """Devuelve la configuración de la base de datos."""
        return cls._config
