# Remove all Number are duplicated from the list

numbers = [10, 9, 9, 99, 10, 11, 34]
uniques= []

for number in numbers:
    if number not in uniques:
        uniques.append(number)


print(uniques)