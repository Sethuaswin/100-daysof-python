# Error handeling
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()  # type: ignore
#     print("File was closed")

# # Raising custom error
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary['sgsfe'])
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")

# Raising our own error
# Take an example of bmi
height = float(input("Height: "))
weight = int(input("Weight: "))

# If we give un realistic weight and height it will take to over come this
if height > 3:
    raise ValueError("Human Height shpuld be over 3 meters")

bmi = weight / height ** 2
print(bmi)
