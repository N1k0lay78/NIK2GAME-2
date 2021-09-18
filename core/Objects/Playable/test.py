from Playeble import Playable


class Test:
    def __init__(self, delta):
        self.delta = delta


test = Test(1)
pl = Playable(test, 'a', 0, 0, '')
pl.is_on_ground = True
pl.is_g = True
pl.move(1, 1, True)
print(pl.acceleration == [50, 30], pl.pos == [50, 30])
pl.is_on_ground = False
pl.move(1, 0, False)
print(pl.acceleration == [30, 20.189999999999998], pl.pos == [80, 50.19])
pl.is_g = False
pl.move(1, 1, False)
print(pl.acceleration == [21.0, 21.0], pl.pos == [101.0, 71.19])
pl.move(0.8, 0.8, False)
print(pl.acceleration == [16.799999999999997, 16.799999999999997], pl.pos == [117.8, 87.99])
