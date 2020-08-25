from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbproject

data = [
    {
        "menu": "스팸후라이주먹밥후라이",
        "description": "노릇노릇한 스팸, 반숙 계란후라이, 주먹밥 세트",
        "price": 11000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT-NdvLYYTkHwhZyaGGDkcZ4CnUQQ91b-JJgA&usqp=CAU"
    },
    {
        "menu": "닭똥집",
        "description": "매콤한 소스로 만든 닭똥집구이",
        "price": 13000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRJFUoLk8Lqra3FSFOFa8jT7aXqK7iRTNJwog&usqp=CAU"
    },
    {
        "menu": "오징어무침",
        "description": "반숙 통오징어와 매콤달콤한 소스의 조화",
        "price": 15000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQeWslEY80U2hhI0Om7zLuVcDrtaAeVE4LqBA&usqp=CAU"
    },
    {
        "menu": "녹두 빈대떡",
        "description": "따끈따끈 고소한 녹두 빈대떡",
        "price": 10000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTxJjlsoVbIjzJ0XHBBUhzyw6GIy7ujuMaQg&usqp=CAU"
    },
]

db.HwangPo.insert_many(data)

exit(1)
