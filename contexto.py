class Contexto:
    _usuario = None
    _session = None

    @classmethod
    def set_usuario(cls, usuario, session):
        cls._usuario = usuario
        cls._session = session

    @classmethod
    def get_usuario(cls):
        return cls._usuario

    @classmethod
    def get_session(cls):
        return cls._session

    @classmethod
    def clear(cls):
        cls._usuario = None
        cls._session = None
