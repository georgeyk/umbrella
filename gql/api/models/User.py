from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin


class User(Model, UUIDPrimaryKeyMixin):
    __uuid_version__ = 4
