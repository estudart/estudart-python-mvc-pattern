import os

from typing import Dict

class PeopleRegisterView:
    def __init__(self):
        pass

    def register_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar nova pessoa \n\n')

        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')

        new_person_informations = {
            "name": name,
            "age": age,
            "height": height
        }

        return new_person_informations

    def register_person_succes(self, message: Dict) -> None:
        os.system('clear')

        success_message = f'''
            Usuário cadastrado com sucesso

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos: 
                Nome: {message["attributes"]["name"]}
                Age: {message["attributes"]["age"]}
        '''
        print(success_message)

    def register_person_failure(self, error: str) -> None:
        os.system('clear')

        fail_message = f'''
            Falha ao cadastrar usuário

            Erro: {error}
        '''
        print(fail_message)
