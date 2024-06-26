
from decorators.permissions import require_permiso
def menu_action(name: str, order: int = 0, permiso=None):
    def decorator(func):
        if permiso:
            func = require_permiso(permiso)(func)
        func.is_menu_action = True
        func.menu_name = name
        func.menu_order = order
        return func
    return decorator
