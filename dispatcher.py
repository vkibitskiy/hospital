

class Dispatcher:
    def __init__(self):
        self.patients = [1] * 200
        self.commands_to_change_patient = [
            'узнать статус пациента',
            'get status',
            'повысить статус пациента',
            'status up',
            'понизить статус пациента',
            'status down',
            'выписать пациента',
            'discharge'
        ]
        self.command_to_get_statistic = "рассчитать статистику"
        self.commands_to_stop = ["стоп", "stop"]
        self.available_commands = (self.commands_to_change_patient + self.commands_to_stop +
                                   [self.command_to_get_statistic])

    def get_actual_patient_status_number(self, patient_id):
        status_number = self.patients[patient_id]
        return status_number

    def get_patient_status_name_by_id(self, patient_id):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        status_number = self.get_actual_patient_status_number(patient_id)
        status_name = statuses[status_number]
        return status_name

    def increase_status(self, patient_id):
        actual_patient_status_number = self.get_actual_patient_status_number(patient_id)
        if actual_patient_status_number == 3:
            flag = False
        else:
            self.patients[patient_id] += 1
            flag = True
        return flag

    def decrease_status(self, patient_id):
        actual_patient_status_number = self.get_actual_patient_status_number(patient_id)
        if actual_patient_status_number == 0:
            flag = False
        else:
            self.patients[patient_id] -= 1
            flag = True
        return flag

    def discharge(self, id):
        pass

    def statistic(self):
        pass

    def handle_command(self, command):
        if type(command) == str:
            response = ''
        else:
            patient_id = command[1] - 1
            command = command[0]
            if command in ('узнать статус пациента', 'get status'):
                status_name = self.get_patient_status_name_by_id(patient_id)
                response = f'Статус пациента: "{status_name}"'
            elif command in ('повысить статус пациента', 'status up'):
                flag = self.increase_status(patient_id)
                if flag:
                    patient_status = self.get_patient_status_name_by_id(patient_id)
                    response = f'Новый статус пациента: "{patient_status}"'
                else:
                    discharge_flag = input('Желаете этого клиента выписать?')
                    discharge_flag = discharge_flag.lower().strip(' ')
                    if discharge_flag == 'да':
                        self.discharge(patient_id)
                        response = 'Пациент выписан из больницы'
                    else:
                        response = 'Пациент остался в статусе "Готов к выписке"'
            elif command in ('понизить статус пациента', 'status down'):
                flag = self.decrease_status(patient_id)
                if flag:
                    patient_status = self.get_patient_status_name_by_id(patient_id)
                    response = f'Новый статус пациента: "{patient_status}"'
                else:
                    pass
            elif command in ('выписать пациента', 'discharge'):


            else:
                response = ''

        return response
