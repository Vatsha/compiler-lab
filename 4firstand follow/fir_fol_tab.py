from collections import OrderedDict
def reverse_dict(dictx):
	reverse_dict = OrderedDict()
	key_list = []
	for key in dictx:
		key_list.append(key)
	key_list.reverse()
	for key in key_list:
		reverse_dict[key] =dictx[key]
	return reverse_dict
def first(grammar,terminal):
	first_dict = OrderedDict()
	grammar_first = reverse_dict(grammar)
	for key in grammar_first:
		each_prod = []
		for element in grammar.copy()[key]:
			if element[0:1] in terminal:
				each_prod.append(element[0:1])
			elif element in terminal:
				each_prod.append(element)
			if not each_prod:
				each_prod = first_dict[element[0:1]]
			first_dict[key] = each_prod
	return first_dict
def check_prod(check_key,grammar):
	dic = {}
	for key in grammar:
		pos_list = []
		for element in grammar[key]:
			pos = element.find(check_key)
			if pos >= 0:
				pos_list.append(pos)
			if pos_list:
				dic[key] = pos_list
	return dic		
def follow(grammar,terminal,first_dict):
	follow_dict = OrderedDict()
	for key in grammar:
		each_prod = []
		if key == "E":
			each_prod.append("$")
		elif check_prod(key,grammar):
			pos = check_prod(key,grammar)
			for found_key in pos:
				for element in grammar[found_key]:
					if key in element:
						string = element
				if (int(pos[found_key][0])+1)==len(string) and (found_key!=key):
					each_prod.extend(follow_dict[found_key])
				elif (int(pos[found_key][0])+1)!=len(string) and (key != found_key) :
					each_prod.extend(first_dict[grammar[found_key][0][int(pos[found_key][0])+1]])
					if "epsln" in each_prod:
						each_prod.remove("epsln")
						each_prod.extend(follow_dict[found_key])
				elif key == found_key and (int(pos[found_key][0])+1)!=len(string):
					each_prod.append(grammar[key][0][int(pos[found_key][0])+1])
		follow_dict[key]=list(set(each_prod))
	return follow_dict
def table(grammar,first_grammar,follow_grammar):
	table = OrderedDict()
	non_terminal = []
	terminal = []
	for nt in grammar:
		non_terminal.append(nt)
		terminal.extend(first_grammar[nt])
		terminal.extend(follow_grammar[nt])
	non_terminal = list(set(non_terminal))
	terminal = list(set(terminal))
	terminal.remove("epsln")
	print "non terminal",non_terminal
	print "terminal",terminal
	for nt in non_terminal:
		prod = []
		for ter in terminal:
			if ter in first_grammar[nt]:
				if len(grammar[nt])==1:
					prod.append(grammar[nt])
				else:
					for single_prod in grammar[nt]:
						if single_prod[0] is ter:
							prod.append([single_prod])
						elif single_prod is ter:
							prod.append([single_prod])
			elif "epsln" in first_grammar[nt] and ter in follow_grammar[nt]:
				prod.append(["epsln"])
			else:
				prod.append("error")
			table[nt]=prod
	return table
'''grammar = {}
le = input("length")
for i in range(le):
	key = raw_input("key")
	l = input("number of production")
	lis = list()
	for i in range(0,l):
		lis.append(raw_input())
	grammar.update({key:lis})'''
grammar = OrderedDict()
grammar["E"] = ["TA"]
grammar["A"] = ["+TA","epsln"]
grammar["T"] = ["FP"]
grammar["P"] = ["*FP","epsln"]
grammar["F"] = ["(F)","id"]
terminal = ["+","*","(",")","id","epsln"]
print "Original grammar"
for key, value in grammar.items(): 
    print(key, value)
print "----------------------------------------------"
print "First"
first_grammar = first(grammar,terminal)
for key, value in first_grammar.items(): 
    print(key, value)
print "----------------------------------------------"
print "Follow"
follow_grammar = follow(grammar,terminal,first_grammar)
for key, value in follow_grammar.items(): 
    print(key, value)
print "----------------------------------------------"
ll1table=table(grammar,first_grammar,follow_grammar)
#for key, value in ll1table.items(): 
    #print(key, value)
