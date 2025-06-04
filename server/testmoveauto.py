import RPi.GPIO as GPIO
import time
import itertools

# Безпечні GPIO пін номери (BCM)
SAFE_GPIO_PINS = [
    2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27
]

def test_motor_combinations():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    combinations = list(itertools.permutations(SAFE_GPIO_PINS, 3))

    print(f"Всього комбінацій: {len(combinations)}")

    try:
        for idx, (en_pin, in1_pin, in2_pin) in enumerate(combinations):
            print(f"[{idx+1}] Тестую: EN={en_pin}, IN1={in1_pin}, IN2={in2_pin}")

            # Налаштування пінів
            GPIO.setup(en_pin, GPIO.OUT)
            GPIO.setup(in1_pin, GPIO.OUT)
            GPIO.setup(in2_pin, GPIO.OUT)

            # Задання напрямку обертання (назад)
            GPIO.output(in1_pin, GPIO.HIGH)
            GPIO.output(in2_pin, GPIO.LOW)

            pwm = GPIO.PWM(en_pin, 1000)
            pwm.start(60)

            time.sleep(2)

            # Зупинка
            pwm.stop()
            GPIO.output(in1_pin, GPIO.LOW)
            GPIO.output(in2_pin, GPIO.LOW)
            GPIO.output(en_pin, GPIO.LOW)

            # Час на візуальне спостереження
            time.sleep(0.3)

            # Очистити перед наступною ітерацією
            GPIO.cleanup([en_pin, in1_pin, in2_pin])

    except KeyboardInterrupt:
        print("Тест перервано вручну.")
    finally:
        GPIO.cleanup()
        print("GPIO очищено.")

# Запуск
if __name__ == "__main__":
    test_motor_combinations()
