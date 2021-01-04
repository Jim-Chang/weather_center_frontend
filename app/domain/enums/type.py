import enum

class FeatureType(enum.Enum):
    all = 'all'
    youtubedl = 'youtubedl'
    weather = 'weather'
    stock = 'stock'
    wordpress = 'wordpress'
    motion = 'motion'

class RoleType(enum.Enum):
    admin = 'admin'
    home_user = 'home_user'
    anonymous = 'anonymous'
