# python_math 1
# proportions

class Prop:
    def __init__(self, prop):
        '''This is how you put the argument e1 : e2 = m1 : m2 
        ie: 12 : 3 = 36:9
        '''
        print(prop)
        self.proportion = prop
        # replace = with :
        prop = prop.replace("=", ":")
        # create a list with the numbers, splitting by the ':'
        self.prop = prop.split(":")
        # converts strings into integers and x to None
        for n, x in enumerate(self.prop):
            if x.strip() == "x":
                self.prop[n] = None
            else:
                self.prop[n] = int(x)
        # memorize in memorable names the extrem and medium terms
        e1, m1, m2, e2 = self.prop
        self.e1 = e1
        self.e2 = e2
        self.m1 = m1
        self.m2 = m2
        self.calculate_x()

    def calculate_x(self):
        "Call this from the istance to find the incognito"
        # Depending on what is None (incognito), it finds it with the other 3
        if self.e1 is None:
            res = self.m1 * self.m2 / self.e2
        elif self.e2 is None:
            res = self.m1 * self.m2 / self.e1
        elif self.m1 is None:
            res = self.e1 * self.e2 / self.m2
        elif self.m2 is None:
            res = self.e1 * self.e2 / self.m1
        print(f"The result of the proportion is {res}\n")
        return res


if __name__ == "__main__":

    p1 = Prop("12 : 3 = 36 : x")
    p2 = Prop("12 : x = 36 : 9")
    # percentage proportion
    p3 = Prop("100 : 20 = 300 : x")
