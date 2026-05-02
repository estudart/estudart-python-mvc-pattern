import os

from typing import Dict

class PeopleFinderView:
    def __init__(self):
        pass

    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')

        name = input('Determine o nome da pessoa para busca: ')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations

    def find_person_success(self, message: Dict) -> None:
        os.system('clear')

        success_message = f'''
            Pessoa encontrada!

            Infos: 
                Nome: {message["attributes"]["name"]}
        '''
        print(success_message)

    def find_person_fail(self, error: str) -> None:
        os.system('clear')

        fail_message = f'''
            Pessoa não encontrada!

            Error: {error}
        '''
        print(fail_message)
