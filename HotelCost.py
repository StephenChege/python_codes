"""There are four parameters: price  is the hotel charge for one night, days is the number of days to stay
at the hotel, tax is the percentage of tax applied to the total price(but not to the fee), and fee is an additional
tourist fee per night after tax is calculated. Consider the following:
 1.Total price before tax and fee is the charge for one night times the number of days stayed at the hotel.
 2. Tax is percentage charge applied to the total price(but not the fee).
 3.The fee is an extra tourist charge added per night after tax is calculated. However, no tourist fee is applied for a
 stay of a week or more and haLf of the tourist  fee applies for a stay of 4-6 days."""
#The function below calculates the cost of a hotel room for one or more nights

def hotelStay(price, days, tax, fee):
    total_price = price * days
    tax_paid = (tax/100) * total_price
    if days >= 7:
        fee = 0
    elif days in range(4,7):
        fee = (fee/2) * days
    else:
        fee = fee * days

    grand_total = total_price + tax_paid + fee
    return grand_total

#Example
print(hotelStay(100,8,10,20))