fruits=["apple","banana","cherry","dragon","grapes"]
fruits[3]="dragonfruit"
fruits.append("Mango")
fruits.extend(["custard","strawberry"])
fruits.remove("dragonfruit")
print(fruits)

import random
friends=["Alice","Bob","Charlie","David","Emanuel"]

print(random.choice(friends))

random_index=random.randint(0,4)
print(friends[random_index])