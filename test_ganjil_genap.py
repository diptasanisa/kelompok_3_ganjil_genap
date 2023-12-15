from ganjil_genap import cek_ganjil_genap

def test_ganjil():
    assert cek_ganjil_genap(3) == "Ganjil"

def test_genap():
    assert cek_ganjil_genap(4) == "Genap"