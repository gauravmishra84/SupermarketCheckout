from typing import Dict

class SupermarketCheckout:
    '''
    This class represents the mechanism to caculate the total price payable by
    a customer for their checkout inventory
    
    params: pricing_rule: Dict ( A Dictionary of a product type with unit and special pricing if any)
    
    returns: A new SupermarketCheckout Object
    '''
    def __init__(self, pricing_rules: Dict[str, Dict[str, int]]):
        self.pricing_rules = pricing_rules
        self.items = {}
        
    def scan(self, item: str):
        '''
        Method to add items in the inventory
        
        params: item: string
        '''
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
        total = 0
        for item, count in self.items.items():
            if item in self.pricing_rules:
                price = self.pricing_rules[item]["price"]
                special_price = self.pricing_rules[item].get("special_price")
                
                if special_price:
                    offer_quantity = special_price["quantity"]
                    offer_price = special_price["price"]
                    quo, rem = divmod(count, offer_quantity)
                    total += quo* offer_price
                    total += rem * price
                else:
                    total += count * price
                    
            else:
                raise ValueError(f"Invalid item: {item}")

        return total
    