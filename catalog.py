from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if type(item) is Magazine:
                        list_result.append(f'Title {item.title}, volume: {item.volume}, Type Catalog: Magazine')
                    elif type(item) is Book:
                        list_result.append(f'Title {item.title}, DDS Number: {item.dds_number}, Type Catalog: Book')
                    if type(item) is Dvd:
                        list_result.append(f'Title {item.title}, Gendre: {item.genre}, Type Catalog: Dvd')
                    elif type(item) is Cd:
                        list_result.append(f'Title {item.title}, Artist: {item.artist}, Type Catalog: Cd')
        return list_result