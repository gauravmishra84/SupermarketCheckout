from typing import Dict

class SupermarketCheckout:
    '''
    This class represents the mechanism to caculate the total price payable by
    a customer for their checkout cart
    
    params: pricing_rule: Dict ( A Dictionary of a product type with unit and special pricing if any)
    
    returns: A new SupermarketCheckout Object
    '''
    def __init__(self, pricing_rules: Dict[str, Dict[str, int]]):
        self.pricing_rules = pricing_rules
        self.items = {}
        
    def scan(self, item: str):
        '''
        Method to add items in the cart
        
        params: item: string
        '''
        # check if the item is part of the inventory
        if item not in self.pricing_rules:
                raise ValueError(f"Invalid item: {item}")            
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        

        
    def total(self) -> int:
        '''
        Method to check the checkout basket and calculate the total payable price
        
        returns: int ( The total price payable with any special offers applicable on the cart)
        '''
        # Check if the shopping cart isn't empty
        if not self.items:
            raise KeyError(f" Empty Cart ")
        
        total = 0
        cart = list(self.items.keys())
        for item in cart:
            if item in self.pricing_rules:
                price = self.pricing_rules[item]["price"]
                special_price = self.pricing_rules[item].get("special_price")
                mix_match = self.pricing_rules[item].get("mix_match", None)
                
                if special_price:
                    offer_quantity = special_price["quantity"]
                    offer_price = special_price["price"]
                    quotient, remainder = divmod(self.items[item], offer_quantity)
                    total += quotient* offer_price
                    total += remainder * price
                    for _ in range(offer_quantity):
                        if self.items[item] > 1:
                            self.items[item] -= 1  
                        else:
                            del self.items[item]
                        
                elif mix_match:
                    offer_quantity = mix_match["quantity"]
                    offer_price = mix_match["price"]
                    mix_match_items = all(i in mix_match["product_type"] for i in self.items)
                    if mix_match_items:
                        total += offer_price
                        for x in mix_match["product_type"]:
                            if self.items[x] > 1:
                                self.items[x] -= 1  
                            else:
                                del self.items[x]
                else:
                    total += self.items[item] * price                     
            else:
                raise ValueError(f"Invalid item: {item}")

        return total
    