# Enter your code here. Read input from STDIN. Print output to STDOUT
num_english = int(input())
english_subscribers = set(map(int, input().split()))
num_french = int(input())
french_subscribers = set(map(int, input().split()))

both_subscriptions = english_subscribers.intersection(french_subscribers)

print(len(both_subscriptions))
