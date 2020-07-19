class Output:
    def __init__(self, _name: str):
        self._name = _name

    def get_name(self):
        try:
            self._name = int(self._name)
        except:
            self._name += ' '
        return self._name

    def set_name(self, name):
        self._name = name

def main():
    avraham = Output('Avraham')
    avraham.get_name()
    print(avraham.get_name())


if __name__ == '__main__':
    main()
    # print(avraham._name)
