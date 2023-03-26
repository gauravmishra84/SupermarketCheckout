## Problem Statement

The is the implementation for the given problem statement of creating a checkout function for a Supermarket and calculate total price for a cart considering any special offers.

### Assumptions

Presuming that the pricing list is available as an input for a shopping cart checkout to be initiated.
Also, that we are just creating a functionality to cater total price payable at checkout and the unit and special prices aren't changing while the total price calculation happens. The solution is currently considering just one instance of the checkout at a Supermarket till. We are not creating any separate product inventory and any functionality for Inventory management and offer price/validity updates.

### Environment and Structure

The code is written using the version `python 3.10.4`

The implementation is structured as a module under `src` and called `checkout_calc`. All the test cases are in the `tests` directory.

### Running in Terminal

To run the code directly in Terminal, we would need do below steps.

`import sys`
`sys.path.append('./src')`
`from checkout import checkout_calc`

And now once the module is imported, we could potentially create the object and a dummy pricing for some items:

`pricing_rules =  { `
           ` "A": {"price": 50, "special_price": {"quantity": 3, "price": 130}},` 
           ` "B": {"price": 30, "special_price": {"quantity": 2, "price": 45}},`
           ` "C": {"price": 20},`
           ` "D": {"price": 15},`
        `}`

`checkout = calc.SupermarketCheckout(pricing_rules)`

`checkout.scan("A")`

`checkout.scan("B")`

`checkout.scan("C")`

`checkout.scan("D")`

`print(checkout.total())`
 This should result in 115.


### Running the Unit Test Cases
 
 To run the Unit Tests from terminal, simply navigate to the root folder and run a test discovery using this command:

 ` python -m unittest discover`

 This will search for unit tests and add the appropriate directory in `sys.path`

 Then simply call the tests with:

 `python -m unittest tests.checkout_calc_test`

### Packaging Configuration

Added the setuptools based packaging configuration defining how the the solutions could be packaged and converted into a wheel distribution.

Additionaly a pyproject.toml file is also provided to showcase how the packaging could be done using pyproject.toml. It could be used with poetry to manage all configuration in just one file, which makes it easy to build and deliver.

## Further improvement and scaling of the solution

 To scale this solution further, in a distributed computing environment, we can run multiple instances of the SupermarketCheckout class and distribute the load among them, possibly using a load balancer. The pricing rules can be passed to each instance as an argument, so they can be customized for each location or store. We can also have a more defined storage and management for inventory and pricing rules targeting specific regions and stores. The solution could be organized in a microservices architecture running in a container orchestrated tool like kubernetes and serving a no of simultaneous requests.

