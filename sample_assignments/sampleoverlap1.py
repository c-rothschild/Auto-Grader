print('This calculator will ask for two lists of classes.')
print('Please enter them separated with commas but no extra spaces!')

first_list_classes = input('Enter the 1st list of classes: ')
second_list_classes = input('Enter the 2cd list of classes:')

split_first_list_classes = (first_list_classes.split(','))
split_second_list_classes = (second_list_classes.split(','))


set_split_first_list_classes = set(split_first_list_classes)
set_split_second_list_classes = set(split_second_list_classes)

overlapping_classes = set_split_first_list_classes.intersection(set_split_second_list_classes) 
print(overlapping_classes)

count_overlapping_classes = len(overlapping_classes)

print(f'these two list The two lists have {count_overlapping_classes} entries in common :')
print('They are:')
print(            *overlapping_classes)




