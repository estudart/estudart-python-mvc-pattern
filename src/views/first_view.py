def introduction_page():
    message = '''
        Sistema cadastral

        * Cadastrar pessoa - 1
        * Buscar pessoa por nome - 2
        * Sair - 5
    '''

    print(message)
    command = input('Comando: ')

    return command
