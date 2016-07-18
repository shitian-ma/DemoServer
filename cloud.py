# coding: utf-8

from leancloud import Engine

from app import app


engine = Engine(app)


@engine.before_save('Plane')
def before_plane_save(plane):
    print plane