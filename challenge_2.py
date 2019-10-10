# -----------------------------------------------------------------------------------
# CHALLENGE 2 - read the code in 'advanced_functions' first
# --------------------------------------------------------
#
# It is January 2011 and the rate of VAT in the UK is increasing from 17.5% to 20%
#
# To help out busy shop owners figure out the new prices of goods I have created
# an amazing class called TaxTron to calculate final prices at the old and new
# tax rate. But I didn't finish it :(
#
# - Add a function to the class below called 'calculate' that
#   works out a final price at different rates of input tax 
#
# - Add a second function called 'print' that nicely outputs the base price and the
#   final price after tax, both with appropriate labels.
#
# Hints:
#
# - To display a floating point number rounded to two decimal places you
#   can use; "{0:.2f}".format(yourFloatingPointNumber)
#
# - I've called the functions for you to show the expected use. Try creating
#   a taxTron2 with a different base price and call the functions on it again.
# ------------------------------------------------------------------------------------


class TaxTron:

    def __init__(self, base_price):
        self.base_price = base_price
        self.final_price = base_price
    

tax_tron_1 = TaxTron(8.50)
tax_tron_1.calculate(0.175)
tax_tron_1.print()

# tax_tron_2.calculate(0.2)
# tax_tron_2.print()
