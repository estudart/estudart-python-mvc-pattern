from typing import Dict

class FinderException(Exception):
    pass

class PeopleFinderController:
    def find_by_name(self, person_informations: Dict) -> Dict:
        try:
            self.__validate_name(person_informations)
            response = self.__format_response(person_informations)
            return {"success": True, "message": response}
        except FinderException as err:
            return {"succes": False, "error": str(err)}

    def __validate_name(self, person_informations: Dict) -> None:
        if not isinstance(person_informations["name"], str):
            raise FinderException("Campo nome não é uma string")

    def __format_response(self, person_informations: Dict):
        return {
            "count": 1,
            "type": "Person",
            "attributes": person_informations
        }