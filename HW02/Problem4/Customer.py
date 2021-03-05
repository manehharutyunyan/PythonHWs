import Productcheck as p

def buy(product,num,price):
    if p.check(product,num):
        print("You bought %s and spent %s ." % (product, num*price))
    else:
        print('Sorry! We are out of this product.')
        
if __name__ == '__main__':
    buy('candy',5,20)
        