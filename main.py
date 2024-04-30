from dispatcher import Dispatcher


dispatcher = Dispatcher()


while True:
    command = input('Введите команду:')
    command = command.lower().strip(' ')
    if command in dispatcher.available_commands:
        if command in dispatcher.commands_to_change_patient:
            patient_id = input('Введите ID пациента:')
            patient_id = int(patient_id)
            command = [command, patient_id]
        response = dispatcher.handle_command(command)
    else:
        response = ''
    print(response)
