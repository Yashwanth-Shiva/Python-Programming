def marsExploration(s):
    msg = "SOS"
    msg_len = len(s)//3
    actual_msg = msg*msg_len
    count = 0
    for i in range(len(s)):
        if s[i] != actual_msg[i]:
            count += 1
    return count

s = input()
print(marsExploration(s))
