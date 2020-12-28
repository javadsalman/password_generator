import random

def get_order():
    length = int(input('Length: '))
    content_indexes = input("""Content;
    1. Lowercases
    2. Uppercases
    3. Digits
    4. Symbols
    5. Identific
    Select: """)
    return {'length': length, 'content_indexes': content_indexes}



class Characters():
    # Ascii codes of characters
    lowercase =  list(range(97, 123))
    uppercase = list(range(65, 91))
    digits = list(range(48, 58))
    symbols =  list(range(33, 48)) + list(range(58, 65))
    identific = lowercase + uppercase + digits + [95] #the characters which accpeted by str.isidentifier() method
    indexes = {'1': 'lowercase', '2': 'uppercase', '3': 'digits', '4': 'symbols', '5': 'identific'} #for getting attribute name according to index

    def new_pass(self, length=8, content_indexes='123'):
        contents = []
        for i in content_indexes:
            attribute_name = self.indexes[i] #atribute name of selected content index
            contents.extend(self.__getattribute__(attribute_name)) # extend contents with selected ascii codes of selected content index
        
        return ''.join(chr(random.choice(contents)) for i in range(length)) # return result as string



if __name__ == '__main__':
    c = Characters()
    while True:
        order = get_order()
        print('Result:', c.new_pass(**order), end='\n\n')

