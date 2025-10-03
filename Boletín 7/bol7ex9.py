''' 9. Sobre a cadea de texto “ Jeve jeve jeve”, substitúe todas as vocais e
pola vogal para dando como resultado “java java java”.'''

cadea = " Jeve jeve jeve"
print("Cadea antes: ", cadea)

cadea = cadea.lower()
cadea = cadea.replace("e", "a")
cadea = cadea[1::]

print("Cadea agora: ", cadea)