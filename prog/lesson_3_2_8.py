def test_input_text (expected_result, actual_result):
    assert expected_result == actual_result,\
        f" expected {expected_result}, got {actual_result}"
 
 
expected_result = 8
actual_result = 11

test_input_text (expected_result, actual_result)