# Enter your code here. Read input from STDIN. Print output to STDOUT
s1 = set(input())
english_newspaper = set(map(int, input().split()))
s2 =set(input())
french_newspaper = set(map(int, input().split()))
total_number_of_students = len(english_newspaper.union(french_newspaper))
print(total_number_of_students)
