import sympy as sp

# Define the spherical coordinates and the Laplace equation
r, theta, phi = sp.symbols('r theta phi', real=True, positive=True)
psi = sp.Function('psi')(r, theta, phi)
laplace_eq = sp.Eq(1/r**2 * sp.diff(r**2 * sp.diff(psi,r), r) - 1/r**2 * psi + 1/(r**2 * sp.sin(theta)) * sp.diff(sp.sin(theta) * sp.diff(psi, theta), theta) + 1/(r**2 * sp.sin(theta)**2) * sp.diff(psi, phi, 2), 0)

# Separate the Laplace equation into three parts
eq1 = laplace_eq.subs(psi, psi.func(r, theta, phi)).doit()
eq2 = laplace_eq.subs(psi, psi.func(r, theta, phi)).doit().subs(sp.Derivative(psi, phi, phi), 0)
eq3 = laplace_eq.subs(psi, psi.func(r, theta, phi)).doit().subs(sp.Derivative(psi, r), 0)

# Solve the three separated equations
solutions_r = sp.dsolve(eq1, psi.func(r, theta, phi))
solutions_θ = sp.dsolve(eq2, psi.func(r, theta, phi))
solutions_φ = sp.dsolve(eq3, psi.func(r, theta, phi))

solutions = []

for i in range(3):


# Display the solutions
for solution in solutions:
    print(f'Solutions {solutions.index(solutions) + 1}:')
    sp.pprint(solutions.rhs)
    print()