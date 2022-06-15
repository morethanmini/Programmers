participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant.sort()
completion.sort()
print(participant, completion)
for i in range(len(completion)):
    if participant[i] != completion[i]:
        print(participant[i])

print(participant[-1])