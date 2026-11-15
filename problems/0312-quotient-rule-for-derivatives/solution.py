import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def evaluate(coeffs, x):
        n = len(coeffs)
        value = 0
        derivative = 0

        for i, coeff in enumerate(coeffs):
            power = n - i - 1

            value += coeff * (x ** power)

            if power > 0:
                derivative += power * coeff * (x ** (power - 1))
            
        return value, derivative

    g, g_prime = evaluate(g_coeffs, x)
    h, h_prime = evaluate(h_coeffs, x)

    return (g_prime * h - g * h_prime) / (h ** 2)