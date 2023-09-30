from src.matrix import Matrix
from src.clock import Clock

display = Matrix(20,20)
clock = Clock(60)

display.clear(1)

clock.startTicker()

display.rect(0,0,4,7)
display.point(19,19)
display.update()

clock.endTicker()

clock.test()
