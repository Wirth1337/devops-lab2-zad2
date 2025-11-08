from src.app.main import greet

def test_greet():
    assert greet("Tester") == "Hello"
