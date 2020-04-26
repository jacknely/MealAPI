import pandas as pd

test_recipe_load = pd.DataFrame(
    {
        "a": [1, 2],
        "title": [1, 2],
        "recipe_cuisine": ["test3", "test4"],
        "marketing_description": ["test1", "test2"],
    }
)
test_recipe_load_index = test_recipe_load.set_index("a")

a_recipe_id_test = {
    "title": 1,
    "recipe_cuisine": "test3",
    "marketing_description": "test1",
}

metatag = [
    {
        "self": "/?page=5&items=5",
        "first": "/?page=1&items=5",
        "previous": "/?page=4&items=5",
        "next": "/?page=6&items=5",
        "last": "/?page=4&items=5",
    },
    {"page": 5, "per_page": 5, "total_count": 20},
]
metatest = [(5, 5, 20, metatag)]
