# Changes internal string representation from being wrapped with single quotes to double quotes
# With json.dumps, output like '"str"' - thus wrapper needed instead

class strf(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))