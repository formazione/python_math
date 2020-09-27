from proportions import Prop


class Percent(Prop):
    def __init__(self, base, percent):
        self.base = base
        self.percent = percent
        prop = f"100 : {percent} = {self.base} : x"
        super(Percent, self).__init__(prop)

    def solve(self):
        return self.base * self.percent / 100

    def print(self):
        print("The solutions is:")
        print(self.solve())
        print(self.calculate_x())

# First the price, then the percent
x = Percent(3000, 20)
x.print()