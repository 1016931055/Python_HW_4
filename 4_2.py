from fractions import Fraction
an,ad=map(int,input().split())
a = Fraction(an,ad)
bn,bd=map(int,input().split())
b = Fraction(bn,bd)
cn,cd=map(int,input().split())
c = Fraction(cn,cd)
print(f'{b/a + b/(a+c) - c/(c-a) :.4f}')
