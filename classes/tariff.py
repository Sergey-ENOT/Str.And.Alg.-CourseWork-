import csv


class Tariff:
    def __init__(self, name, services):
        self.name = name
        self.services = services
        self.price = 0

    def get_price(self, dict_services):
        for value in self.services:
            self.price += dict_services[value].price

    def __str__(self):
        return self.name + " " + " ".join(self.services) + " " + str(self.price)


class Tariffs:
    def __init__(self):
        self.dict_tariffs = {}
        self.id_dict_tariff = {}

    def import_data(self, path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                data = Tariff(row['name'], row['service_ID'].split(','))
                self.dict_tariffs[row['ID']] = data

    def export_data(self, path):
        header = ['ID', 'name', 'service_ID']    # csv header

        data = []     # csv data
        str_services = ""

        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|')
            csvwriter.writerow(header)
            for elem in self.dict_tariffs.keys():
                data.append(elem)
                data.append(self.dict_tariffs[elem].name)
                list_services = self.dict_tariffs[elem].services
                for i in range(len(list_services)):
                    if i == (len(list_services) - 1):
                        str_services += str(list_services[i])
                    else:
                        str_services += str(list_services[i]) + ","
                data.append(str_services)

                csvwriter.writerow(data)
                data = []
                str_services = ""
