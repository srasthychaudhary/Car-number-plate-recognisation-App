#!/usr/bin/python3

import cgi
import requests
import xmltodict
import json

print("content-type: text/html")
print()



data = cgi.FieldStorage()
p_number= data.getvalue("x")

def get_vehicle_info(number):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=plateapi".format(str(number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1


data1 = get_vehicle_info(p_number)

print("<h1>vehicle details</h1>")
print("<br>")
print("Owner Information         : ",data1["Owner"])
print("Model                     : ",data1["CarModel"]["CurrentTextValue"])
print("Company Name             : ",data1["CarMake"]["CurrentTextValue"])
print("Registration Year        : ",data1["RegistrationYear"])
print("Insurance Till Date      : ",data1["Insurance"])
print("Engine Number            : ",data1["EngineNumber"])
print("Fuel Type                : ",data1["FuelType"]["CurrentTextValue"])
print("Identification Number    : ",data1["VechileIdentificationNumber"])
print("Registration Date        : ",data1["RegistrationDate"])
print("Fitness Till Date        : ",data1["Fitness"])
print("Registration Location    : ",data1["Location"])