import utime
import machine

pin1 = machine.Pin(15, machine.Pin.OUT)
pin2 = machine.Pin(16, machine.Pin.OUT)
a1 = machine.PWM(machine.Pin(15))

for _ in range(1,5):
    # get brighter
    for n in range(0,64,2):
        print("n:{}".format(n))
        a1.duty_u16(n*1000)
        utime.sleep(0.02)

    # get dimmer
    for n in range(64,-2,-2):
        print("n:{}".format(n))
        a1.duty_u16(n*1000)
        utime.sleep(0.02)

# while True:
#     pin1.value(1)
#     pin2.value(1)
#     time.sleep(1)
#     print("loop")
#     pin1.value(0)
#     pin2.value(0)
#     time.sleep(0.5)
