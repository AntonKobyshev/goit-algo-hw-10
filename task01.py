import pulp

model = pulp.LpProblem("MaximizeProduction", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

model += 2 * lemonade + fruit_juice <= 100, "WaterConstraint"
model += lemonade <= 50, "SugarConstraint"
model += lemonade <= 30, "LemonJuiceConstraint"
model += 2 * fruit_juice <= 40, "FruitPureeConstraint"

model += lemonade + fruit_juice, "TotalProduction"

model.solve()

print("Optimal Production:")
print("Lemonade:", pulp.value(lemonade))
print("Fruit Juice:", pulp.value(fruit_juice))
