from bao import greet
from bao.main import main


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_named():
    assert greet("Bao") == "Hello, Bao!"


def test_main_prints(capsys):
    assert main([]) == 0
    assert capsys.readouterr().out.strip() == "Hello, world!"
