import numpy as np
class NeuralNetwork:
    def __init__(self, layers, sizes):
        self.layers = layers
        self.sizes = [size + 1 for size in sizes]
        self.sizes[-1] -= 1
        self.weights = [np.random.randn(y, x) for x, y in zip(self.sizes[:-1], self.sizes[1:])]

    @staticmethod
    def relu(z):
        return np.maximum(0, z)

    def backprop(self, X, y, eta):
        # Forward pass
        a = [X]
        for w in self.weights:
            a.append(self.relu(w @ a[-1]))
        # Backward pass

