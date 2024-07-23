import time


class Delivery:
    service_charge = 1.15
    extras = "sweet pop corn"

    def __init__(self) -> None:

        self.menu = {
            1: ["coconut curry", 7.50],
            2: ["spicy tofu", 5.25],
            3: ["veg noodles", 8.75],
        }
        self.order = []

    def choose_in_menu(self):
        for i in range(1, len(self.menu) + 1):
            print(i, self.menu[i][0] + f": ${str(self.menu[i][1])}")

        print("Please enter the dish numbers you'd like")
        while True:
            self.food = input("")
            try:
                num = abs(int(eval(self.food)))

            except:
                print("Please enter a valid number")
                continue

            if self.food == "" or num == 0 and num < 4:
                print("Thank you, Your order is complete")
                break
            elif num >= 4:
                print("Please enter a number between 1 and 3")
            else:
                self.order.append(self.menu[num][1])
        print(self.order)

    def Pay(self):
        total = sum(self.order) * Delivery.service_charge
        print(f"That will be a total of ${str(round(total, 2))}")
        if total > 30:
            print(f"We've also included a free {Delivery.extras}")
        else:
            None

    def decision_time(self, func):
        print("How long does it take for the customer to choose?")

        def customer_time(*args, **kwargs):
            start_time = time.time()
            dec1 = func()
            end_time = time.time()
            duration = round(((end_time - start_time) * 1000) / 1000, 2)
            print(f"Time taken to order: {duration} seconds")
            return dec1

        return customer_time


if __name__ == "__main__":
    try:
        df = Delivery()
        # df.choose_in_menu()
        # df.Pay()
        dex = df.decision_time(df.choose_in_menu)
        dex()
    except KeyboardInterrupt:
        print("\nHope to see you soon! Bye!")
