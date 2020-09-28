from proportions import Prop


class Percent(Prop):
    def __init__(self, base, percent):
        self.base = base
        self.percent = percent
        prop = f"100 : {percent} = {self.base} : x"
        super(Percent, self).__init__(prop)
<<<<<<< HEAD
        self.print()
=======
>>>>>>> 5782f8dc5bb3092a6084bc4f87f9daeb5f4b8c15

    def solve(self):
        return self.base * self.percent / 100

    def print(self):
<<<<<<< HEAD
        print("You find the x this way:")
        print(f"x = {self.base} * {self.percent} / 100 = {self.solve()}")


# First the price (for example), then the percent
Percent(3000, 20)
=======
        print("The solutions is:")
        print(self.solve())
        print(self.calculate_x())

# First the price, then the percent
x = Percent(3000, 20)
x.print()
>>>>>>> 5782f8dc5bb3092a6084bc4f87f9daeb5f4b8c15
