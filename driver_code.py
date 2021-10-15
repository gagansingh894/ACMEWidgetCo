from core.basket import Basket

if __name__ == "__main__":
    my_basket = Basket(offer_name='BORGSHP')
    my_basket.add_product("RO1")
    my_basket.add_product("RO1")
    print(my_basket.items)
    print(my_basket.calculate_total())
    print(my_basket.items)


