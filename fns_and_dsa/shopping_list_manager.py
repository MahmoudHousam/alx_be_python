def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item_added = input("Enter the item to add: ")
            shopping_list.append(item_added)
        elif choice == "2":
            item_removed = input("Enter the item to remove: ")
            shopping_list.append(item_removed)
        elif choice == "3":
            print("Your shopping list: ")
            for i in shopping_list:
                print(i)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
