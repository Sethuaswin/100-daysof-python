import colorgram

colors = colorgram.extract("Day 18/hirst-painting/image.jpg", 30)
color_list = []

# Extracting RGB tuples in color_list (own approach)
for color in colors:
    color_list.append(tuple(color.rgb))

# Extracting RGB tuples in color_list (instructor approach)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
print(color_list)
