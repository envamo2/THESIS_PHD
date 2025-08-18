import numpy as np
import matplotlib.pyplot as plt

# Activations and their derivatives
def relu(x):
    return np.maximum(0, x)

def relu_deriv(x):
    return np.where(x > 0, 1, 0)

def leaky_relu(x, alpha=0.3):
    return np.where(x > 0, x, alpha * x)

def leaky_relu_deriv(x, alpha=0.3):
    return np.where(x > 0, 1, alpha)

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

def gelu_deriv(x):
    # Approximate derivative of GELU (analytic is complex)
    tanh_term = np.tanh(0.797885 * (x + 0.044715 * x**3))
    sech2_term = 1 - tanh_term**2
    return 0.5 * (1 + tanh_term) + 0.5 * x * sech2_term * (
        0.797885 + 0.1070322243 * x**2
    )

# Plot settings
x = np.linspace(-5, 5, 500)
plt.figure(figsize=(12, 8))

# ReLU
plt.plot(x, relu(x), label="ReLU", color="blue")
plt.plot(x, relu_deriv(x), "--", label="ReLU Derivative", color="blue")

# Leaky ReLU
plt.plot(x, leaky_relu(x), label="Leaky ReLU", color="green")
plt.plot(x, leaky_relu_deriv(x), "--", label="Leaky ReLU Derivative", color="green")

# GELU
plt.plot(x, gelu(x), label="GELU", color="red")
plt.plot(x, gelu_deriv(x), "--", label="GELU Derivative", color="red")

# Style
plt.xlabel("x", fontsize=14)
plt.ylabel("Activation / Derivative", fontsize=14)
plt.title("Activation Functions and Their Derivatives", fontsize=16)
plt.axhline(0, color="gray", lw=1, linestyle=":")
plt.axvline(0, color="gray", lw=1, linestyle=":")
plt.legend(fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("activation_functions.png")
plt.show()
