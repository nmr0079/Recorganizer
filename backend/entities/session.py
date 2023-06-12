from datetime import datetime

from patient import Patient


class Session:

    def __init__(self, patient: Patient, **kwargs):
        self.patient = patient
        self.__dict__.update(kwargs) # add attributes to class based on kwargs
        self.date = datetime.now().strftime("%Y%m%d")
    
    def __repr__(self):
        return f'Session(' + ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()]) + ')'   



if __name__ == '__main__':
    patient = Patient('AX314', 'ABC')
    session = Session(patient)
    print(repr(session))
