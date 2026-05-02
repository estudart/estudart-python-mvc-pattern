from typing import Dict

class RegisterException(Exception):
    pass

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:
        try:
            self.__validete_fields(new_person_informations)
            # enviar para models para cadastro de dados
            response = self.__format_response(new_person_informations)
            return {"success": True, "message": response}
        except RegisterException as err:
            return {"success": False, "error": str(err)}

    def __validete_fields(self, new_person_informations: Dict) -> None:
        if not isinstance(new_person_informations["name"], str):
            raise RegisterException("Campo nome não é uma string")

        try: int(new_person_informations["age"])
        except: raise RegisterException('Campo idade incorreto')

        try: float(new_person_informations["height"])
        except: raise RegisterException('Campo altura incorreto')

    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }
