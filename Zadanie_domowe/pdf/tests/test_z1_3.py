from Zadanie_domowe.pdf.zadania.z1_3 import status


def test_status():
    assert status(statuses, "online") == 2
    assert status(status, "offline") == 1
    assert status(status, "xxx") == 0
