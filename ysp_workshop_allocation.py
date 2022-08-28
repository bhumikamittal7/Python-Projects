import pandas as pd
import xlwt
import xlsxwriter

data = pd.read_excel('responses.xlsx')
out_list = list(data['Please share your workshop preference for Day 1'])
out = [elem.split(",") for elem in out_list]
out = [elem[:-1] for elem in out]
name =list(data['Hello, what\'s your name?'])
email = list(data['What\'s your ashoka email address?'])

d = {'Logic':0, 'Bullsh\\*t Theory':1, 'Basics of Odissi for Beginners':2, 'Perceiving Personas':3,
     'Decoding Deutsch - German 101':4,'Keeping up with the Dictators: Politics 101':5,
     'The Anatomy of Argumentation':6,'One Up On Wall Street':7,
     'Music at the Movies':8,'A Discourse on Ethical Dilemmas':9 }
s = [[d[x] for x in out[i]] for i in range(len(out))]

slots = 25
w = 10
eff = 5

def preferences(L):
    workshops = [[] for i in range(w)]     
    i = 0
    while (name):
        pref = L[0][i]
        if (i==eff):
            print(i)
        if (len(workshops[pref]) < slots):
            workshops[pref].append(name[0])
            name.pop(0)
            L.pop(0)
            i = 0
        else:
            name[0], name[-1] = name[-1], name[0]
            i = i+1
    return workshops

l = preferences(s)
d = dict((v, k) for k, v in d.items())

df = pd.DataFrame(l)
df.index = df.index.map(d)
df.index = df.index.to_series().replace(d)
df = df.rename(index = d)
df.to_excel("workshops1.xlsx")

name1 =list(data['Hello, what\'s your name?'])
output = []
for x in range(slots):
    for student in name1:
        row_numbers = list(df[df[x] == student].index.values)
        if len(row_numbers) != 0:
            row_numbers.insert(0, email[name1.index(student)])
            row_numbers.insert(0, student)
            output.append(row_numbers)

df1 = pd.DataFrame(output)
df1.to_excel("student1.xlsx", index = False)
