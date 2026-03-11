class Bag:
    def __init__(self, CAPACITY: int) -> None:
        # precondition: None
        # postcondition: The Bag starts empty

        self.CAPACITY: int = CAPACITY
        self.data: list[int] = []
        self.used: int = 0

    def insert(self, new_entry: int) -> None:
        # precondition: Bag is not full
        # postcondition: A new copy of new_entry is added to the Bag
        
        if self.full():
            print("The bag is full!")
            return

        self.used += 1
        self.data.insert(self.used, new_entry)

    def occurrence(self, entry: int) -> int:
        # precondition: None
        # postcondition: Returns the number of occurrences of the entry element in the Bag
        
        total: int = 0
        for element in self.data:
            if element == entry:
                total += 1
        
        return total
    
    def remove(self, entry: int) -> None:
        # precondition: None
        # postcondition: Removes an occurrence of the entry element from the Bag. If the element does not exist, the Bag remains unchanged
        
        index: int = 0
        for i, element in enumerate(self.data):
            if element == entry:
                index = i
        
        self.used -= 1
        self.data.pop(index)
    
    def full(self) -> bool:
        # precondition: None
        # postcondition: Returns true if the Bag is full; false otherwise
        
        return self.used == self.CAPACITY

    def size(self) -> int:
        # precondition: None
        # postcondition: Returns the number of items in the Bag
        
        return self.used

    def print_bag(self) -> None:
        # precondition: None
        # postcondition: Print Bag contents 
        
        print("<[", end="")
        for i, element in enumerate(self.data):
            print(element, end="")
            if i != len(self.data) - 1:
                print(", ", end="")
        print("]>")