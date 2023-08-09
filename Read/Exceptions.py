# consider an automation that we do to add items in cart

ItemsInCart = 2

if ItemsInCart != 2:
    #raise Exception("products cart count not matching")
 pass

assert (ItemsInCart == 2)

#try,catch
try:
    with open('Text.txt', 'r') as  reader:
        reader.read()
except:
    print("Reached here because there is failure")


try:
    with open('Text.txt', 'r') as  reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Cleaning up the resources")

