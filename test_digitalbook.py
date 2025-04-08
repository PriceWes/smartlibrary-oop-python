from digitalbook import DigitalBook

ebook = DigitalBook("Python for All", "van", 2020, 75)

print(ebook.get_details())
print(ebook.stream())  #unique to digital books
print(ebook.borrow())  #Overides the original method