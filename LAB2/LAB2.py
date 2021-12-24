#########################################
##      LAB 2
##      3 INPUTS PURCHASE AND SELL STOCK
##      Author: DeonDre White
##      Version: 1.0
##
#########################################

numShares = int(input('How many shares are you purchasing: ')) #the number of shares purchaes
purPrice = float(input('What is the purchase price for the stock: '))  #purchase price of the stocks
salePrice = float(input('What is the price of the stock when you sold it: ')) #price of stock when sold

purchase_total = numShares * purPrice
sale_total = salePrice * numShares

purCommission = (numShares * purPrice) * .03 #Stockbroker commission for purchase stock 3%
sellCommission = (salePrice * numShares) * .03 #stockbroker commission for sold stock 3%

pur_cost = purchase_total + purCommission
sell_cost = sale_total - sellCommission

net_profit = sale_total - sellCommission - ( purchase_total + purCommission)

test_sales = salePrice - sellCommission
test_purchase = purPrice + purCommission

purPrice = "{:.2f}".format(purPrice)
purchase_total = "{:.2f}".format(purchase_total)
salePrice = "{:.2f}".format(salePrice)
sale_total = "{:.2f}".format(sale_total)
purCommission = "{:.2f}".format(purCommission)
sellCommission = "{:.2f}".format(sellCommission)
net_profit = "{:.2f}".format(net_profit)



print('\nNo. of stock purchase:', numShares,
      '\nPrice for stock(Purchase)', purPrice,
      '\nTotal purchase price:',purchase_total,
      '\nPrice for stock(Sale):', salePrice,
      '\nGross profit:', sale_total,
      '\nStockbroker Purchase Commission:', purCommission,
      '\nStockbroker Sale Commission:', sellCommission,
      '\nYour net profit', net_profit)

if float(net_profit) > 0:
    print('You made a profit.')
elif float(net_profit) == 0:
    print('You broke even')
else:
    print('You lose money')
