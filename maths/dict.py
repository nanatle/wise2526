data: dict[int:str] = {2:'A', 1:'B'}

#data.update({'b=B', '2:C'})
#print(data)

#data.setdefault(1,5)
#print(data)
#------------------------
#Aufgabe 3.3
name: str = input('Name: ')
tag: str = input('Tag: ')
monat: str = input('Monat: ')
jahr: str = input('Jahr: ')
birthday = (jahr, monat, tag)
data: dict[str:str] = {name, birthday}
print(data)