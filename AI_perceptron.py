
# The Perceptron defines the first step into Neural Networks.
#code is written in Python

print("Will I go to the concert?")

threshold = 1.5
inputs = [1, 0, 1, 0, 1]
weights = [0.7, 0.6, 0.5, 0.3, 0.4]

sum_value = 0

for i in range(len(inputs)):
    sum_value += inputs[i] * weights[i]

print(sum_value > threshold)
