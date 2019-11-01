class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        if type(value) == list:
            self[key] = value
        else:
            self[key] = [value]

    def update(self, key, value):
        oldVal = self.get(key)
        newVal = oldVal
        newVal.append(value)

        del self[key]

        self.add(key, newVal)