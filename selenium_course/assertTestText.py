def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f'expected {expected_result}, got {actual_result}'

a = int(input())
b = int(input())

test_input_text(a, b)
