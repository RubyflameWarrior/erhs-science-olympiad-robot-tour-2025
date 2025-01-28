# Robot is 8.25 cm front-to-back

# Function definitions
def drive(sets):
    Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CW, 100)
    pause(850 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

def driveBack(sets):
    Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CCW, 100)
    pause(850 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

def turn(direction, sets):
    if direction == "left" or direction == "l":
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, 50)
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, 50)
    else:
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, 50)
        Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, 50)
    pause(600 * sets)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

def drivePID():
    # (25 cm half tile length - 4.125 half bot length) rounded to integer = 21 cm
    targetpoint = 21
    
    error = targetpoint - Maqueen_V5.ultrasonic()
    previousError = error
    derivative = 0
    power = 0

    sameErrorCount = 0

    kP = 5
    kD = 0

    while abs(error) > 0 and sameErrorCount < 10:
        error = targetpoint - Maqueen_V5.ultrasonic()
        # serial.write_value("Error", error)
        serial.write_value("Sensor", Maqueen_V5.ultrasonic())
        if error == previousError:
            sameErrorCount += 1
        derivative = error - previousError
        previousError = error
        power = (error * kP) + (derivative * kD)

        if power > 100:
            power = 100
        elif power < -100:
            power = -100

        if power > 0:
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, abs(power))
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, abs(power))
        elif power < 0:
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, abs(power))
            Maqueen_V5.motor_run(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, abs(power))
        else:
            Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)

        pause(10)

def on_button_pressed_a():
    drivePID()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    turn("l", 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Background main code
# def onEvery_interval():
#     serial.write_value("Sensor", Maqueen_V5.ultrasonic())
#     # serial.write_value("Roll", input.rotation(Rotation.ROLL))
#     # serial.write_value("Compass", input.compass_heading())
# loops.every_interval(500, onEvery_interval)

# MAIN CODE
basic.show_icon(IconNames.HAPPY)
drive(2)

serial.redirect_to_usb() # Ignore this
# drive(2)