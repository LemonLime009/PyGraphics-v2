from src.matrix import Matrix
from src.clock import Clock
from src.input import Input

Display = Matrix(20,20)
Clock = Clock(60)
Input = Input()

Display.clear(1)

def hello():
    print("HElLo")

Input.detect("K_LEFT", hello)
