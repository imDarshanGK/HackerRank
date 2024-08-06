# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
r=input()
abs_value=abs(complex(r))
print(abs_value)
phase_value=cmath.phase(complex(r))
print(phase_value)
