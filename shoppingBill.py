def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst

def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total
    

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_bill = total - discount

    
    return final_bill


a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_bill = calculateDiscountedBill(a, b, c, d, e)

print("Shopping Bill")
print("--------------------")
print("Electronics:", calculateElectronicsGST(a, b))
print("Fashion:", calculateFashionGST(c, d))
print("Food:", calculateFoodGST(e))
print("--------------------")
print("Total after GST:", round(total, 2))
print("Discount:", round(discount, 2))
print("Final payable amount:", round(final_bill, 2))
