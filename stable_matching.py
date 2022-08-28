men_preflist = {'Suraj': ['Alice', 'Vriti', 'Kritika', 'Tia'],
				'Jon': ['Vriti', 'Kritika', 'Tia', 'Alice'],
				'Sarthak': ['Kritika', 'Tia', 'Alice', 'Vriti'],
				'Prabal': ['Alice', 'Kritika', 'Tia', 'Vriti']	}

women_preflist = {'Alice': ['Suraj', 'Prabal', 'Jon', 'Sarthak'],
				'Vriti': ['Prabal', 'Jon', 'Sarthak', 'Suraj'],
				'Tia': ['Jon', 'Sarthak', 'Suraj', 'Prabal'],
				'Kritika': ['Suraj', 'Jon', 'Prabal', 'Sarthak']	}

key = men_preflist.keys()
freeMan = [man for man in list(key)] 
temp = [] #initalise both men and women to be free

#to find the stable match for n men and n women. 
def stable():
	while freeMan:  #runs the loop till there is no free man
		for man in freeMan:
			engage(man)


def engage(man):
	#select the first free man and check his pref list
	for woman in men_preflist[man]: 
		engaged = [free for free in temp if woman in free] 
		#if the woman in the preference list is free, 
		#pair the man with her,
		#change remove him from list and goes to the next free man
		if not engaged:
			temp.append([man, woman]) 
			freeMan.remove(man)
			break
		#if the woman is not free
		else:
			#find her current pair
			partner = women_preflist[woman].index(engaged[0][0])
			new_partner = women_preflist[woman].index(man)
			#if the woman prefers the chosen man over her current partner
			if partner > new_partner:
				#replace the chosen man with her current partner
				#and remove him from list
				freeMan.remove(man)
				#put current man as free 
				engaged[0][0] = man
				break



stable()
print(temp)