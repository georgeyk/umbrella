from loafer.managers import LoaferManager

from .routes import routes


service = LoaferManager(routes=routes)
print('iniciando serviço ...')
service.run()
