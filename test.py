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
    print(my_set.as_list())

    my_set.remove("item 2")
    my_set.remove("item 6")
    print(my_set.as_list())

    my_set.as_list()  # This line doesn't do anything
    print(my_set.as_list())

    my_set.clear()  # You need to call the clear method using ()
    print(my_set.as_list())

if __name__ == "__main__":
    main()

