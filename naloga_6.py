from Core import *

from time import *

# Naloga 6
start_time = time()
nal_6 = Core(random_color())

while time() < start_time+20:
    nal_6.run()
    sleep(0.02)
