from core.basket import Basket


def test_condition_1():
    my_basket = Basket(offer_name='BORGSHP')
    my_basket.add_product("BO1")
    my_basket.add_product("GO1")
    result = my_basket.calculate_total()
    assert round(result, 2) == 37.85


def test_condition_2():
    my_basket = Basket(offer_name='BORGSHP')
    my_basket.add_product("RO1")
    my_basket.add_product("RO1")
    result = my_basket.calculate_total()
    assert round(result, 2) == 54.38


def test_condition_3():
    my_basket = Basket(offer_name='BORGSHP')
    my_basket.add_product("RO1")
    my_basket.add_product("GO1")
    result = my_basket.calculate_total()
    assert round(result, 2) == 60.85


def test_condition_4():
    my_basket = Basket(offer_name='BORGSHP')
    my_basket.add_product("BO1")
    my_basket.add_product("BO1")
    my_basket.add_product("RO1")
    my_basket.add_product("RO1")
    my_basket.add_product("RO1")
    result = my_basket.calculate_total()
    assert round(result, 2) == 98.28

