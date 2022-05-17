from djitellopy import tello
from time import sleep

babner = tello.Tello()
babner.connect()
print(babner.get_battery())
# take off at 170cm
babner.takeoff()
babner.moveup(120)
# move forward 150cm
babner.move_forward(310)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# move forward 50cm
babner.move_forward(600)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# cool slip
babner.flip()
sleep(1)
# move forward 150cm
babner.move_forward(310)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# move forward
babner.move_forward(600)
sleep(1)
# landing
babner.land()
