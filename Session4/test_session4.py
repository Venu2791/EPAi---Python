import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import cmath
import decimal
from decimal import Decimal

CONTENT_CHECK = [
    '__and__', 
    '__or__', 
    '__repr__', 
    '__str__', 
    '__add__', 
    '__eq__', 
    '__float__', 
    '__ge__', 
    '__gt__', 
    '__invert__', 
    '__le__', 
    '__lt__', 
    '__mul__', 
    '__sqrt__', 
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_class_methods():
    value = random.choice([1,0,-1])
    s = session4.Qualean(value)
    for i in CONTENT_CHECK:
        assert i in dir(s), 'All Functions not used!'

def test_add_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__add__(s2)) == s+s2, f"Your program returned wrong addition"

def test_and_function():
    for _ in range(50):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)        
        assert (s.__and__(s2)) == s&s2, f"Your program returned wrong and"

def test_or_function():
    for _ in range(50):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)        
        assert (s.__or__(s2)) == s|s2, f"Your program returned wrong or"

def test_mul_100_q_function():
    for _ in range(50):
        value = random.choice([-1,0,1])
        q = session4.Qualean(value)
        sum= 0
        for i in range(100):
            sum=sum+q.__decimal__()
        assert (sum) == q.__decimal__()*100, f"q + q + q ... 100 times <> 100 * q"

def test_million_q_function():
    sum = 0
    for _ in range(1000000):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        sum = sum + s.__decimal__()
        assert math.isclose(sum,0,rel_tol=1e3), f"sum of 1 million different is not close to zero"

def test_eq_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__eq__(s2)) == (s == s2), f"Your program returned wrong == comparison"

def test_greater_than_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__gt__(s2)) == (s>s2), f"Your program returned wrong > comparison"

def test_greater_than_eq_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__ge__(s2)) == (s>=s2), f"Your program returned wrong >= comparison"

def test_less_than_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__lt__(s2)) == (s<s2), f"Your program returned wrong < comparison"

def test_less_than_eq_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__le__(s2)) == (s<=s2), f"Your program returned wrong <= comparison"

def test_mul_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        assert (s.__mul__(s2)) == s*s2, f"Your program returned wrong multiplication"

def test_invert_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        assert (s.__invert__()) == ~s, f"Your program returned wrong invert"

def test_float_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        assert (type(s.__float__())) == float, f"Your program returned wrong float conversion"

def test_sqrt_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        assert (s.__sqrt__()) == cmath.sqrt(s), f"Your program returned wrong sqrt"

def test_sqrt_and_decimalsqrt_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        sqrt_with_complex_num = s.__sqrt__()
        sqrt_fun = round(Decimal(sqrt_with_complex_num.real),10)
        if(sqrt_with_complex_num.real>0):
            decimal_sqrt = round(s.__decimal__().sqrt(),10)
            assert (sqrt_fun) == decimal_sqrt, f"Your program returned wrong sqrt. Sqrt of positive number derived from __sqrt__ function is not the same as Decimal(q).sqrt"

def test_bool_comparison_function():
    for _ in range(50):
        value = random.choice([1,0,-1])
        s = session4.Qualean(value)
        assert (s.__bool__()) == bool(s), f"Your program returned wrong bool"

def test_or_short_circuit():
    for _ in range(50):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value) 
        if bool(s) == True:
            assert (s.__or__(s2)) == True, f"Your program returned wrong or"
            assert (s.__or__()) == True, f"Your program returned wrong or"
            assert (s.__and__()) == False, f"Q2 not defined"
        else:
            assert (s.__or__()) == False, f"Q2 not defined"
            assert (s.__and__(s2)) == False, f"Your program returned wrong and"
            assert (s.__and__()) == False, f"Your program returned wrong and"

def test_input():
    with pytest.raises(ValueError):
            session4.get_input(2)