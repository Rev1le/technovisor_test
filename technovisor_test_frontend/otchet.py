from pandas import DataFrame

d = [
    {
        "id": 1,
        "date": "2023-04-29",
        "worker": {
            "name": "Александр"
        },
        "dishes": []
    },
    {
        "id": 2,
        "date": "2023-04-29",
        "worker": {
            "name": "Александр"
        },
        "dishes": []
    },
    {
        "id": 3,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 4,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 5,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 6,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 7,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 8,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 9,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 10,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 11,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 12,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 13,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    },
    {
        "id": 14,
        "date": "2002-08-27",
        "worker": {
            "name": "Александр"
        },
        "dishes": [
            {
                "title": "Салат \"Весенний\"",
                "composition": "Огурец, помидор, перец",
                "price": 80.0
            },
            {
                "title": "Курица с рисом",
                "composition": "Курица, рис",
                "price": 130.0
            }
        ]
    }
]

#def dishes_to_str(dishes):
#    dishes_list = list(map(lambda dish: dish['title'], dishes))


df = DataFrame(data=d)
df["worker"] = df["worker"].transform(lambda worker: worker["name"])
df["dishes"] = df["dishes"].transform(lambda dishes: ", ".join(list(map(lambda dish: dish['title'], dishes))))

del df['id']
df.replace()
df = df.rename(columns={"date": "Дата заказа", "worker": "Работник", "dishes": "Блюда"}, errors="raise")
print(df.columns)
df = df.sort_values(by=['Дата заказа'])
df.to_excel('output1.xlsx', engine='xlsxwriter', index=False) 