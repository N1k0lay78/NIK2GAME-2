from core.Objects.Playable.Playeble import Playable
from animation import ghost
from core.toolsImage import AnimationDefault, TileSet, load_image


class Ghost(Playable):
    def __init__(self, game, name, x, y, tile_set=TileSet(load_image(ghost["filename"]), ghost["sizeCell"])):
        super().__init__(game, name, x, y, AnimationDefault(tile_set, **ghost["animation"]))
