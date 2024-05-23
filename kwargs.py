def add_ages(**ages):
    sum=0
    for k,v in ages.items():
        sum+=v
    return sum

print ("ages total", add_ages(michael= 22, david =21, mathew =24))
