import sympy as sp

# Define the spherical coordinates and the Laplace equation
r, theta, phi = sp.symbols('r theta phi', real=True, positive=True)
psi = sp.Function('psi')(r, theta, phi)
laplace_eq = sp.Eq(1/r**2 * sp.diff(r**2 * sp.diff(psi,r), r) - 1/r**2 * psi + 1/(r**2 * sp.sin(theta)) * sp.diff(sp.sin(theta) * sp.diff(psi, theta), theta) + 1/(r**2 * sp.sin(theta)**2) * sp.diff(psi, phi, 2), 0)

# Solvr the Laplacian equation for Phi
solutions = sp.pdsolve(laplace_eq, psi)

# Display the solutions
for solution in solutions:
    print(f'Solutions {solutions.index(solutions) + 1}:')
    sp.pprint(solutions.rhs)
    print()