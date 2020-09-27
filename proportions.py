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

    def calculate_x(self):
        "Call this from the istance to find the incognito"
        print(f"The result of '{self.proportion}' is ", end="")
        # Depending on what is None (incognito), it finds it with the other 3
        if self.e1 is None:
            res = self.m1 * self.m2 / self.e2
            return res
        elif self.e2 is None:
            res = self.m1 * self.m2 / self.e1
            return res
        elif self.m1 is None:
            res = self.e1 * self.e2 / self.m2
            return res 
        elif self.m2 is None:
            res = self.e1 * self.e2 / self.m1
            return res
        print(res)

if __name__ == "__main__":
    print("This is an example")
    # First you create the istance of Prop with a string containing the proposition
    p1 = Prop("12 : 3 = 36 : x")
    # Then you get the solution with calculate_x (method of Prop class)
    print(p1.calculate_x())
    # Second example with same proportion but different incognito
    p2 = Prop("12 : x = 36 : 9")
    print(p2.calculate_x())
