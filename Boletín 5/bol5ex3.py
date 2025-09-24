# 3. Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

for fahrenheit in range(0, 120, 10):
    print(str((fahrenheit - 32) * 5/9))
