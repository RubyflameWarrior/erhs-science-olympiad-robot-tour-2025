basic.show_icon(IconNames.HAPPY)
# serial.redirect_to_usb()
# basic.show_number(25 - maqueen.ultrasonic(PingUnit.CENTIMETERS))

def drive(sets):
    Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CW, 100)
    pause(100 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)
    serial.write_number(1)

def driveBack(sets):
    Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CCW, 50)
    pause(100 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

def turn(direction, sets):
    if direction == "left":
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, 50)
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, 50)
    else:
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, 50)
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, 50)
    pause(261 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

drive(2)

"""
PIDMode = 1
sameErrorCount = 0

setpoint = 10

error = setpoint - maqueen.ultrasonic(PingUnit.CENTIMETERS)
previousError = error
derivative = 0
power = 0

def on_every_interval():
    basic.show_number(PIDMode)
    if PIDMode == 1:
        kP = 5
        kD = 0

        error = setpoint - maqueen.ultrasonic(PingUnit.CENTIMETERS)
        if error == previousError:
            sameErrorCount = sameErrorCount + 1
        derivative = error - previousError
        previousError = error
        power = (error * kP)
        # basic.show_number(error)
        if error > 0:
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, abs(power))
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, abs(power))
        elif error < 0:
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, abs(power))
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, abs(power))
loops.every_interval(10, on_every_interval)

def basicDrive(target):
    global setpoint = target
    global PIDMode = 1
    while sameErrorCount < 10:
        pause(10)
    global PIDMode = 0
    sameErrorCount = 0

# basicDrive(25)
def on_forever():
serial.write_value("Pitch", input.acceleration(Dimension.X))
basic.forever(on_forever)


def on_every_interval():
    # serial.write_value("Pitch", input.acceleration(Dimension.X))
    serial.write_value("Compass", input.rotation(Rotation.ROLL))
loops.every_interval(10, on_every_interval)
"""

def on_every_interval():
    print(input.compass_heading())
    serial.write_value("Pitch", input.acceleration(Dimension.X))
    # Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CW, 100)
    # maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)