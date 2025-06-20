from mathematic import add, multiply, substract, divide  # esto el 19/06 implantacion devops y demas.

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, 20) == 30

def test_multiply():
    assert multiply(2,5) ==10
    assert multiply(3,5) ==15
    assert multiply(0,5) ==0
    print("multiply")

def test_substract():
    assert substract(10,5) ==5
    assert substract(45,5) ==40
    assert substract(10,5) ==5

def test_divide():
    assert divide(20,5) ==4
    assert divide(750,5) ==150
    assert divide(0,5) ==0
    
test_multiply()