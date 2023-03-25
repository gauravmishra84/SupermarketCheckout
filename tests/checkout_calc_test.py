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
        }

    def test_valid_item(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        checkout.scan("A")
        self.assertEqual(checkout.items, {'A':1})
        
    def test_invalid_item(self):
        checkout = calc.SupermarketCheckout(self.pricing_rules)
        self.assertRaises(ValueError)

            
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
        

if __name__ == "__main__":
    unittest.main()