from mathematica.algebra.matrices import add_matrices, m1, m2


def test_add_matrices():
    assert add_matrices(m1, m2)
