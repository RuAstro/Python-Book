def get_cat_with_hats(array_of_cats):
    cats_with_hats_on = []
    
for num in range(1, 100 + 1):
    for cat in range(1, 100 + 1):
        
        if cat % num == 0:
            
            if array_of_cats[cat] is True:
                array_of_cats[cat] = False
            else:
                array_of_cats[cat] = True
                
for cat in range(1, 100 + 1):
    if array_of_cats[cat] is True:
        cats_with_hats_on.append(cat)