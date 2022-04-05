import csv
import datetime


class Client:
    def __init__(self, name, surname, patronymic, current_balance, address, date, ID_tariff, active):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.current_balance = current_balance
        self.address = address
        self.date = date
        self.ID_tariff = ID_tariff
        self.active = active

    def plus(self, summ):
        self.current_balance += summ

    def minus(self, summ):
        if self.current_balance >= summ:
            self.current_balance -= summ


class Clients:
    def __init__(self):
        self.dict_clients = {}

    def import_data(self, path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                data = Client(row['name'],
                              row['surname'],
                              row['patronymic'],
                              int(row['current_balance']),
                              row['address'],
                              datetime.datetime.strptime(row['date'], "%d.%m.%Y").date(),
                              row['ID_tariff'],
                              row['active'])
                self.dict_clients[row['ID']] = data

    def export_data(self, path):
        # csv header
        header = ['ID', 'name', 'surname', 'patronymic', 'current_balance', 'address', 'date', 'ID_tariff', 'active']

        data = []     # csv data

        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|')
            csvwriter.writerow(header)
            for elem in self.dict_clients.keys():
                data.append(elem)
                data.append(self.dict_clients[elem].name)
                data.append(self.dict_clients[elem].surname)
                data.append(self.dict_clients[elem].patronymic)
                data.append(str(self.dict_clients[elem].current_balance))
                data.append(self.dict_clients[elem].address)
                data.append(self.dict_clients[elem].date.strftime("%d.%m.%Y"))
                data.append(self.dict_clients[elem].ID_tariff)
                data.append(self.dict_clients[elem].active)

                csvwriter.writerow(data)
                data = []
