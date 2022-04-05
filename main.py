from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients


ds = Services()
ds.import_data("csv files/services.csv")
for k in ds.dict_services.keys():
    print(k, ds.dict_services[k])
print("------------------------")
df = Tariffs()
df.import_data("csv files/tariffs.csv")
for k in df.dict_tariffs.keys():
    for n in df.dict_tariffs[k].services:
        df.dict_tariffs[k].price += ds.dict_services[n].price
    print(k, df.dict_tariffs[k])
print("------------------------")
dc = Clients()
dc.import_data("csv files/clients.csv")
for k in dc.dict_clients.keys():
    print(k, dc.dict_clients[k].name, dc.dict_clients[k].surname, dc.dict_clients[k].date.strftime("%d.%m.%Y"))

dc.export_data("test_file.csv")


# print("hello world!")
