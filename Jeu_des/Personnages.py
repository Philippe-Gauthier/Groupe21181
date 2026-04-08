
import des

force = 0
point_de_vie = 0


def creation(f,pv):
    f = des.des(1,20)
    pv = des.des(2,6)
    return f, pv

force , point_de_vie = creation(force, point_de_vie)
print(force)
print(point_de_vie)