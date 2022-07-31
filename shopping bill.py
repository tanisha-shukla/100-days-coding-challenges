print("-"*90)
print("                 Y.A.M.C.A  STORE                       ")
print("-"*90)
name =input("ENTER A COUSTOMER NAME :")
cost =eval(input("ENTER THE COST  :"))
quantity =int(input("ENTER THE QUANTITY    :"))
amount = cost*quantity  
gst =round((amount*12)/100 ,2,)
total =amount+gst
print("-"*90)
print("COUSTOMER NAME  :",name)
print("TOTAL AMOUNT OF PRODUCT THAT YOU ARE PURCHASED :","Rs.",amount)
print("TOTAL GST APPLIED ON YOUR PRODUCTS :",gst ,"%")
print("TOTAL AMOUNT TO BE PAID :","Rs.",total)
print("-"*90)
if total <1000:
    discountprice =0
elif total <=2000:
    discountprice =0.1*total
    print("TOTAL DISCOUNTPRICE ON YOUR PRODUCT :","Rs.",round((discountprice),2))
    print("YOUR TOTAL AMOUNT AFTER THE DISCOUNTCOUPON APPLIED :","Rs.",total - round((discountprice),2))
else :
    discountprice =0.2*total
    print("TOTAL DISCOUNTPRICE ON YOUR PRODUCT :","Rs.",round((discountprice),2))
    print("YOUR TOTAL AMOUNT AFTER THE DISCOUNTCOUPON APPLIED :","Rs.",total - round((discountprice),2))
print("-"*90)
print("DAY 04 COMPLETED :)" )  

