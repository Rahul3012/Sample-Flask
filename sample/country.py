import json

def find_Capital(coun):
    counter=0
    data=json.load(open(r"templates\country_with_capitals.json"))
    coun=coun.lower()
    coun=coun.split()
    coun=' '.join([x.capitalize() for x in coun])
    str1=coun
    for i in data:
        if i['country']==str1:
            return (i['city'])
            break
        else:
            continue
    if counter==len(data):
        return ("not found")


'''For Alternative '''
# import json
# def find_Capital(coun):
#     data=json.load(open("templates\country_with_capitals.json"))
#     #coun=coun.split()
#     #coun=' '.join([x.capitalize() for x in coun])
#     for i in data:
#         if i["country"]==coun:
#             return str(i["city"])
#             break
#         else:
#             return str("not found"+coun)
#
# data=find_Capital("Afghanistan")
# print(data)
