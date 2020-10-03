from fib_challenge import app

def test_calculate_fibonacci():
    response = app.test_client().get('/calculate_fibonacci?num="4"')
    assert response.status_code == 200
    assert response.data =="The fibonacci sequence is [0, 1, 1, 2, 3] for the number: s4"

def test_invalid_string():
    response = app.test_client().get('/calculate_fibonacci?num="NotAnInt"')
    assert response.status_code == 500
    assert response.data == "The number is not a valid integer for NotAnInt with error invalid literal for int() with base 10: 'NotAnInt'"
