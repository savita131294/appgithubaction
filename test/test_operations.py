from src.math_operations import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(4,8)==12

def test_sub():
    assert subtract(8,4)==4
    assert subtract(9,6)==3
    assert subtract(10,2)==8
    assert subtract(4,5)==-1