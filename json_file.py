import json

# Task 1

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
talaba  = json.loads(talaba_json)
talaba_json1 = json.dumps(talaba)


with open('mashina.json', 'w') as f:
    json.dump(data, f)

with open('talaba.json', "w") as f:
    json.dump(talaba, f)




# Task 2


with open('students.json',) as f:
     student = json.load(f)

student_json = json.dumps(student, indent=4)
# print(student_json)
print(f'{student["student"][0]["name"]} {student["student"][0]["lastname"]}, {student["student"][0]["year"]} - kurs, {student["student"][0]["faculty"]} talabasi')
print(f'{student["student"][1]["name"]} {student["student"][1]["lastname"]}, {student["student"][1]["year"]} - kurs, {student["student"][1]["faculty"]} talabasi')
print(f'{student["student"][2]["name"]} {student["student"][2]["lastname"]} {student["student"][2]["year"]} - kurs, {student["student"][2]["faculty"]} talabasi')





# Task 3

with open('api-result.json') as f:
    python = json.load(f)

python_json = json.dumps(python, indent=4)

a = (f"Title:  {python['query']['pages']['13801']['title']} \n"
     f"Extract: {python['query']['pages']['13801']['extract']}" )

print(a)