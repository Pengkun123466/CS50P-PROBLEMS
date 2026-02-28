def main():
   fruit = input("Fruit: ").lower()
   calory = calories(fruit)
   if calory is not None:
    print(f"calories: {calory}")

def calories(fruit:str) -> int:
    nutrition_facts = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
    if fruit in nutrition_facts:
        fruit_calory = nutrition_facts[fruit]
        return fruit_calory 

if __name__ == "__main__":
    main()    