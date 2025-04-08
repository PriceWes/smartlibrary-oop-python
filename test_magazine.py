from magazine import Magazine

mag = Magazine("Python for All", "van ", 2020)

print(mag.get_details())
print(mag.borrow())   #Overides the original method