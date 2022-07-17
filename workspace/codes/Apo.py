# -*- coding: utf-8 -*-

# 括号匹配
n = int(input())
s = input()
cnt = 0

for i in s:
	if i == '(':
		cnt += 1
	else:
		if cnt > 0:
			cnt -= 1
		else:
			print("No")
			exit(0)

if len(ls) > 0:
	print("No")
else:
	print("Yes")

# 节能电梯
d = float(input())
f1, f2 = map(int, input().split())
n1, n2 = map(int, input().split())
n = min(abs(f1 - n1), abs(f2 - n1)) + abs(n1 - n2)
print(n * d)

# 电话号码
def asc(phone):
	for i in range(3):
		if ord(phone[i + 1)] - ord(phone[i]) != 1:
			return 0
	return 5
	

def desc(phone):
	for i in range(3):
		if ord(phone[i]) = ord(phone[i + 1]) != 1:
			return 0
	return 5

def same1(phone):
	if phone[0] == phone[1] and phone[1] == phone[2]:
		return 3
	return 0

def same2(phone):
	if phone[1] == phone[2] and phone[2] == phone[3]:
		return 3
	return 0

def AABB(phone):
	if phone[0] == phone[1] and phone[2] == phone[3]:
		return 1
	return 0

def ABAB(phone):
	if phone[0] == phone[2] and phone[1] == phone[3]:
		return 1
	return 0
def have689(phone):
	cnt = 0
	for i in phone:
		if i == '6' or i == '8' or i == '9':
			cnt += 1
	return cnt

n = int(input())
for i in range(n):
	sum = 0
	phone = input()
	sum = asc(phone) + desc(phone) + same1(phone) + same2(phone) + AABB(phone) + ABAB(phone) + have689(phone)
	print(sum)