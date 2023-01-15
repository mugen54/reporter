import pandas as pd


def function_a():
    print("a")
    value = 5/0
    return 5

def function_b():
    print("J appelle la fonction a")
    function_a()


function_b()
