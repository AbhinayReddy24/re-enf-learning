

def activtion_function(weighted_sum_with_bias):
    if weighted_sum_with_bias > 0:
        return 1
    return 0


def perceptron(inputs, weights):

    bias = 0.4
    weighted_sum = 0
    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]
    weighted_sum_with_bias = weighted_sum + bias

    return activtion_function(weighted_sum_with_bias)


def correct_weights(input_to_relu_greater_than_zero, inputs, weights):
    corrected_weights = []
    precent_correction = 0.1

    # check for the correctnes of individual weights
    for i in range(len(inputs)):
        inputs_multiplied_by_weights = 0
        current_weight_value = weights[i]
        expected_weight = 0
        input_value_of_current_weight = inputs[i]
        for j in range(len(inputs)):
            if i == j:
                input_value_of_current_weight = inputs[j]
                continue
            inputs_multiplied_by_weights += inputs[j] * weights[j]
        if (input_value_of_current_weight != 0):
            expected_weight = inputs_multiplied_by_weights / \
                input_value_of_current_weight
        else:
            expected_weight = inputs_multiplied_by_weights
        # build condition to skip the weight if it is already correct
        # if both are negative or both are positive, then the weight is correct
        print('current_weight_value', current_weight_value,
              'expected_weight', expected_weight)
        if not input_to_relu_greater_than_zero:
            if current_weight_value <= expected_weight:
                corrected_weights.append(current_weight_value)
            else:
                corrected_weight = expected_weight - precent_correction * expected_weight
                corrected_weights.append(corrected_weight)
        else:
            if current_weight_value >= expected_weight:
                corrected_weights.append(current_weight_value)
            else:
                corrected_weight = expected_weight + precent_correction * expected_weight
                corrected_weights.append(corrected_weight)
    print('corrected_weights', corrected_weights)
    return corrected_weights


# train_data structure = [ {inputs: [1, 1, 1], output:1}, ...]
def train_percepton(training_data):
    weights = [0.1, 0.1, 0.1]
    for data in training_data:
        predicted_value = perceptron(data['inputs'], weights)
        actual_value = data['output']
        input_to_relu_greater_than_zero = None
        if (predicted_value == actual_value):
            continue
        elif (predicted_value > actual_value):
            # in this case, input to relu should have been less than 0
            input_to_relu_greater_than_zero = True
        else:
            # in this case, input to relu should have been greater than 0
            input_to_relu_greater_than_zero = False

        corrected_weights = correct_weights(
            input_to_relu_greater_than_zero, data['inputs'], weights)
        weights = corrected_weights

    return weights


if __name__ == '__main__':
    training_data = [
        {'inputs': [1, 1, 1], 'output': 1},
        {'inputs': [1, 1, 0], 'output': 1},
        {'inputs': [1, 0, 1], 'output': 1},
        {'inputs': [1, 0, 0], 'output': 0},
        {'inputs': [0, 1, 1], 'output': 1},
        {'inputs': [0, 1, 0], 'output': 0},
        {'inputs': [0, 0, 1], 'output': 0},
        {'inputs': [0, 0, 0], 'output': 0},
    ]

    # Train perceptron
    trained_weights = train_percepton(training_data)
    print("Trained weights:", trained_weights)

    # Test the perceptron with new inputs
    inputs = [1, 1, 1]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [1, 1, 0]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [1, 0, 1]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [1, 0, 0]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [0, 1, 1]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [0, 1, 0]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [0, 0, 1]
    print("Prediction:", perceptron(inputs, trained_weights))

    inputs = [0, 0, 0]
    print("Prediction:", perceptron(inputs, trained_weights))
    inputs = [1, 1, 1]
    print(perceptron(inputs, trained_weights))
    inputs = [1, 1, 0]
    print(perceptron(inputs, trained_weights))
    inputs = [1, 0, 1]
    print(perceptron(inputs, trained_weights))
    inputs = [1, 0, 0]
    print(perceptron(inputs, trained_weights))
    inputs = [0, 1, 1]
    print(perceptron(inputs, trained_weights))
    inputs = [0, 1, 0]
    print(perceptron(inputs, trained_weights))
    inputs = [0, 0, 1]
    print(perceptron(inputs, trained_weights))
    inputs = [0, 0, 0]
    print(perceptron(inputs, trained_weights))
