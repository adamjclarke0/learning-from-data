from pla_utils import *

def test_horizontal_target_function_boundary():
    f = generate_target_function([-1, 0], [1, 0])
    assert f([0.5, 0.0001]) == 1
    assert f([0.5, -0.0001]) == -1

def test_vertical_target_function_boundary():
    f = generate_target_function([-0.2, 0.5], [-0.2, 0.4])
    assert f([0.1, -0.3]) == 1
    assert f([-0.8, 0.3]) == -1

def test_upward_target_function_boundary():
    f = generate_target_function([-0.9, -0.05], [0.2, 0.7])
    assert f([-0.4, 0.8]) == 1
    assert f([0.6, 0.1]) == -1

def test_downward_target_function_boundary():
    f = generate_target_function([-0.8, 0.1], [0.7, -0.05])
    assert f([-0.4, 0.1]) == 1
    assert f([-0.3, -0.1]) == -1

def test_training_data_generation():
    f = generate_target_function([-0.8, 0.1], [0.7, -0.05])
    print(generate_training_data(f, 10))
    assert 1 == 0