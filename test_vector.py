from vector import Vector3D


def test_str():
    u = Vector3D(0, 4, -2)
    assert str(u) == "(0, 4, -2)"


def test_repr():
    u = Vector3D(0, 4, -2)
    assert repr(u) == "Vector3D(0, 4, -2)"


def test_add():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u + v == Vector3D(4, 4, 0)


def test_sub():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u - v == Vector3D(0, -4, -4)


def test_dot():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u.dot(v) == (4 + 0 - 4)


def test_mul():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u * v == (4 + 0 - 4)


def test_cross():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u.cross(v) == Vector3D(8, -8, 8)


def test_matmul():
    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u @ v == Vector3D(8, -8, 8)


def test_perpendicular():

    u = Vector3D(2, 0, -2)
    v = Vector3D(2, 4, 2)
    assert u.perpendicular(v)

    w = u @ v
    assert w.perpendicular(u)
    assert w.perpendicular(v)


def test_scalarmult_right():

    u = Vector3D(4, -6, 2)
    assert u * 2 == Vector3D(8, -12, 4)


def test_scalarmult_left():

    u = Vector3D(4, -6, 2)
    assert 2 * u == Vector3D(8, -12, 4)


def test_get_length():
    u = Vector3D(4, 0, 0)
    assert u.length == 4


def test_set_length():
    u = Vector3D(4, 0, 0)
    u.length = 1
    assert u == Vector3D(1, 0, 0)


def test_unit_vector():

    u = Vector3D(2, -2, 1)
    w = u.unit()

    assert w.length == 1
    assert not (u is w)
