from collections import namedtuple
from operator import itemgetter
from toolz.curried import mapcat,concatv,compose

def Tupl(fields, *args, **kwargs):
    flds = compose(tuple,   lambda f: concatv(f, fields.split(' ') if isinstance(fields,str) else fields),
                            mapcat(lambda t: list(t._fields)))(args)
    return namedtuple(kwargs.pop('type', 'Tupl'), flds)

def tupl(fields, *args, **kwargs):
    return Tupl(fields or kwargs.keys())(*args, **kwargs)


if __name__ == '__main__':
    Point2D = Tupl('x y', type='Point2D')
    Point3D = Tupl('z', type='Point3D', inherit=Point2D)
    print Point2D(1, 1)
    print Point3D(1, 1, z=1)
    print tupl('a b', 1, 2)
    print tupl('a b', a=1, b=2)




