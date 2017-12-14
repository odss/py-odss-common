import inspect

from . import consts

__all__ = ['activator']


def activator(clazz):
    setattr(inspect.getmodule(clazz), consts.ACTIVATOR, clazz())
    return clazz
