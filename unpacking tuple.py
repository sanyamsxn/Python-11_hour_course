person1_info=('john',25,'pizza')
person2_info=('jack',23,'burger')
persons=[person1_info,person2_info]           #creating list of tuples
for name,age,fav_food in persons:
    print(name)
    print(age)
    print(fav_food)
    print()                    #for leaving a line blank after iteration