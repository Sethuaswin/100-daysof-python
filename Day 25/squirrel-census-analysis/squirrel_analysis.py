import pandas as pd

data = pd.read_csv("Day 25/squirrel-census-analysis/2018_Central_Park_Squirrel_Census.csv")  # noqa

gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color": [
        "Gray",
        "Cinnamon",
        "Black"
    ],
    "Count": [
        gray_squirrels_count,
        cinnamon_squirrels_count,
        black_squirrels_count
    ]
}

df = pd.DataFrame(data_dict)
df.to_csv("Day 25/squirrel-census-analysis/squirrel_count.csv")
