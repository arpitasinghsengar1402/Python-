# Dictionaries are ordered collection of data items. 
# Dictionaries are ordered collection of data items. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(type(info))

dic={
    344:"arpita",
    56:"karan",
    678:"neha",
    567:"zahir"
}
print(dic[56])


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
print(info['eligible'])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())