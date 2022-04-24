import csv


class Service:
    def __init__(self, content, price):
        self.content = content
        self.price = int(price)

    def __str__(self):
        return self.content + " " + str(self.price)


class Services:
    def __init__(self):
        self.dict_services = {}

    def import_data(self, path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                data = Service(row['content'], row['price'])
                self.dict_services[row['ID']] = data

    def export_data(self, path):
        header = ['ID', 'content', 'price']    # csv header

        data = []     # csv data

        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|')
            csvwriter.writerow(header)
            for elem in self.dict_services.keys():
                data.append(elem)
                data.append(self.dict_services[elem].content)
                data.append(str(self.dict_services[elem].price))
                csvwriter.writerow(data)
                data = []
