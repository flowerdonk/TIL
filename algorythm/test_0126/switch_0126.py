def Woman(num, switches):
    changed_switches = switches[:]

    return changed_switches

def Man(num):
    changed_switches = switches[:]

    return changed_switches


num = int(input())
switches = list(map(int, input().split()))
member = int(input())
member_choice = list(map(int, input().split()))

if member_choice[0] == 1:
    print(Man(member_choice[1], switches))
else:
    print(Woman(member_choice[1], switches))