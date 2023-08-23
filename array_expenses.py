expenses = [2200, 2350, 2600, 2130, 2190]

#1. In Feb, how many dollars you spent extra compare to January?
print(f"spent {expenses[1] - expenses[0]} more in feb than jan")

#2. Find out your total expense in first quarter (first three months) of the year.
print(f"spent {sum(expenses[:4])} in the first trimester")

#3. Find out if you spent exactly 2000 dollars in any month
print(f"{'yes' if 2000 in expenses else 'no'} spent")

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(2000)