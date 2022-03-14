from string import Template

def Main():
    cart=[]
    cart.append(dict(item='coke',price=8, quantity=2))
    cart.append(dict(item='cake', price=12,quantity=1))
    cart.append(dict(item='fish', price =22, quantity =4))

    t=Template('$quantity x $item = $price')
    print(cart)
    print(Template('$quantity x $item = $price').substitute(cart[1]))
    total= 0
    print('cart:')
    for data in cart:
        print(t.substitute(data))
        total+= data['price']
    print('total: '+str(total))

Main()