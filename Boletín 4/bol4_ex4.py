num = int(input("Pon un número entre 1 e 99: "))

iniciais = {
    0: "",
    1: "un",
    2: "dous",
    3: "tres",
    4: "catro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dezaseis",
    17: "dezasete",
    18: "dezaoito",
    19: "dezanove"
  }

decenas = {
    2: "vinte",
    3: "trinta",
    4: "cuarenta",
    5: "cinconta",
    6: "sesenta",
    7: "setenta",
    8: "oitenta",
    9: "noventa"
  }

if num < 1 or num > 99:
    print("Número incorrecto.")
else:
      if num < 20:
        print(iniciais[num])
      else:
        num = str(num)
        a = int(num[0])
        b = int(num[1])
        if b == 0:
          print(decenas[a],iniciais[b])
        else:
          print(decenas[a],"e",iniciais[b])