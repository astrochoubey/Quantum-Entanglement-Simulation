import numpy as np

# ==========================================
# 1. COMPLEX NUMBERS
# ==========================================

z = 3 + 4j

print("Complex number:", z)
print("Complex conjugate:", np.conjugate(z))
print("Modulus:", abs(z))
print("Modulus squared:", abs(z)**2)

# To find the modulus of \(z = 3 + 4i\):
# 1. Square the real part: \(3^2 = 9\)
# 2. Square the imaginary part: \(4^2 = 16\)
# 3. Add them together and take the square root: \(\sqrt{9 + 16} = \sqrt{25} = 5\)

# ==========================================
# 2. QUANTUM BASIS VECTORS
# ==========================================

zero = np.array([1, 0], dtype=complex)
one = np.array([0, 1], dtype=complex)

print("\nBasis vectors:")
print("|0> =", zero)
print("|1> =", one)
