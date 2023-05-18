
with open('pi_million_digits.txt', 'r') as file:
    a = 8
    b = []

    for line in file:
        line = line.strip()  # Remove any leading or trailing whitespace
        for i in range(0, len(line), a):
            end_index = i + a
            group = line[i:end_index]
            b.append(group)
     
    c = '12112003'

    if c in b:
        print(c)
    else:
        print("Sizning tug'ilgan sanangiz bu ro'yxatda yo'q ekan")

