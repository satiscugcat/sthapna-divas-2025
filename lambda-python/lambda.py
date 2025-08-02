"""
   In the Lambda Calculus, the only primitives are (nameless) single argument functions and variables.
   Let us define our own booleans!
"""
def id(x):
    return x

id = lambda x: x

true = lambda x: lambda y: x
false = lambda x: lambda y: y
_not = lambda b: lambda x: lambda y: b(y)(x)
ifthenelse = (lambda i: lambda t: lambda e: (i(lambda _: t)(lambda _: e))(id))

x = true
y = false
z = ifthenelse(_not(x))(y)("Hi")

def lambda_to_bool(b):
    return b(True)(False)

print(z)
pair = lambda e1: lambda e2: (lambda x: lambda y: lambda b: b(x)(y))(e1)(e2)
fst = lambda p: p(true)
snd = lambda p: p(false)

print(snd (pair ("Hi") ("Hello!")))

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))

succ = lambda n: lambda f: lambda x: f(n(f)(x))
plus = lambda n1: lambda n2: lambda f: lambda x: n1(f)(n2(f)(x))
mul = lambda n1: lambda n2: lambda f: lambda x: n1(n2(f))(x)

zz = pair(zero)(zero)
ss = lambda p: pair (snd(p)) (succ (snd(p)))
pred = lambda n: fst (n(ss)(zz))
sub = lambda n1: lambda n2: n2(pred)(n1)
iszero = lambda n: n (lambda _: false) (true)

print(ifthenelse (iszero (sub (two) (plus (one) (one))))
      ("Zero!")
      ("Not Zero!")
      )

def num_to_church(n):
    if n == 0:
        return zero
    else:
        t = (num_to_church(n-1))
        return succ(t)
    
def church_to_num(n):
    return n (lambda x: x+1) (0)

print(church_to_num(mul(two)(three)))

fix = (
    lambda f: 
    (lambda x: f(
        lambda v: x(x)(v)
    ))
    (lambda x: f(
        lambda v: x(x)(v)
    ))
)

F = (lambda f: (lambda x: (iszero(x)
                           (lambda _: one)
                           (lambda _: mul(x)(fact(pred(x)))))(id)))

fact = fix(F)

print(church_to_num(fact(num_to_church((5)))))
