from model import *
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        add(Cube(app, pos=(5, 0, 1), scale=(10, 0.1, 16), tex_id=3))

        # building
        add(Cube(app, pos=(0, 5.1, 10), scale=(4.9, 5, 2), tex_id=4))
        # building walls (left, right)
        add(Cube(app, pos=(-4.95, 5.1, 10), scale=(0.05, 5, 2), tex_id=10))
        add(Cube(app, pos=(4.95, 5.1, 10), scale=(0.05, 5, 2), tex_id=10))
        #building roof
        add(Cube(app, pos=(0, 10.2, 10),  scale=(5.2, 0.1, 2.2), tex_id=9))

        #shops
        add(Cube(app, pos=(-3.3, 1.7, 7), scale=(1.6, 1.5, 1), tex_id=5))
        add(Cube(app, pos=(0, 1.7, 7), scale=(1.65, 1.5, 1), tex_id=6))
        add(Cube(app, pos=(3.3, 1.7, 7), scale=(1.6, 1.5, 1), tex_id=7))

        add(Cube(app, pos=(-4.95, 1.7, 7), scale=(0.05, 1.5, 1), tex_id=10))
        add(Cube(app, pos=(4.95, 1.7, 7), scale=(0.05, 1.5, 1), tex_id=10))
        #roof
        add(Cube(app, pos=(0, 3.3, 7), scale=(5.2, 0.1, 1.2), tex_id=9))

        #bordur
        add(Cube(app, pos=(0, 0.1, 6), scale=(5, 0.1, 2), tex_id=8))

        
        add(Bench(app, pos=(5.5, 0, 7), rot=(0, 90, 0)))
        add(Bench(app, pos=(5.5, 0, 10), rot=(0, 90, 0)))

        add(Garbagec(app, pos=(-4,0,12.5)))
        add(Garbagec(app, pos=(-3,0,12.5)))
        add(Garbagec(app, pos=(3,0,12.5)))
        add(Garbagec(app, pos=(4,0,12.5)))

        #road
        add(Road(app, pos=(8, -1, 0)))
        add(Ctree(app, pos=(0, 0, 0)))
        add(Ctree(app, pos=(13, 0, -10)))
        add(Ctree(app, pos=(13, 0, 0)))
        add(Ctree(app, pos=(13, 0, 10)))

        # building
        add(Cube(app, pos=(0, 5.1, -10), scale=(4.9, 5, 2), tex_id=4))
        # building walls (left, right)
        add(Cube(app, pos=(-4.95, 5.1, -10), scale=(0.05, 5, 2), tex_id=10))
        add(Cube(app, pos=(4.95, 5.1, -10), scale=(0.05, 5, 2), tex_id=10))
        #building roof
        add(Cube(app, pos=(0, 10.2, -10),  scale=(5.2, 0.1, 2.2), tex_id=9))

        #shops
        add(Cube(app, pos=(-3.3, 1.7, -7), scale=(1.6, 1.5, 1), tex_id=5))
        add(Cube(app, pos=(0, 1.7, -7), scale=(1.65, 1.5, 1), tex_id=6))
        add(Cube(app, pos=(3.3, 1.7, -7), scale=(1.6, 1.5, 1), tex_id=7))

        add(Cube(app, pos=(-4.95, 1.7, -7), scale=(0.05, 1.5, 1), tex_id=10))
        add(Cube(app, pos=(4.95, 1.7, -7), scale=(0.05, 1.5, 1), tex_id=10))
        #roof
        add(Cube(app, pos=(0, 3.3, -7), scale=(5.2, 0.1, 1.2), tex_id=9))

        #bordur
        add(Cube(app, pos=(0, 0.1, -6), scale=(5, 0.1, 2), tex_id=8))
        
        add(Bench(app, pos=(5.5, 0, -7), rot=(0, 90, 0)))
        add(Bench(app, pos=(5.5, 0, -7), rot=(0, 90, 0)))

        add(Garbagec(app, pos=(-4,0,-12.5)))
        add(Garbagec(app, pos=(-3,0,-12.5)))
        add(Garbagec(app, pos=(3,0,-12.5)))
        add(Garbagec(app, pos=(4,0,-12.5)))

    def update(self): ...


