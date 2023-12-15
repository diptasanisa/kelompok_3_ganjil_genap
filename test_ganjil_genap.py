from ganjil_genap import cek_ganjil_genap

def test_ganjil():
    assert cek_ganjil_genap(3) == "Ganjil"

def test_genap():
    assert cek_ganjil_genap(4) == "Genap"

def test_ganjil_salah():
    assert not cek_ganjil_genap(4) == "Ganjil"

def test_0_genap():
    assert cek_ganjil_genap(0) == "Genap"
    
def test_minus_ganjil():
    assert cek_ganjil_genap(-1) == "Ganjil"