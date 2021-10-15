"""
CONFIG - Requirement as described in the document
"""

"""
Catalogue of items as described in requirements
For POC, we will be using python dictionary. However, in case of production system, we can use a NoSQL DB (MongoDB) 
for storing products. This will provide scalability
"""
PRODUCT_CATALOGUE = {
    "RO1": {
        "product": "Red",
        "price": 32.95
    },
    "GO1": {
        "product": "Green",
        "price": 24.95
    },
    "BO1": {
        "product": "Blue",
        "price": 7.95
    }
}

"""
Delivery cost mapping. 
Key is threshold and value is the amount which will be added to the total. Again, for POC, we will be using a dictionary. 
Ideally, since this is more like a configuration, we can store this in a key value store. The benefit is that we can 
connect our Basket class to this key value store. This way, in future if the cost of delivery increases due to xyz 
reason, no change in code will be required. However, let's say the threshold value change, then code changes 
will be required.
"""
DELIVERY_COST = {
    50: 4.95,
    90: 2.95
}

"""
Description of Valid Offers
"""
VALID_OFFERS = {
    "BORGSHP": "buy one red widget,get the second half price"
}

