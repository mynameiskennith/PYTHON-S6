class String1:
    def get_String(self):
        self.s = input('Enter a String : ')

    def print_String(self):
        print(self.s.upper())

a = String1()
a.get_String()
a.print_String()