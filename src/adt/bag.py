class Bag:
    def __init__(self, CAPACITY: int) -> None:
        # precondition: None
        # postcondition: The Bag starts empty
        self.CAPACITY: int = CAPACITY
        self.data: list[int] = []

    def insert(self, new_entry: int) -> None:
        # precondition: Bag is not full
        # postcondition: A new copy of new_entry is added to the Bag
        
        if self.full():
            print("The bag is full!")
            return

        self.data.append(new_entry)

    def occurrence(self, entry: int) -> int:
        # precondition: None
        # postcondition: Returns the number of occurrences of the entry element in the Bag
        
        return self.data.count(entry)
    
    def remove(self, entry: int) -> None:
        # precondition: None
        # postcondition: Removes an occurrence of the entry element from the Bag. If the element does not exist, the Bag remains unchanged
        
        self.data.remove(entry)
    
    def full(self) -> bool:
        # precondition: None
        # postcondition: Returns true if the Bag is full; false otherwise
        
        return len(self.data) == self.CAPACITY

    def size(self) -> int:
        # precondition: None
        # postcondition: Returns the number of items in the Bag
        
        return len(self.data)

    def print_bag(self) -> None:
        # precondition: None
        # postcondition: Print Bag contents 
        
        print("<[", end="")
        for i, element in enumerate(self.data):
            print(element, end="")
            if i != len(self.data) - 1:
                print(", ", end="")
        print("]>")