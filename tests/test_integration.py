from calculator import add, clear

def test_full_user_add_flow():
    result = add(5, 3)
    assert result == 8

def test_clear_resets_result():
    result = add(4, 6)
    result = clear()
    assert result == 0