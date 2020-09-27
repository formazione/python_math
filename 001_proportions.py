# python_math 1
# proportions

class Prop:
    def __init__(self, prop):
        '''This is how you put the argument e1 : e2 = m1 : m2 
        ie: 12 : 3 = 36:9
        '''
        self.proportion = prop
        prop = prop.replace("=", ":")
        self.prop = e1, m1, m2, e2 = prop.split(":")
        for n, x in enumerate(self.prop):
            if x.strip() == "x":
                self.prop[n] = None
            else:
                self.prop[n] = int(x)
        e1, m1, m2, e2 = self.prop
        self.e1 = e1
        self.e2 = e2
        self.m1 = m1
        self.m2 = m2

    def calculate_x(self):
        "Call this from the istance to find the incognito"
        print(f"The result of '{self.proportion}' is ", end="")
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



p1 = Prop("12 : 3 = 36 : x")
print(p1.calculate_x())
