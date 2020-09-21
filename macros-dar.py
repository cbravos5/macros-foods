import copy
from prettytable import PrettyTable

class Food(object):
	def __init__(self, name, carb_quant, protein_quant, quantity):
		self.name = name
		self.carb_quant = carb_quant
		self.protein_quant = protein_quant
		self.grams_unity = quantity

inp = input().split(' ')

meals_day = 5 if (len(inp) == 2) else 6

total_carbs = int(inp[0])
total_proteins = int(inp[1])

meals = []
for x in range(meals_day):
	meals.append(list())

foods = []

###############################################
#cafe da manha e janta eh padrao
foods.append(Food("ovo",0,6,3))
foods.append(Food("banana",15,0,2))

meals[0] = copy.deepcopy(foods)

foods.clear()

foods.append(Food("banana",15,0,2))

meals[meals_day - 1] = copy.deepcopy(foods)

foods.clear()

total_carbs -= 60
total_proteins -= 18
##################################################

####################################################
#almoco e janta
partial_carbs = total_carbs/(len(inp) + 1)
partial_proteins = total_proteins/(len(inp) + 1)

quant_arroz = 100 if meals_day == 5 else 120
quant_feijao = int(round((partial_carbs - quant_arroz*0.28)/0.14))


foods.append(Food("arroz",0.28,0,quant_arroz))
foods.append(Food("feijao",0.14,0,quant_feijao))
foods.append(Food("frango",0,0.32,int(round(partial_proteins/0.32))))

meals[1] = copy.deepcopy(foods)
meals[meals_day - 2] = copy.deepcopy(foods)

foods.clear()
####################################################

####################################################
#cafe(s) da tarde
foods.append(Food("batata doce",0.28,0,int(round(partial_carbs/0.28))))
foods.append(Food("frango",0,0.32,int(round(partial_proteins/0.32))))

meals[2] = copy.deepcopy(foods)
if (meals_day == 6):
	meals[3] = copy.deepcopy(foods) 
####################################################
	

table_foods = PrettyTable()

if (meals_day == 5):
	names = ["Café da manhã","Almoço","Café da tarde","Janta","Ceia"]
else:
	names = ["Café da manhã","Almoço","Café da tarde 1","Café da tarde 2","Janta","Ceia"]

refeicao = []

for i in range(meals_day):
	for x in range(len(meals[i])):
		refeicao.append(str(meals[i][x].grams_unity) + " gramas/unidades de " + str(meals[i][x].name))
	if (len(refeicao) == 2):
		refeicao.append(" ")
	elif(len(refeicao) == 1):
		refeicao.append(" ")
		refeicao.append(" ")	
	table_foods.add_column(names[i],refeicao)
	refeicao.clear()

table_utility = PrettyTable()

aux = ["Macarrão","Pão integral","Pão francês"]
table_utility.add_column("Substituto",copy.deepcopy(aux))
aux = [str(int((round(partial_carbs/0.31))))+" gramas/unidades",\
							str(int((round(partial_carbs/6))))+ " gramas/unidades",\
							str(int((round(partial_carbs/30))))+ " gramas/unidades"]
table_utility.add_column("Equivale a",copy.deepcopy(aux))
aux.clear()

table_macros = PrettyTable()
for i in range(meals_day):
	carbs = 0
	proteins = 0
	for x in range(len(meals[i])):
		carbs += meals[i][x].carb_quant*meals[i][x].grams_unity
		proteins += meals[i][x].protein_quant*meals[i][x].grams_unity
	aux = [str(int(round(carbs))) + " g de carbs e " + str(int(round(proteins))) + " g de proteinas"]
	table_macros.add_column(names[i],copy.deepcopy(aux))
	aux.clear()

print(table_macros)
print(" ")
print(table_foods)
print(" ")
print(table_utility)

with open("macros_out.html", 'w') as w:
    w.write(table_macros.get_html_string())
    w.write("<p>")
    w.write(table_foods.get_html_string())
    w.write("<p>")
    w.write(table_utility.get_html_string())



