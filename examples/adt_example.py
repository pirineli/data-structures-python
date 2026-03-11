from src.adt.bag import Bag

def main():
    # Create a new Bag
    bag = Bag(20)

    # Insert elements
    bag.insert(10)
    bag.insert(20)
    bag.insert(10)
    bag.insert(30)

    # Print bag contents
    print("Bag contents:")
    bag.print_bag()

    # Check size
    print("Size of bag:", bag.size())

    # Count occurrences of an element
    print("Occurrences of 10:", bag.occurrence(10))

    # Remove an element
    bag.remove(20)

    print("Bag after removing 20:")
    bag.print_bag()

    # Fill the bag to test capacity
    for i in range(17):
        bag.insert(i)

    print("Is the bag full?", bag.full())

if __name__ == "__main__":
    main()


"""
### Expected Output (example)

Bag contents:
<[10, 20, 10, 30]>
Size of bag: 4
Occurrences of 10: 2
Bag after removing 20:
<[10, 10, 30]>
Is the bag full? True

"""