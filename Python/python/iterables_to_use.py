#DESCRIPTION:
#Here I'll only storage iterable objects that i could use in a future...
from typing import Union,Any

plushy_store_items:list[dict] = [
    {
        "product": "Giant Teddy Bear",
        "price": 49.99,
        "stock": 15,
        "extra_characteristics": {
            "material": "Soft Polyester",
            "color": "Brown",
            "size": "Large",
            "washable": True
        }
    },
    {
        "product": "Sparkle Unicorn Plush",
        "price": 25.50,
        "stock": 30,
        "extra_characteristics": {
            "material": "Glitter Fabric",
            "color": "Rainbow",
            "size": "Medium",
            "sound_feature": False
        }
    },
    {
        "product": "Mini Octopus Reversible",
        "price": 12.00,
        "stock": 50,
        "extra_characteristics": {
            "material": "Velvet",
            "color": "Pink/Blue",
            "size": "Small",
            "mood_expression": True
        }
    },
    {
        "product": "Dragon Hatchling Plush",
        "price": 35.75,
        "stock": 20,
        "extra_characteristics": {
            "material": "Felt",
            "color": "Green",
            "size": "Medium",
            "articulated_wings": True
        }
    },
    {
        "product": "Space Alien Plushie",
        "price": 18.99,
        "stock": 40,
        "extra_characteristics": {
            "material": "Fuzzy Fleece",
            "color": "Purple",
            "size": "Small",
            "glow_in_dark": True
        }
    },
    {
        "product": "Wise Owl Plush",
        "price": 29.00,
        "stock": 10,
        "extra_characteristics": {
            "material": "Knitted Fabric",
            "color": "Grey",
            "size": "Medium",
            "glasses_included": True
        }
    },
    {
        "product": "Kawaii Sushi Roll Plush",
        "price": 9.50,
        "stock": 60,
        "extra_characteristics": {
            "material": "Soft Plush",
            "color": "White/Orange",
            "size": "Mini",
            "food_themed": True
        }
    },
    {
        "product": "Mystical Phoenix Plush",
        "price": 42.25,
        "stock": 8,
        "extra_characteristics": {
            "material": "Shimmer Fabric",
            "color": "Red/Gold",
            "size": "Large",
            "poseable_tail": True
        }
    },
    {
        "product": "Sleepy Sloth Buddy",
        "price": 20.00,
        "stock": 25,
        "extra_characteristics": {
            "material": "Ultra-soft Plush",
            "color": "Beige",
            "size": "Medium",
            "hanging_feature": True
        }
    },
    {
        "product": "Robotic Companion Plush",
        "price": 30.00,
        "stock": 12,
        "extra_characteristics": {
            "material": "Synthetic Felt",
            "color": "Silver",
            "size": "Small",
            "light_up_eyes": True
        }
    }
]

_mixed_values_:tuple= (
    42,
    "hello world",
    (10, 20, 30),
    True,
    None,
    3.14159,
    ["apple", "banana", "cherry"],
    {"city": "New York", "population": 8000000},
    "Python programming",
    False,
    (50, "fifty", 50.0),
    -7,
    0.001,
    "a long string with many words",
    {"item_id": "ABC123", "status": "available"},
    ["red", "green", "blue", "yellow"],
    123456789,
    None,
    "another sentence here",
    (True, False),
    {"code": 200, "message": "Success"},
    987.654,
    "Zebra",
    [100, 200, 300, 400, 500],
    {"country": "Guatemala", "capital": "Guatemala City"},
    -0.5,
    "final entry in the tuple",
    (1, (2, 3), 4),
    float('inf'),
    "data science",
    {'key': 'value'},
    1000000,
    'single_character',
    ('a', 'b', 'c', 'd', 'e', 'f'),
    True,
    None,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "The quick brown fox jumps over the lazy dog.",
    3.14,
    {"weather": "sunny", "temperature": 25},
    (11, 12, 13, 14, 15),
    "December",
    99.99,
    False,
    ["cat", "dog", "bird"],
    float('-inf'),
    "tuple within a tuple",
    (0, 0, 0),
    {"product_id": "XYZ789", "quantity": 100},
    "programming is fun",
    1.618,
    True,
    None,
    ["alpha", "beta", "gamma", "delta"],
    "long and descriptive sentence about nothing specific",
    123,
    (100, 200),
    "another string",
    {"first": 1, "second": 2, "third": 3},
    45.67,
    False,
    None,
    None, 
    None,
    [9, 8, 7, 6, 5],
    "end of tuple"
)

random_strings_list:list = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "apple",  # Repeated
    "banana", "cherry", "dragonfruit", "elderberry", "fig",
    "grape", "honeydew", "kiwi", "lemon", "mango",
    "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon",
    "apple", "banana", "cherry", "date", "fig", # More repetitions
    "grape", "kiwi", "lemon", "mango", "orange",
    "raspberry", "strawberry", "tangerine", "vanilla", "watermelon",
    "blueberry", "cantaloupe", "durian", "guava", "lime",
    "melon", "pear", "plum", "starfruit", "apricot",
    "blackberry", "cranberry", "date", "grapefruit", "passionfruit",
    "peach", "pineapple", "pomegranate", "satsuma", "tomato"
]


sentences:tuple=(
    "The ancient map hinted at a forgotten treasure.",
    "Butterflies fluttered gracefully in the sunlit meadow.",
    "A lone wolf howled at the full moon.",
    "The old clock chimed precisely at midnight.",
    "She dreamt of flying among the stars.",
    "Rain pattered softly on the windowpane.",
    "He found an unusual seashell on the beach.",
    "The city lights twinkled like scattered diamonds.",
    "A curious cat explored the dusty attic.",
    "The aroma of fresh bread filled the kitchen.",
    "hello","bye","it's late!","i am boring","i'm hungry","let's finished this...")   

Words:list[str]=["Shoes","Duck","Jiraph","Water","Arrise","Guittar",
   "Duck","Piano","Country","Zebra","Water","Duck"]

Currency_:dict={"quetzales":7.68,"mexican pesos":18.54,"colombian pesos":4108.25,
                "peruvian soles":3.53,"yen":147.72,"brazilian reais":5.56,"euro":0.85,
                "won":1388.53
                
                }
