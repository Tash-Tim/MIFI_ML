# from sympy import FiniteSet, Union
# from sympy.codegen.cnodes import union
# import  numpy as np

# l1 = {1, 3, 7, 10}
# l2 = {9, 7, 1}
# l3 = l1.union(l2)
# l4 = l1 | l2
# print(l1)
# print(l2)
# print(l3)
# print(l3)
# print()
#
# l1_s = [1, 3, 7, 10]
# l2_s = [9, 7, 1]
# a = FiniteSet(*l1_s)
# b = FiniteSet(*l2_s)
# print(Union(a, b))
# print()
#
# from sympy import ConditionSet, Eq, Symbol, Interval
# x=Symbol('x')
# s=ConditionSet(x, Eq(x**2-5*x,0), Interval(2,9))
# print(s)

# prog = {'bennet@xyz.com', 'darcy@abc.com', 'margaret@xyz.com', 'pa@hhh.com', 'marimari@xyz.com', 'mallika@yahoo.com',
#         'abc@xyz.com', '0071235@gmail.ru'}
# ml = {'marimari@xyz.com', 'darcy@abc.com', '0071235@gmail.ru', 'darcy@abc.com', 'petr44@xyz.com', 'katrin@ya.com'}
#
# inter = prog.intersection(ml)
# print(len(inter))
#
# union_all = prog.union(ml)
# print(len(union_all))
#
# sym_defer = prog.symmetric_difference(ml)
# print(len(sym_defer))

# from sympy import Symbol, solveset, Eq
# x = Symbol("x")
# a = solveset(Eq(x*x+2*x-8, 0), x)
# print(a)

# from sympy import Symbol, S, sin #импортируем нужные функции для обозначения переменных
# from sympy.calculus.util import function_range #импортируем функцию для поиска области значений
# x = Symbol("x")
# f = 3/(x**2-10)
# print(function_range(f, x, S.Reals))

# from sympy import symbols
# x, y = symbols('x y')
# f = (x**3 + y)/(x**2-1*y)
# result = f.subs(x, 1)
# print(result)


# from sympy import Symbol
# x = Symbol("x")
# expr = (x**3)/(x**2-1)
# print(expr.diff(x))

# from sympy import solveset, Eq, Symbol
# x = Symbol('x')
# expr = (x**3 + x)/(x**2-1)
# y = expr.diff(x)
# res = solveset(Eq(y, 0), x)
# print(res)

from sympy import Symbol
x = Symbol('x')
f = x**3/2*(x+5)**2
print(f.diff(x))

