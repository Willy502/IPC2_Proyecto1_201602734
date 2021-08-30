class ProyectoSingleton(object):

    __instance = None
    file = None
    positions = None
    name = None
    ground = None
    finish = None

    def __new__(cls):
        if ProyectoSingleton.__instance is None:
            ProyectoSingleton.__instance = object.__new__(cls)
        return ProyectoSingleton.__instance