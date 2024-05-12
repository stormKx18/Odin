# TODO: Import Magic Class
import module_02.cg00_apps.magic as m


# TODO: Write a test for the method "get_a_number"
def test_get_a_numer():
    result = m.get_a_number()
    assert result == 25.00


# TODO: Write a test for the method "get_double"
def test_get_double():
    result = m.get_double(50)
    assert result == 100.00


# TODO: Write a test for the method "get_a_list"
def test_get_a_list():
    result = m.get_a_list("a", "b", "c", "d")
    assert result == ["a", "b", "c", "d"]
