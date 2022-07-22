#Create a shoping cart,customer can pick any number of products
#when customer inputEND the shoping ends,
#customer is told how many items in cart and is ask to check out
# if customer inpput -1 one system tell customer how many items left in the cart
#Ask customer to check out.
store = []
user_cart = True
while user_cart:
    cart = input("pick items into cart: ")
    if cart == str(-1):
      break
    elif cart == "end":
     break
    else:
        store.append(cart)
        
    
print(f"you have {len(store)} items on your cart")
print(store)
remove_product = True
answer = input("would you like to remove an item from the cart ?:")
if answer == "yes":
    while remove_product:
        product = input("which item would you like to remove ?:")
        if product == str(-1):
            break
        elif product == "end":
            break
        else:
            store.remove(product)
    
    print(f"you have {len(store)} items on your cart")
    print(store)
    

else:
    print(f"you have {len(store)} items on your cart")

    
