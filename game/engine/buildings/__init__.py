from .barrack import Barrack
from .field import Field
from .tower import Tower
from .wall import Wall
from .granary import Granary
from .grange import Grange
from .gallery import Gallery
from .entrance_gallery import EntranceGallery
from .exit_gallery import ExitGallery
from .cannon import Cannon
from .factory_weapon_headquarters import FactoryWeaponHeadquarters
from .foundry import Foundry
from .init_class import *

DICT_BUILDINGS = {"Barrack": Barrack,
                  "Field": Field,
                  "Granary": Granary,
                  "Tower": Tower,
                  "Wall": Wall,
                  "Grange": Grange,
                  "Gallery" : Gallery,
                  "EntranceGallery" : EntranceGallery,
                  "ExitGallery" : ExitGallery,
                  "Cannon" : Cannon,
                  "FactoryWeaponHeadquarters" : FactoryWeaponHeadquarters,
                  "Foundry" : Foundry}
