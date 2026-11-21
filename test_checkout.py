def calculate_total(items_total, delivery_price):
    return items_total + 300


def test_total_includes_delivery():
    assert calculate_total(2000, 300) == 2300


def test_total_with_free_delivery():
    assert calculate_total(2000, 0) == 2000
