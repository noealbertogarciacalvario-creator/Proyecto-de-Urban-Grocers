# Headers base para requests
USER_HEADERS = {
    "Content-Type": "application/json"
}


# =========================
# DATOS DE USUARIO
# =========================

VALID_USER_BODY = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave, Hamburg, NY"
}


# =========================
# DATOS DE KIT
# =========================

def get_kit_body(name):
    """Genera un body de kit con el nombre especificado."""
    return {
        "name": name
    }


# =========================
# CASOS DE PRUEBA (name)
# =========================

VALID_KIT_NAMES = [
    "a",                        # mínimo válido
    "A valid kit name",         # normal
    "123",                      # números
    "Kit con espacios",         # espacios
    "Kit-123_@",                # caracteres especiales
]

INVALID_KIT_NAMES = [
    "",                         # vacío
    None,                       # tipo incorrecto
    123,                        # tipo incorrecto
    "a" * 512                   # demasiado largo
]