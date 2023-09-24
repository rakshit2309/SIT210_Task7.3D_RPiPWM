import RPi.GPIO as GPIO
import time

# Ultra Sonic GPIO pins
tPin = 13  # Trigger pin
ePin = 19  # Echo pin


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  
GPIO.setup(tPin, GPIO.OUT)  
GPIO.setup(ePin, GPIO.OUT) t

# Creating an LED named 'led' instance, which will initialize PWM with GPIO pin 17
# and a frequency of 350Hz
led = GPIO.PWM(17, 350)

# Starting the PWM with a duty cycle of 0%
led.start(0)

# function to calculate distance from the sensor
def obtainingDistance():
    # Sending a pulse to the ultrasonic sensor to trigger a measurement
    GPIO.output(tPin, True)

    # Wait for a short time
    time.sleep(0.001)
    GPIO.output(tPin, False)

    # calculate the time when the ultrasonic sensor sends the pulse
    startPulse = time.time()
    endPulse = time.time()

    # Measuring the time it takes for the ultrasonic sensor to receive the pulse back
    while GPIO.input(ePin) == 0:
        startPulse = time.time()
    while GPIO.input(ePin) == 1:
        endPulse = time.time()

      pulseLength = endPulse - startPulse    # Calculate the duration of the pulse, which corresponds to the distance

    distance = pulseLength * 17150    # Calculate the distance in centimeters (speed of sound in air is approximately 343 meters per second)
    return distance

while True:
    distance = obtainingDistance()  # Obtain the distance from the sensor    
    brightness = max(0, min(100, int(100 - (distance / 10))))  # Map the distance to LED brightness (0% to 100%)
    led.ChangeDutyCycle(brightness)
    time.sleep(0.1)
