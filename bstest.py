import time

asdf = True
a = 0
try:
    while asdf:
        print a
        a = a + 1
        time.sleep(1)
except KeyboardInterrupt:
    time.sleep(10)
    asdf = False
