# with open("Day 24/my_file.txt") as f:
#     contest = f.read()
#     print(contest)

# with open("Day 24/my_file.txt", mode='a') as f: # Append mode
#     f.write("\nNew text.")

with open("../my_file.txt", mode='r') as f:  # write mode
    print(f.read())
