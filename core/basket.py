from core.basket_interface import BasketInterface
from core.config import PRODUCT_CATALOGUE, DELIVERY_COST
import copy
from typing import Dict


class Basket(BasketInterface):
    """
    Method Names
     - add_product()
     - calculate_total()

    Helper Functions
     - _make_delivery_cost_adjustments()
     - _update_with_offer()
    """

    def __init__(self, product_catalogue: Dict = PRODUCT_CATALOGUE, delivery_cost: Dict = DELIVERY_COST,
                 offer_name: [str, None] = None) -> None:
        """

        :param product_catalogue: Dictionary containing all the products and their prices.
                                  The key is the product code and value itself is another dictionary containing
                                  the name of product and the price
        :param delivery_cost: Dictionary containing the threshold value as key and the corresponding discount amount
                              to be offered as value
        :param offer_name: Name of the offer
        """
        self.items = list()
        self.catalogue = product_catalogue
        self.delivery_cost = delivery_cost
        self.offer_name = offer_name

    def add_product(self, product_code: str) -> "Basket":
        """
        Method implementation - This methods updates basket based on product code.
        :param product_code: product code of the item which is to be added to the list
        :return:
        """
        product = self.catalogue.get(product_code)
        if product is not None:
            product = copy.deepcopy(product)
            product.update({"product_code": product_code})
            self.items.append(product)
        else:
            raise ValueError(f"You are trying to add a product with code {product_code} which does not exist.")
        return self

    def calculate_total(self) -> float:
        """
        Method implementation - This methods calculates the total based on number of items, offer if any and discounts.
        :return:
        """
        total = 0.0

        # Check for offers and update
        if self.offer_name is not None:
            self._update_with_offer()

        # compute total
        for item in self.items:
            total += item['price']

        # Make adjustments to final price
        updated_total = self._make_delivery_cost_adjustments(total=total)
        del total
        return updated_total

    def _make_delivery_cost_adjustments(self, total: float) -> float:
        """
        Helper function which takes in existing total amount and based on conditions apply update total with discounts
        :param total: existing total value of items in basket
        :return:
        """
        if total <= 50:
            return total + self.delivery_cost[50]
        elif total <= 90:
            return total + self.delivery_cost[90]
        else:
            return total

    def _update_with_offer(self):
        """
        Helper function to update cart based on offer. Description of offer is given in the config file.
        :return:
        """
        if self.offer_name == "BORGSHP":
            result = list(filter(lambda item: item['product'] == 'Red', self.items))
            if len(result) > 1:
                item = result[-1]
                item['price'] /= 2
