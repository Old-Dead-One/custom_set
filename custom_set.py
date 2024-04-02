class CustomSet:
    def __init__(self):
        self.item = []

    def add(self, item):
        if item in self.item:
            print("Item already in set.")
        else:
            self.item.append(item)

    def remove(self, item):
        try:
            self.item.remove(item)
        except ValueError:
            print("Item not in set, moving on.")

    def as_list(self):
        return self.item

    def clear(self):
        self.item = []

def main():

    my_set = CustomSet()

    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 3")
    my_set.add("item 4")
    my_set.add("item 5")
    my_set.add("item 6")
    print (my_set.as_list())

    my_set.remove("item 1")
    my_set.remove("item 3")
    print (my_set.as_list())
        
    print (my_set.as_list)

    my_set.clear()
    print (my_set.as_list())


