from proportions import Prop


class Percent(Prop):
    def __init__(self, base, percent):
        self.base = base
        self.percent = percent
        prop = f"100 : {percent} = {self.base} : x"
        super(Percent, self).__init__(prop)

        self.print()

    def solve(self):
        return self.base * self.percent / 100

    def print(self):

        print("You find the x this way:")
        print(f"x = {self.base} * {self.percent} / 100 = {self.solve()}")


# First the price (for example), then the percent
Percent(3000, 20)


