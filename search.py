# import csv
# #with open("scrapped2.csv","r") as file:
#     ge= "Hostel Registration for 2019-20"
#     sc= csv.reader(file)
#     for row in sc:
#        # for field in row:
#             if row[2] == ge:
#                 print("found")
#             else:
#                 print("not found")
#
#                 file.close()
#
#


if 'Cricket' in open('scrapped2.csv').read():
    print("keyword found/Hostel Accomodation open")
else:
    print("keyword not found/Hostel Accomodation not open")
