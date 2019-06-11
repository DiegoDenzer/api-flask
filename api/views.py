from api import resources
from api.run import api

#endPoints for login ( endpoints para login, registro e tokens)
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')

# endpoints api
api.add_resource(resources.SecretResource, '/secret')
