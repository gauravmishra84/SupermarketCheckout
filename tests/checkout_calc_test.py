import sys  
sys.path.append("./src")

import unittest
from checkout import checkout_calc as calc


class SupermarketCheckoutGenericTestCases(unittest.TestCase):
    
    pricing_rules =  {
            "A": {"price": 50, "special_price": {"quantity": 3, "price": 130}},
            "B": {"price": 30, "special_price": {"quantity": 2, "price": 45}},
            "C": {"price": 20},
            "D": {"price": 15},
            "E": {"price": 10, "mix_match": {"product_type": ["E","D"], "quantity":2 , "price":40 }},
        }

    def test_valid_item(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        checkout.scan("A")
        self.assertEqual(checkout.items, {'A':1})
        
    def test_invalid_item(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        with self.assertRaises(ValueError):
            checkout.scan("K")

    def test_empty_cart(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        with self.assertRaises(KeyError):
            checkout.total()
            
    def test_calculate_total_without_special_price(self):
        pricing_rules = {
            "A": {"price": 50},
            "B": {"price": 30},
            "C": {"price": 20},
            "D": {"price": 15},
        }
        checkout = calc.SupermarketCheckout(pricing_rules)
        checkout.scan("A")
        checkout.scan("B")
        checkout.scan("C")
        checkout.scan("D")
        self.assertEqual(checkout.total(), 115)
        
    def test_calculate_total_with_special_price(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        checkout.scan("A")
        checkout.scan("B")
        checkout.scan("A")
        checkout.scan("B")
        checkout.scan("A")
        checkout.scan("B")
        self.assertEqual(checkout.total(), 205)
        
    def test_calculate_total_with_mix_match(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        checkout.scan("E")
        checkout.scan("D")
        checkout.scan("D")
        self.assertEqual(checkout.total(), 55)        
        

if __name__ == "__main__":
    unittest.main()
