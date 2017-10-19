#testes agrupados em uma classe
class TestClass:
   def test_one(self) :
      x = 8
      assert x==9
   def test_two(self) :
      x = 1
      assert x==1
#testes unitários fora da classe
def func(x) :
   return x + 1
   
def test_answer1() : # teste da funcao func(x)
   assert func(3) == 4

def test_answer2() :
   assert func(5) == 6 # teste da funcao func(x)

def function(y) :
	return y*3

def test_func() :
	assert function(6) == 9 # teste da funcao function(y)

def test_func2() :
	assert function(1) == 3 # teste da funcao function(y)

def test_func3() :
	assert function(10) == 30 # teste da funcao function(y)

def test_func4() :
	assert function(10000) == 300000 # teste da funcao function(y)

def fun(z) :
	return z/2

def test_fun1() :
	assert fun(1) == 0 # teste da funcao fun(z)

def test_fun2() :
	assert fun(1) == 1 # teste da funcao fun(z)