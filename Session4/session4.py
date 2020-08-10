import decimal
from decimal import Decimal
import random
import cmath

class Qualean():
    # Constructor 
    def __init__(self,real_state):
        super().__init__()
        self.im_state = round(Decimal(real_state) * Decimal(random.uniform(-1,1)),10)
    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Qualean({0})'.format(self.im_state)
    # For call to str(). Prints readable form 
    def __str__(self): 
        return '%s' % (self.im_state)
    def __and__(self, other=None):
        if(bool(self.im_state) is False):
            return False
        elif(other is None):
            return False
        else:      
            return bool(self.im_state and other.im_state)
    def __or__(self, other=None):
        if(bool(self.im_state) is True):
            return True
        elif(other is None):
            return False
        else:
            return bool(self.im_state or other.im_state)
    def __gt__(self, other):
        return self.im_state > other.im_state
    def __lt__(self, other):
        return self.im_state < other.im_state
    def __ge__(self, other):
        return self.im_state >= other.im_state
    def __le__(self, other):
        return self.im_state <= other.im_state
    def __eq__(self, other):
        return self.im_state == other.im_state
    def __add__(self, other):
        return self.im_state + other.im_state
    def __float__(self):
        return float(self.im_state)
    def __mul__(self,other):
        return self.im_state * other.im_state
    def __sqrt__(self):
        return cmath.sqrt(self.im_state)
    def __bool__(self):
        return self.im_state!=0
    def __invert__(self):
        return self.im_state * -1
    def __decimal__(self):
        return self.im_state

def get_input(num):
    if(num not in [-1,0,1]):
        raise ValueError("Enter 0 or 1 or -1")
    q1 = Qualean(num)
    q2 = Qualean(num)
    pass