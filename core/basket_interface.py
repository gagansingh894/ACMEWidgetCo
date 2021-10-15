from abc import ABC, abstractmethod


class BasketInterface(object):
    """
    Interface which list methods for Basket class.
    """

    @abstractmethod
    def add_product(self, product_code: str):
        """
        Method declaration for updating items in the basket
        :param product_code:
        :return:
        """
        pass

    @abstractmethod
    def calculate_total(self):
        """
        Method declaration for calculating total of items in the basket
        :return:
        """
        pass
