import RPi.GPIO as GPIO
import time

def manual_motor_test(EN, IN1, IN2):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    try:
        print(f"Тест EN={EN}, IN1={IN1}, IN2={IN2}")

        # Налаштування
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(IN1, GPIO.OUT)
        GPIO.setup(IN2, GPIO.OUT)

        # Задаємо сигнал IN1 = HIGH, IN2 = LOW (звичайна комбінація для запуску)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        # PWM на EN
        pwm = GPIO.PWM(EN, 1000)
        pwm.start(70)

        time.sleep(2)

        # Зупинка
        pwm.stop()
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(EN, GPIO.LOW)
        print("Зупинено.")

    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        GPIO.cleanup()
        print("GPIO очищено.")

# 🧪 Запуск тесту вручну:
if __name__ == '__main__':
    # Просто замінюй значення тут на ті, що хочеш перевірити
    manual_motor_test(EN=2, IN1=3, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=3, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=3, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=3, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=4, IN2=3)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=4, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=4, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=4, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=5, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=5, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=5, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=5, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=6, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=6, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=6, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=6, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=7, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=7, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=7, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=7, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=8, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=8, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=8, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=8, IN2=27)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=9, IN2=18)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=9, IN2=21)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=9, IN2=26)
    time.sleep(3)
    manual_motor_test(EN=2, IN1=9, IN2=27)
    time.sleep(3)

