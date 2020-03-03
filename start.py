n=10
for i in range (n):
    print(i)



#test za 2ra verzija za push na github

n=20
for i in range (n):
    print(i)



the_list =[1,2,3,4,5]
the_list2=["a","b","c","d","e"]

ale=zip(the_list2,the_list)
print(ale)
ale2=dict(ale)
print(ale2)

for item in ale2.items():
    print(item)