book = {}
book['aryan'] = {
    'name' : 'aryan',
    'address' : 'plot 35 air for housing society',
    'phone' : 8180916400
}
book['happy'] = {
    'name' : 'happy',
    'address' : 'plot 35 air for housing society',
    'phone' : 7758928844
}

import json
s = json.dumps(book)
print(s)