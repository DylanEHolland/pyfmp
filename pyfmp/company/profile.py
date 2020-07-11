from ..api import company_profile as company_profile_request

float_columns = set([
    'price',
    'beta',
    'volAvg',
    'mktCap',
    'lastDiv',
    'dcfDiff',
    'dcf',
    'fullTimeEmployees',
    'changes'
])

list_columns = set([
    
])

class company_profile:
    data = {}
    index = -1

    def __init__(self, ticker, client):
        object.__getattribute__(self, "_load_data")(ticker, client)

    def __iter__(self):
        object.__setattr__(self, "index", -1)
        return self

    def __next__(self):
        if object.__getattribute__(self, "index") >= len(object.__getattribute__(self, "data")) - 1:
            raise StopIteration
        
        object.__setattr__(self, "index", 
            object.__getattribute__(self, "index") + 1
        )
        
        key = list(object.__getattribute__(self, "data").keys())[object.__getattribute__(self, "index")]

        return (key, object.__getattribute__(self, "data")[key])

    def __getattribute__(self, key):
        return object.__getattribute__(self, "data")[key]

    def __getitem__(self, key):
        return object.__getattribute__(self, "data")[key]

    def _load_data(self, ticker, client):
        data = company_profile_request(client, ticker)
        data = data[0]
        data_store = object.__getattribute__(self, "data")

        for key in data:
            value = data[key]
            if key in float_columns:
                value = float(value)
            elif key == "range":
                buffer = value.split(",")
                value = [
                    float(value[0]),
                    float(value[1])
                ]

            data_store[key] = value

    def __str__(self):
        return str(
            object.__getattribute__(self, "data")
        )