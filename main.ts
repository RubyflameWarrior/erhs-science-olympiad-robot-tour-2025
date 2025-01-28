//  Robot is 8.25 cm front-to-back
//  Function definitions
function drive(sets: number) {
    Maqueen_V5.motorRun(Maqueen_V5.Motors.All, Maqueen_V5.Dir.CW, 100)
    pause(100 * sets)
    Maqueen_V5.motorStop(Maqueen_V5.Motors.All)
}

function driveBack(sets: number) {
    Maqueen_V5.motorRun(Maqueen_V5.Motors.All, Maqueen_V5.Dir.CCW, 50)
    pause(100 * sets)
    Maqueen_V5.motorStop(Maqueen_V5.Motors.All)
}

function turn(direction: string, sets: number) {
    if (direction == "left" || direction == "l") {
        Maqueen_V5.motorRun(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, 50)
        Maqueen_V5.motorRun(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, 50)
    } else {
        Maqueen_V5.motorRun(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, 50)
        Maqueen_V5.motorRun(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, 50)
    }
    
    pause(300 * sets)
    Maqueen_V5.motorStop(Maqueen_V5.Motors.All)
}

function drivePID() {
    basic.showIcon(IconNames.Angry)
    //  (25 cm half tile length - 4.125 half bot length) rounded to integer = 21 cm
    let targetpoint = 21
    let error = targetpoint - Maqueen_V5.Ultrasonic()
    let previousError = error
    let derivative = 0
    let power = 0
    let sameErrorCount = 0
    let kP = 5
    let kD = 0
    while (Math.abs(error) > 0 && sameErrorCount < 10) {
        error = targetpoint - Maqueen_V5.Ultrasonic()
        //  serial.write_value("Error", error)
        serial.writeValue("Sensor", Maqueen_V5.Ultrasonic())
        if (error == previousError) {
            sameErrorCount += 1
        }
        
        derivative = error - previousError
        previousError = error
        power = error * kP + derivative * kD
        if (power > 100) {
            power = 100
        } else if (power < -100) {
            power = -100
        }
        
        if (power > 0) {
            Maqueen_V5.motorRun(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CCW, Math.abs(power))
            Maqueen_V5.motorRun(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CCW, Math.abs(power))
        } else if (power < 0) {
            Maqueen_V5.motorRun(Maqueen_V5.Motors.M1, Maqueen_V5.Dir.CW, Math.abs(power))
            Maqueen_V5.motorRun(Maqueen_V5.Motors.M2, Maqueen_V5.Dir.CW, Math.abs(power))
        } else {
            Maqueen_V5.motorStop(Maqueen_V5.Motors.All)
        }
        
        pause(10)
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    drivePID()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    turn("l", 1)
})
//  Background main code
//  def onEvery_interval():
//      serial.write_value("Sensor", Maqueen_V5.ultrasonic())
//      # serial.write_value("Roll", input.rotation(Rotation.ROLL))
//      # serial.write_value("Compass", input.compass_heading())
//  loops.every_interval(500, onEvery_interval)
//  MAIN CODE
serial.redirectToUSB()
