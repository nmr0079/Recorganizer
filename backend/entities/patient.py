class Patient:

    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        self.__dict__.update(kwargs) # add attributes to class based on kwargs

    def __repr__(self) -> str:
        return 'Patient(' + ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()]) + ')'        



if __name__ == '__main__':
    patient = Patient('AX314', 'ABC')
    print(repr(patient))
    patient = Patient('GF342', 'POW', place='X-122')
    print(repr(patient))