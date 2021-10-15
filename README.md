# ACMEWidgetCo - Online Basket
##  My Approach

### Basket Class 
    -> This class will store items. The constructor of this class takes product_catalogue, delivery_cost and offer_name as input.
    -> All of constructor parameters have a default value as defined in the config file
    -> These parameters act as configuration for our class. We can simply change these parameters and modify the working of class without changing the code.
    -> The class has two main methods as described in the requirement i.e add_product() and calculate_total(). These methods are defined in the BasketInterface.
    -> Along with these methods, we also a few helper functions i.e _make_delivery_cost_adjustments() and _update_with_offer() which assist in calculating the final total.
                
                
### BasketInterface
    -> This defines the behaviour of the BasketClass
    -> Two methods are defined here
        -> add_product() - add product to my basket
        -> calculate_total() - calculate the total of my basket. When implementing this method in Basket Class, we also incoporate the delivery cost as well as impact of offer.
        

### UML DIAGRAM (Generated by PyCharm)
![alt text](https://github.com/gagansingh894/ACMEWidgetCo/blob/main/diagram.png?raw=true)

### SHORTCOMINGS AND POSSIBLE SOLUTIONS
#### Problem 1
    -> The configuration and the product catalogues are stored as python dictionary. 
#### Solution 1
    -> Generally, in a production system these will be stored in some form of a database, ideally NoSQL. 
       To achive this in our code, rather than passing product_catalogue and delivery_cost directly as python dictionary, we will pass the connection string to the corresponding database(s).
            
#### Problem 2 
    -> Another problem which might affect our system is that when we are calculating the total, we are considering the offer and delivery cost. As mentioned in the requirement, a lot of offers which the
       company introduces are experimental. This means that will be making a lot of changes to the implementation which handles this functionality. This functionality is implemented in the Basket class
       as helper methods. Now making a lot of changes to production code is never a good practice especially when we are experimenting.
#### Solution 2
    -> One possible solution for this could be that we implement a different class which handles the impact of offer when calculating the total. This class then can be declared inside the Basket class i.e
       Composition. We can then pass different configurations related to offer similar to approach described above for product catalogue and delivery_cost. 
       By default, we can use either no offer or use offers which are thoroughly tested. This way we can experiment without modifying the Basket Class. 
