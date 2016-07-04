class aa:
    w = 10
    def __init__(self):
        self.x = 11
        self.y = 12

    def process(self):
        aa.w =30

    def add(self):
        return self.x + self.y

    def sum(self):
        return aa.w

# a = aa()
# print a.add()
# print a.sum()

class t(object):
    x = 1
    def t1(self):
        global x
        x =2
        print x
    print x
# t().t1()
# print t.x


class T(object):
    a = None

    def t1(self):
        self.a = 9

    def t2(self):
        print self.a

T().t1()
T().t2()