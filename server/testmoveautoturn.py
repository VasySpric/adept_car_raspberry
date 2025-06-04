import RPi.GPIO as GPIO
import time
import itertools

# Вже перевірені робочі піни напрямків
Motor_A_Pin1 = 21  # Ліво назад
Motor_A_Pin2 = 26  # Ліво вперед
Motor_B_Pin1 = 27  # Право вперед
Motor_B_Pin2 = 18  # Право назад

# Безпечні GPIO пін номери (BCM)
SAFE_GPIO_PINS = [
    2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15,
    16, 17, 19, 20, 22, 23,
    24, 25
]

# Видалимо ті, які вже використовуються
USED_PINS = {Motor_A_Pin1, Motor_A_Pin2, Motor_B_Pin1, Motor_B_Pin2}
AVAILABLE_EN_PINS = [pin for pin in SAFE_GPIO_PINS if pin not in USED_PINS]

def test_en_pin_combinations():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    combinations = list(itertools.permutations(AVAILABLE_EN_PINS, 2))

    print(f"Всього комбінацій для EN: {len(combinations)}")

    try:
        for idx, (Motor_A_EN, Motor_B_EN) in enumerate(combinations):
            print(f"[{idx+1}] Тест Motor_A_EN={Motor_A_EN}, Motor_B_EN={Motor_B_EN}")

            # Setup all
            GPIO.setup([Motor_A_EN, Motor_B_EN, Motor_A_Pin1, Motor_A_Pin2, Motor_B_Pin1, Motor_B_Pin2], GPIO.OUT)

            # Задати напрям: вперед обидва мотори
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.HIGH)
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)

            pwm_A = GPIO.PWM(Motor_A_EN, 1000)
            pwm_B = GPIO.PWM(Motor_B_EN, 1000)

            pwm_A.start(60)
            pwm_B.start(60)

            print("→ Вперед")
            time.sleep(2)

            # Задати напрям: назад обидва мотори
            GPIO.output(Motor_A_Pin1, GPIO.HIGH)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)

            print("← Назад")
            time.sleep(2)

            # Зупинка
            pwm_A.stop()
            pwm_B.stop()

            GPIO.output([Motor_A_Pin1, Motor_A_Pin2, Motor_B_Pin1, Motor_B_Pin2, Motor_A_EN, Motor_B_EN], GPIO.LOW)

            GPIO.cleanup([Motor_A_EN, Motor_B_EN, Motor_A_Pin1, Motor_A_Pin2, Motor_B_Pin1, Motor_B_Pin2])
            print("⏹ Зупинено\n")

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Тест перервано вручну.")
    finally:
        GPIO.cleanup()
        print("GPIO очищено.")

# Запуск
if __name__ == '__main__':
    test_en_pin_combinations()
