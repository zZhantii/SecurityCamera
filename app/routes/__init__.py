from .public import register_public_routes
from .private import register_private_routes

# Rutas public y privadas   
def register_routes(app): 
    register_public_routes(app)
    register_private_routes(app)