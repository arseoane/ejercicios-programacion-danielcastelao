class DniNonValido(Exception):
    """Excepción para un DNI con formato incorrecto."""
    pass


class FormatoLicenzaError(Exception):
    """Excepción para un formato de licenza incorrecto."""
    pass


class Persoa:
    def __init__(self, nome: str, direccion: str, dni: str):
        self.nome = nome
        self.direccion = direccion
        self.set_dni(dni)

    def set_dni(self, dni: str):
        # Validación: 8 números e unha letra final
        if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
            self._dni = dni
        else:
            raise DniNonValido(f"O DNI {dni} non é válido.")

    def get_dni(self) -> str:
        return self._dni


class Deportista(Persoa):
    def __init__(self, nome, direccion, dni, deporte, clube, licencia):
        super().__init__(nome, direccion, dni)
        self.deporte = deporte
        self.clube = clube
        self.set_licencia(licencia)

    def set_licencia(self, licencia: str):
        """
        Verifica o formato aaaadddnnnnnn:
        - aaaa: 4 números do ano
        - ddd: 3 letras do deporte
        - nnnnnn: 6 números de licenza
        """
        if len(licencia) == 13:
            ano = licencia[0:4]
            dep = licencia[4:7]
            num = licencia[7:13]

            if ano.isdigit() and dep.isalpha() and num.isdigit():
                self._licencia = licencia
                return

        raise FormatoLicenzaError("Formato de licenza incorrecto (aaaadddnnnnnn).")

    def get_licencia(self) -> str:
        return self._licencia