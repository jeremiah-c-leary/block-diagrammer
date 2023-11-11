
def print_map(self):
    for line in self.map:
        sLine = ''
        for item in line:
            sLine += item.__class__.__name__.center(14)
        print(sLine)
