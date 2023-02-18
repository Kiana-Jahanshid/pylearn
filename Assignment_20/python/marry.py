import random
girls = ["mahtab" , "hane" , "harir" ,"fateme" , "kiana" , "faezeh" , "minoo" , "mina" , "soghra"]
boys = ["mohammad","sobhan","abdollah", "kiya" , "mahdi" , "sajjad" , "homan" , "arman"]

results = []

for i in range(len(boys)):
    g_index = random.randint(0, (len(girls)-1))
    b_index = random.randint(0,(len(boys)-1))
    random_girl = girls[g_index]
    random_boy = boys[b_index]
    results.append((random_boy , random_girl))
    girls.pop(g_index)
    boys.pop(b_index)

print(results)
print("remain girl :" , girls)