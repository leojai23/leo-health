# -*- coding: utf-8 -*-
"""Satvic Kids — plant-based recipes that kids will love (Subah Saraf)."""
from helpers import P, H2, H3, UL, OL, NOTE, TIP, recipe

ALL = ["Morning Detox Drink", "Breakfast", "Lunch", "Evening Snack", "Dinner", "An Occasional Treat"]


def bf(*names):
    return list(names)


SUBJECT = {
    "id": "kids",
    "name": "Satvic Kids",
    "tag": "Recipes Kids Will Love",
    "blurb": "Plant-based recipes for children &mdash; smoothies, smoothie bowls, salads, "
             "juices, energy balls and naturally-sweet desserts. Only ingredients that come "
             "from plants, nothing from a factory.",
    "accent": "#5aa469",
    "sections": [
        {
            "id": "basics",
            "name": "Basics",
            "pages": [
                {
                    "id": "how-to-use",
                    "title": "How to Use This Book",
                    "body": "\n".join([
                        OL([
                            "<strong>Use proper measuring cups and spoons.</strong> Normal home "
                            "cups and spoons will not give the desired taste and texture.",
                            "<strong>If making conversions, follow the chart:</strong> "
                            "&frac14; cup = 4 tablespoons; &frac12; cup = 8 tablespoons; "
                            "1 tablespoon = 3 teaspoons; 1 pinch = 1/16 teaspoon.",
                            "<strong>Always soak nuts &amp; seeds in water before using.</strong> "
                            "Unsoaked nuts are very difficult to digest &mdash; soak for at least "
                            "6 hours, or overnight.",
                        ]),
                        P("The recipes use only ingredients that come from plants &mdash; no animals "
                          "or animal products, and nothing made in a factory. Read the recipes, but "
                          "also feel free to be creative and use your imagination!"),
                    ]),
                },
                {
                    "id": "coconut-milk",
                    "title": "How to Make Coconut Milk",
                    "body": OL([
                        "Take 1 cup of fresh coconut, cut into pieces.",
                        "Combine it with 2 cups of water in a blender.",
                        "Blend until smooth.",
                        "Pour the mixture over a bowl covered with a nut milk bag or a muslin cloth.",
                        "Squeeze out the milk with your hands. You can use the leftover pulp as a face scrub.",
                        "Milk can be used immediately or stored in the refrigerator for up to 1&ndash;2 days.",
                    ]),
                },
                {
                    "id": "almond-milk",
                    "title": "How to Make Almond Milk",
                    "body": OL([
                        "Soak 1 cup of almonds in water for at least 6 hours, or overnight.",
                        "In a blender, add 2 cups of drinking water along with 1 cup of soaked almonds.",
                        "Blend the almonds and water together until smooth.",
                        "Pour the mixture over a bowl covered with a nut milk bag or a muslin cloth.",
                        "Squeeze out the milk with your hands.",
                        "Milk can be used immediately or stored in the refrigerator for up to 1&ndash;2 days.",
                    ]),
                },
                {
                    "id": "peanut-almond-butter",
                    "title": "How to Make Peanut &amp; Almond Butter",
                    "body": "\n".join([
                        H2("Peanut butter"),
                        OL([
                            "Heat a pan, add 1 cup of peanuts and reduce flame to low. Roast for "
                            "5&ndash;7 minutes, continuously stirring.",
                            "Transfer to a blender or food processor and blend for 4&ndash;5 minutes "
                            "till you get a creamy butter. Do not add any water.",
                            "It will feel like it&rsquo;ll never blend, but be patient &mdash; the "
                            "peanuts first turn to powder, then creamy. Store in the refrigerator.",
                        ]),
                        H2("Almond butter"),
                        P("Same method as peanut butter, using 1 cup of almonds in place of peanuts."),
                    ]),
                },
                {
                    "id": "peanut-curd",
                    "title": "How to Make Peanut Curd",
                    "body": OL([
                        "Soak 1 cup of raw peanuts overnight. Drain &amp; rinse well. Grind with 3 "
                        "cups water till smooth. Pour into a muslin cloth and squeeze out the peanut milk.",
                        "Transfer the peanut milk to a saucepan and bring to a boil on medium heat. "
                        "It will thicken slightly. Remove from the stove and let it cool down.",
                        "To set the curd, take 2 green chilis, remove their crowns and drop them "
                        "into the milk. Make a small slit in the remaining chilis and drop those "
                        "in too. Cover and keep aside for 12 hours &mdash; it sets into a jelly-like "
                        "substance. Discard the chili pieces and blend the curd until smooth.",
                    ]),
                },
                {
                    "id": "cashew-cheese",
                    "title": "Cashew Cheese",
                    "body": recipe(
                        groups=[(None, ["&frac12; cup cashews, soaked",
                                        "&frac12; cup roughly chopped bell pepper",
                                        "1 tablespoon lemon juice",
                                        "&frac14; small green chili",
                                        "&frac14; teaspoon salt"])],
                        method=["Process all ingredients together in a blender until smooth. "
                                "Serve as a dip with raw veggies, salads and crackers."],
                    ),
                },
                {
                    "id": "pumpkin-hummus",
                    "title": "Pumpkin Hummus",
                    "body": recipe(
                        groups=[(None, ["1 cup pumpkin, steamed",
                                        "2 tablespoons cashews, crushed",
                                        "1 teaspoon white sesame seeds, roasted",
                                        "&frac14; cup coriander, chopped",
                                        "&frac14; teaspoon salt"])],
                        method=["Mash the pumpkin with a mortar and pestle.",
                                "Add the other ingredients and continue breaking them down with "
                                "the mortar and pestle until well combined. Enjoy."],
                    ),
                },
            ],
        },
        {
            "id": "breakfast",
            "name": "Breakfast",
            "pages": [
                {
                    "id": "pineapple-smoothie",
                    "title": "Pineapple Smoothie",
                    "body": recipe(
                        meta="Serves 1",
                        intro=["Replace packaged-powder drinks with these smoothies, made from "
                               "fresh fruits and vegetables straight from the farm."],
                        groups=[(None, ["1 cup pineapple chunks", "1 cup coconut milk",
                                        "&frac12; medium banana", "&frac14; cup ice cubes",
                                        "2 dates, seedless",
                                        "&frac18; teaspoon vanilla bean powder (optional)"])],
                        method=["Place everything into a blender and blend until smooth. Serve."],
                    ),
                },
                {
                    "id": "banana-date-shake",
                    "title": "Banana Date Shake",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["1&frac12; cups coconut milk", "3 bananas",
                                        "6 dates, seedless", "4 ice cubes",
                                        "&frac12; teaspoon cinnamon powder"])],
                        method=["Place coconut milk, bananas, dates, ice and cinnamon into a "
                                "blender and blend until smooth. Serve."],
                    ),
                },
                {
                    "id": "tropical-smoothie",
                    "title": "Tropical Smoothie",
                    "body": recipe(
                        meta="Serves 1",
                        groups=[(None, ["1 cup coconut water", "1 cup chopped spinach",
                                        "1 cup chopped apple", "1 cup mango chunks",
                                        "&frac12; teaspoon lemon juice"])],
                        method=["Place all the ingredients into a blender and blend until smooth.",
                                "Let the smoothie cool in the refrigerator for about 20 minutes "
                                "before serving."],
                        notes=["Note: If mango is out of season, replace it with 1 cup chopped "
                               "guava and 2 seedless dates."],
                    ),
                },
                {
                    "id": "chocolate-smoothie-bowl",
                    "title": "Chocolate Smoothie Bowl",
                    "body": recipe(
                        meta="Serves 1",
                        groups=[(None, ["2 frozen bananas", "&frac14; cup coconut milk",
                                        "3 dates, seedless",
                                        "1 tablespoon homemade almond or peanut butter",
                                        "1 tablespoon cacao powder"]),
                                ("Topping", ["any seasonal fruits &amp; nuts"])],
                        method=["Place all the ingredients into a blender and blend until smooth.",
                                "Pour into bowls and top with fresh seasonal fruits and nuts of "
                                "your choice."],
                        prep=["Peel, slice and freeze the bananas for about 6 hours.",
                              "Prepare coconut milk and almond / peanut butter."],
                        notes=["Tip: Freeze the bananas for at least 6 hours or you won&rsquo;t get "
                               "a good texture.",
                               "Tip: CACAO is very different from COCOA &mdash; use CACAO powder."],
                        bestfor=bf("Breakfast", "Evening Snack", "An Occasional Treat"),
                    ),
                },
                {
                    "id": "blush-smoothie-bowl",
                    "title": "Blush Smoothie Bowl",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["2 frozen bananas", "3 chopped soft pears",
                                        "&frac12; cup chopped beetroot"]),
                                ("Topping", ["any seasonal fruits &amp; nuts"])],
                        method=["Place all the ingredients into a blender and blend until smooth.",
                                "Pour into bowls and top with fresh seasonal fruits and nuts."],
                        prep=["Peel, slice and freeze the bananas for about 6 hours."],
                        notes=["Note: In case pear is not available, use soft apples.",
                               "Tip: Use the soft, ripe variety of pears &mdash; hard pears won&rsquo;t "
                               "taste nice in the base."],
                        bestfor=bf("Breakfast", "Evening Snack"),
                    ),
                },
                {
                    "id": "green-smoothie-bowl",
                    "title": "Green Smoothie Bowl",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["4 frozen bananas", "&frac34; cup shredded coconut",
                                        "2 cups spinach", "4 dates, seedless",
                                        "&frac12; teaspoon cinnamon powder",
                                        "2 teaspoons lemon juice"]),
                                ("Topping", ["any seasonal fruits &amp; nuts"])],
                        method=["Place all the ingredients in a blender and blend until smooth.",
                                "Pour into bowls and top with fresh seasonal fruits and nuts."],
                        prep=["Peel, slice and freeze the bananas for about 6 hours."],
                        bestfor=bf("Breakfast", "Evening Snack"),
                    ),
                },
                {
                    "id": "cinnamon-smoothie-bowl",
                    "title": "Cinnamon Smoothie Bowl",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["3 bananas, frozen", "1 cup coconut milk",
                                        "1&frac12; tablespoon almond butter",
                                        "1 tablespoon flaxseeds", "4 dates, seedless",
                                        "&frac14; teaspoon cinnamon powder",
                                        "&frac14; teaspoon vanilla powder (optional)"]),
                                ("Topping", ["any seasonal fruits &amp; nuts"])],
                        method=["Place all the ingredients in a blender and blend until smooth.",
                                "Pour into bowls and top with fresh seasonal fruits and nuts."],
                        prep=["Prepare 1 cup coconut milk and almond butter.",
                              "Peel, slice and freeze the bananas for about 6 hours."],
                        bestfor=bf("Breakfast", "Evening Snack"),
                    ),
                },
                {
                    "id": "marigold-smoothie-bowl",
                    "title": "Marigold Smoothie Bowl",
                    "body": recipe(
                        meta="Serves 1",
                        groups=[(None, ["1&frac12; cup frozen papaya", "1 frozen banana",
                                        "3 dates, seedless", "6 strands saffron",
                                        "&frac14; cup coconut milk"]),
                                ("Topping", ["any seasonal fruits &amp; nuts"])],
                        method=["Place all the ingredients in a blender and blend until smooth.",
                                "Pour into bowls and top with fresh seasonal fruits and nuts."],
                        prep=["Peel, slice and freeze the papaya and banana for about 6 hours."],
                        bestfor=bf("Breakfast", "Evening Snack"),
                    ),
                },
                {
                    "id": "chia-pudding",
                    "title": "Chia Pudding",
                    "body": recipe(
                        meta="Serves 2&ndash;3",
                        groups=[(None, ["1 cup coconut milk",
                                        "1&frac12; tablespoon powdered jaggery",
                                        "&frac12; ripe banana", "&frac18; teaspoon rock salt",
                                        "2 tablespoons chia seeds",
                                        "1 cup chopped mixed fruits (banana, mango, grapes, pear, "
                                        "kiwi, orange, pomegranate, berries)"]),
                                ("Garnish", ["edible flowers (optional)", "fresh seasonal fruits"])],
                        method=["Place coconut milk, jaggery, banana and salt into a blender and "
                                "blend until smooth.",
                                "Pour over the chia seeds and let them soak for about 3 hours on "
                                "the kitchen counter &mdash; they swell up and thicken the mixture.",
                                "Add the chopped fruits. Refrigerate for 30 minutes before serving."],
                        prep=["Prepare coconut milk."],
                        bestfor=bf("Breakfast", "Evening Snack"),
                    ),
                },
            ],
        },
        {
            "id": "drinks",
            "name": "Drinks",
            "pages": [
                {
                    "id": "thandai",
                    "title": "Thandai",
                    "body": recipe(
                        meta="Serves 3",
                        groups=[(None, ["8 almonds, soaked in water &amp; drained",
                                        "1 tablespoon fennel, soaked 1 hour &amp; drained",
                                        "1 tablespoon poppy seeds, soaked 1 hour &amp; drained",
                                        "1&frac12; cups coconut milk", "&frac12; cup water",
                                        "4 dates, seedless",
                                        "1 teaspoon powdered jaggery",
                                        "&frac18; teaspoon rock salt",
                                        "&frac18; teaspoon black pepper"]),
                                ("Garnish", ["chopped pistachio, saffron &amp; dried rose petals"])],
                        method=["Place everything except coconut milk into a blender and blend until smooth.",
                                "Add coconut milk and blend again.",
                                "Let the drink cool in the refrigerator for a while. Garnish and serve."],
                    ),
                },
                {
                    "id": "coconut-chaas",
                    "title": "Coconut Chaas",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["2 cups coconut milk", "1 cup water",
                                        "&frac14; cup mint leaves",
                                        "2&frac12; tablespoon lemon juice",
                                        "1 teaspoon rock salt",
                                        "1 teaspoon roasted cumin powder (bhuna jeera)"])],
                        method=["Place everything except the roasted cumin powder into a blender "
                                "and blend until smooth.",
                                "Add the roasted cumin powder from the top and stir well. Cool in "
                                "the refrigerator for a while and serve."],
                    ),
                },
                {
                    "id": "pink-power-juice",
                    "title": "Pink Power Juice",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["3 cups chopped apples", "1 cup chopped beetroot",
                                        "2 cups chopped carrot", "2 cups chopped cucumber",
                                        "3 coins ginger", "2 teaspoons lemon juice"])],
                        method=["Juice all the ingredients together.",
                                "Add the lemon juice from the top and serve."],
                        notes=["Note: You can replace apples with pears."],
                    ),
                },
                {
                    "id": "glowing-green-juice",
                    "title": "Glowing Green Juice",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["2 cups chopped cucumber", "1 cup chopped bottle gourd",
                                        "1 cup roughly chopped spinach, tightly packed",
                                        "&frac14; cup mint leaves, tightly packed",
                                        "2 cups chopped apple", "1 teaspoon lemon juice"])],
                        method=["Juice all the ingredients together.",
                                "Add the lemon juice from the top and serve."],
                        notes=["Tip: When juicing leafy greens like spinach and mint, alternate "
                               "them with watery ingredients such as cucumber and apple to keep "
                               "the juicer moving."],
                    ),
                },
                {
                    "id": "clean-carrot-juice",
                    "title": "Clean Carrot Juice",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["2 cups chopped carrots", "3 cups chopped papaya",
                                        "2 oranges", "1 coin ginger"])],
                        method=["Juice all the ingredients together and serve."],
                        notes=["Note: You can replace oranges with kinnow."],
                    ),
                },
            ],
        },
        {
            "id": "salads",
            "name": "Salads",
            "pages": [
                {
                    "id": "carrot-raisin-salad",
                    "title": "Carrot Raisin Salad",
                    "body": recipe(
                        meta="Serves 2",
                        groups=[(None, ["3 cups shredded carrots",
                                        "1 cup homegrown vegetable sprouts (alfalfa, clover, radish)",
                                        "2 tablespoon finely chopped mint",
                                        "&frac14; cup soaked cashews, chopped",
                                        "3 tablespoons raisins (kishmish)"]),
                                ("Tahini Dressing",
                                 ["1 cup white sesame seeds or 4 tablespoons homemade tahini",
                                  "&frac12; cup water", "4 dates, seedless",
                                  "2 tablespoons lemon juice",
                                  "1 tablespoon powdered jaggery",
                                  "&frac14; green chili", "&frac12; teaspoon rock salt"])],
                        method=[("Tahini",
                                 ["Toast the sesame seeds in a saucepan over medium heat, stirring "
                                  "constantly, until fragrant and very lightly coloured (not brown), "
                                  "3&ndash;5 minutes. They burn quickly.",
                                  "Once completely cooled, blend to a smooth paste, about 30 seconds."]),
                                ("Salad",
                                 ["Blend 4 tablespoons tahini with water, dates, lemon juice, "
                                  "jaggery, chili and salt until smooth.",
                                  "Place the carrots, sprouts, mint, cashews and raisins in a large "
                                  "mixing bowl. Pour the dressing on top and enjoy."])],
                        prep=["Prepare vegetable sprouts."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
                {
                    "id": "cheesy-salad",
                    "title": "Cheesy Salad",
                    "body": recipe(
                        meta="Serves 2",
                        intro=["We don&rsquo;t need real cheese for a cheesy flavour &mdash; blend "
                               "soaked cashews with flavourings and it tastes even better than Parmesan."],
                        groups=[(None, ["&frac12; cup cashews, soaked", "&frac14; cup coconut milk",
                                        "&frac12; small green chili", "1 cup broccoli florets",
                                        "1 cup thinly sliced baby corn",
                                        "1 cup chopped red bell pepper",
                                        "1 cup chopped yellow bell pepper",
                                        "1 teaspoon rock salt",
                                        "1 tablespoon dried oregano leaves"])],
                        method=["Blend the cashews, coconut milk and green chili until smooth.",
                                "Steam the broccoli, bell peppers and baby corn together for about "
                                "5 minutes.",
                                "Pour the blended mixture into a mixing bowl. Add the steamed "
                                "vegetables, salt and oregano.",
                                "Mix well and serve."],
                        prep=["Soak cashews in water for 6 hours.", "Prepare coconut milk."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
                {
                    "id": "thai-papaya-salad",
                    "title": "Thai Papaya Salad",
                    "body": recipe(
                        meta="Serves 2&ndash;3",
                        groups=[(None, ["&frac12; small unripe green papaya", "1 large mango",
                                        "1 medium carrot", "2 medium tomatoes",
                                        "&frac12; cup fresh coriander"]),
                                ("Peanut Dressing",
                                 ["2 tablespoons soaked peanuts", "1 tablespoon lemon juice",
                                  "&frac18; small green chili", "&frac12; teaspoon rock salt",
                                  "1 tablespoon jaggery", "2 tablespoons water"]),
                                ("Topping", ["1 tablespoon roasted peanuts, chopped"])],
                        method=["Peel the skin of the papaya.",
                                "Cut the papaya and carrot into thin long strips (a julienne peeler "
                                "works well).",
                                "Cut the mango and tomatoes into thin long strips with a knife.",
                                "Place the papaya, carrot, mango, tomatoes and coriander in a large "
                                "bowl and mix well.",
                                "Blend all the dressing ingredients until smooth.",
                                "Combine the dressing with the salad and mix well.",
                                "Top with chopped peanuts for an extra crunch."],
                        prep=["Soak raw peanuts in water for about 3 hours."],
                        notes=["Tip: Use the unripened green papaya &mdash; firm, green outside and "
                               "pale yellow inside &mdash; not the soft ripe orange one."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
                {
                    "id": "moong-bowl",
                    "title": "Moong Bowl",
                    "body": recipe(
                        meta="Serves 3",
                        groups=[(None, ["&frac12; cup split moong dal with skin",
                                        "1&frac12; cup finely chopped fresh fenugreek (methi) leaves",
                                        "1 cup finely chopped coriander",
                                        "1&frac12; cup diced apple",
                                        "1&frac12; cup chopped grapes",
                                        "1&frac12; cup pomegranate",
                                        "2 tablespoons chia seeds",
                                        "2 tablespoons pumpkin seeds",
                                        "2 tablespoons white sesame seeds"]),
                                ("Flavoring",
                                 ["1 teaspoon grated fresh ginger", "2 tablespoons lemon juice",
                                  "1 teaspoon rock salt", "1 green chili, crushed",
                                  "&frac18; teaspoon asafoetida (hing)"])],
                        method=["Place the moong dal, methi, coriander, apple, grapes, pomegranate, "
                                "chia, pumpkin and sesame seeds into a large mixing bowl. Mix well.",
                                "Mix all the flavoring ingredients together in a small bowl so they "
                                "infuse.",
                                "Add the flavouring to the rest of the ingredients, mix well and serve."],
                        prep=["Soak split moong dal in water for about 4 hours."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
                {
                    "id": "sweet-potato-salad",
                    "title": "Sweet Potato Salad",
                    "body": recipe(
                        meta="Serves 2&ndash;3",
                        groups=[(None, ["1 medium sweet potato, steamed",
                                        "2 cups lettuce leaves, torn into pieces",
                                        "1&frac12; cup broccoli, cut into florets",
                                        "&frac14; small red bell pepper, thinly sliced then halved",
                                        "&frac14; small yellow bell pepper, thinly sliced then halved",
                                        "1 tablespoon dry rosemary"]),
                                ("For marinating sweet potato",
                                 ["1 tablespoon lemon juice", "&frac14; teaspoon black pepper",
                                  "&frac12; teaspoon salt"]),
                                ("Tomato Salsa Dressing",
                                 ["2 cups frozen tomatoes, peeled &amp; seedless",
                                  "&frac14; cup coriander",
                                  "1 tablespoon chopped red bell pepper",
                                  "&frac12; teaspoon roasted cumin powder",
                                  "&frac12; teaspoon lemon juice", "&frac12; green chili, chopped",
                                  "&frac12; teaspoon rock salt", "&frac18; teaspoon black pepper"]),
                                ("Topping", ["2 tablespoons dry roasted almonds, chopped finely"])],
                        method=[("Salad",
                                 ["Peel the steamed sweet potato and mash with a fork.",
                                  "Mix in the rosemary, then shape the mash into small cubes.",
                                  "Mix the marination ingredients and dip the cubes till coated on "
                                  "all sides.",
                                  "Dip the broccoli florets in water heated on a medium flame for "
                                  "about 10 minutes.",
                                  "Combine the lettuce, bell peppers, steamed broccoli and "
                                  "marinated sweet potato in a mixing bowl."]),
                                ("Dressing",
                                 ["Blend all the dressing ingredients &mdash; keep it a little "
                                  "chunky, don&rsquo;t over-blend. Refrigerate before use.",
                                  "Pour over the salad, top with toasted almonds and enjoy."])],
                        prep=["Freeze the tomatoes for about 40&ndash;50 minutes for a refreshing "
                              "salsa flavour."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
                {
                    "id": "nori-rolls",
                    "title": "Nori Rolls",
                    "body": recipe(
                        meta="Makes 9 pieces (3 rolls)",
                        groups=[(None, ["4 nori sheets", "4 lettuce leaves",
                                        "2 cups homegrown sprout mix",
                                        "1 small cucumber, cut lengthwise",
                                        "1 small carrot, cut lengthwise",
                                        "1 red bell pepper, cut lengthwise",
                                        "&frac14; red cabbage, cut lengthwise",
                                        "1 avocado (optional), peeled and cut lengthwise"]),
                                ("Peanut Dressing",
                                 ["2 tablespoons peanuts, soaked", "1 tablespoon lemon juice",
                                  "&frac18; small green chili", "&frac12; teaspoon rock salt",
                                  "1 tablespoon jaggery", "&frac18; cup water"])],
                        method=["Place a nori sheet shiny side down on a bamboo mat. At the bottom "
                                "half, place a lettuce leaf.",
                                "Add a handful of the sprout mix, cucumber, carrot, bell pepper, "
                                "cabbage and avocado.",
                                "Wrap the roll tightly, using a little water to seal the ends.",
                                "Cut each roll into 3 pieces with a sharp knife.",
                                "Blend all the dressing ingredients together. Add inside the roll "
                                "or serve alongside."],
                        prep=["Soak raw peanuts in water for about 3 hours."],
                        notes=["Note: Nori sheets are easily available online."],
                        bestfor=bf("Lunch", "Dinner"),
                    ),
                },
            ],
        },
        {
            "id": "snacks-desserts",
            "name": "Snacks &amp; Desserts",
            "pages": [
                {
                    "id": "energy-balls",
                    "title": "Energy Balls",
                    "body": recipe(
                        meta="Makes 10 balls",
                        groups=[("Balls",
                                 ["1 cup fresh coconut, shredded", "&frac14; cup almonds, soaked",
                                  "&frac12; cup dates, soaked", "&frac12; teaspoon cinnamon",
                                  "&frac12; teaspoon cardamom", "2 thin coins of ginger",
                                  "&frac14; teaspoon rock salt"]),
                                ("Topping",
                                 ["&frac14; cup poppy seeds", "&frac14; cup coconut, shredded"])],
                        method=["Place all the ball ingredients in a food processor and process "
                                "until you reach a mouldable consistency.",
                                "Shape into small balls.",
                                "Roll the balls in the toppings of your choice.",
                                "Refrigerate for about 4 hours and enjoy."],
                        bestfor=bf("Evening Snack", "An Occasional Treat"),
                    ),
                },
                {
                    "id": "satvic-ladoo",
                    "title": "Satvic Ladoo",
                    "body": recipe(
                        meta="Makes 12 ladoos",
                        groups=[(None, ["1 dry coconut (gola)", "2 tablespoons almond butter",
                                        "2 tablespoons powdered jaggery",
                                        "2 tablespoons soaked almonds, chopped",
                                        "2 tablespoons dry rose petals"])],
                        method=["Break the dry coconut into pieces and shred it finely.",
                                "Blend the shredded coconut in a high-speed blender until creamy, "
                                "scraping down the sides as needed. It first turns to powder, then "
                                "soft and buttery &mdash; usually 5&ndash;7 minutes. Let it cool if "
                                "it overheats.",
                                "Add the coconut butter to a bowl with the almond butter, jaggery, "
                                "chopped almonds and rose petals. Mix well with your hands.",
                                "Shape into small ladoos. Garnish with dry rose petals and enjoy."],
                        prep=["Prepare almond butter.", "Soak the almonds in water for 5&ndash;6 hours."],
                        bestfor=bf("Evening Snack", "An Occasional Treat"),
                    ),
                },
                {
                    "id": "satvic-kheer",
                    "title": "Satvic Kheer",
                    "body": recipe(
                        meta="Serves 4&ndash;5",
                        intro=["Kheer that is healthy &mdash; no sugar, no milk, no ghee, just "
                               "wholesome ingredients straight from nature."],
                        groups=[(None, ["1 cup soaked almonds", "&frac12; cup quinoa",
                                        "3&frac12; cups water",
                                        "6 tablespoons powdered jaggery",
                                        "&frac14; teaspoon cardamom powder",
                                        "20 strands of saffron", "&frac18; teaspoon rock salt"]),
                                ("Topping",
                                 ["1 tablespoon chopped almonds", "1 tablespoon chopped pistachios",
                                  "1 tablespoon raisins"])],
                        method=["Place the quinoa in a saucepan with 2 cups water and bring to a "
                                "boil. Simmer about 45 minutes until fully cooked.",
                                "Meanwhile, blend the peeled almonds with 1&frac12; cups water "
                                "until very smooth.",
                                "Add jaggery, cardamom, saffron and salt and blend again.",
                                "Pour into a bowl, add the boiled quinoa and stir well.",
                                "Refrigerate at least 30 minutes &mdash; the quinoa swells and the "
                                "kheer thickens.",
                                "Top with almonds, pistachios and raisins and enjoy."],
                        prep=["Soak the almonds in water for about 6 hours, then peel them."],
                        bestfor=bf("An Occasional Treat"),
                    ),
                },
                {
                    "id": "kulfi",
                    "title": "Kulfi",
                    "body": recipe(
                        meta="Serves 2&ndash;3, makes 1&frac12; cups",
                        groups=[("Kulfi Ice Cream",
                                 ["&frac12; cup soaked cashews", "1 cup coconut malai",
                                  "&frac14; cup jaggery, powdered", "4 dates, seedless",
                                  "&frac13; cup coconut water", "10 strands of saffron",
                                  "&frac18; teaspoon green cardamom powder",
                                  "&frac18; teaspoon rock salt"]),
                                ("Topping", ["1 tablespoon chopped pistachios"])],
                        method=["Blend all the ice cream ingredients until smooth.",
                                "Pour into a shallow glass dish or steel container and freeze for "
                                "about 6 hours.",
                                "Before serving, let it thaw on the counter for 15&ndash;30 minutes "
                                "until soft enough to scoop.",
                                "Top with chopped pistachios and serve."],
                        prep=["Soak the cashews in water for about 6 hours."],
                        bestfor=bf("An Occasional Treat"),
                    ),
                },
                {
                    "id": "peanut-butter-ice-cream",
                    "title": "Peanut Butter Ice Cream",
                    "body": recipe(
                        meta="Serves 3",
                        groups=[(None, ["6 dates, seedless", "&frac14; cup water",
                                        "4 frozen bananas", "1 tablespoon peanut butter",
                                        "&frac12; tablespoon powdered jaggery",
                                        "&frac18; teaspoon rock salt"]),
                                ("Topping",
                                 ["1 tablespoon almonds, chopped",
                                  "1 tablespoon date paste (optional)", "few banana slices"])],
                        method=["Blend the dates and water into a paste.",
                                "Add the frozen bananas, peanut butter, jaggery and salt and blend "
                                "again until smooth. Do not over-blend.",
                                "Scoop into bowls, top with almonds, date paste and banana slices, "
                                "and serve immediately soft-serve style."],
                        prep=["Prepare peanut butter.",
                              "Peel, slice and freeze the bananas for about 6 hours."],
                        bestfor=bf("An Occasional Treat"),
                    ),
                },
                {
                    "id": "sweet-potato-brownie",
                    "title": "Sweet Potato Brownie",
                    "body": recipe(
                        groups=[("Brownie",
                                 ["2 cups mashed sweet potato, steamed until soft",
                                  "&frac12; cup almond butter",
                                  "&frac12; cup cacao powder (very different from cocoa)",
                                  "&frac14; cup jaggery syrup (melt jaggery on a low flame)",
                                  "&frac12; cup date paste (dates blended with a little water)",
                                  "pinch of salt", "&frac14; cup water"]),
                                ("Chocolate Sauce",
                                 ["&frac13; cup jaggery", "&frac12; cup cacao powder",
                                  "&frac12; cup date paste", "&frac13; cup water"]),
                                ("Topping", ["1 tablespoon walnuts, chopped"])],
                        method=[("Brownie",
                                 ["Blend all the brownie ingredients into a smooth batter.",
                                  "Put the batter in a baking tray and bake at 215&deg;F for 30 minutes.",
                                  "Check with a fork &mdash; it should be crispy on top and soft "
                                  "inside."]),
                                ("Chocolate sauce",
                                 ["Boil water in a pan on medium flame and melt the jaggery in it.",
                                  "Add cacao powder slowly, stirring constantly for 10 minutes "
                                  "until you get a thick sauce.",
                                  "Cool, then combine with the date paste."]),
                                ("Assemble",
                                 ["Cut the brownie into squares, drizzle with chocolate sauce and "
                                  "chopped walnuts, and enjoy."])],
                        prep=["Steam 2 cups mashed sweet potato.",
                              "Make &frac12; cup almond butter.",
                              "Make jaggery syrup by melting jaggery on a low flame."],
                        bestfor=bf("An Occasional Treat"),
                    ),
                },
                {
                    "id": "lemon-cheesecake",
                    "title": "Lemon Cheesecake",
                    "body": recipe(
                        meta="Serves 5",
                        intro=["No dairy, cheese or sugar &mdash; but it does contain lots of "
                               "cashews, so eat sparingly."],
                        groups=[("Cheesecake",
                                 ["1 cup cashews, soaked", "3 tablespoons powdered jaggery",
                                  "&frac14; cup water", "3 tablespoons lemon juice"]),
                                ("Lime Gel",
                                 ["&frac14; cup cashews, soaked overnight",
                                  "&frac14; cup powdered jaggery",
                                  "4 medium leaves of spinach", "&frac12; tablespoon lemon juice",
                                  "&frac12; tablespoon lemon zest (finely grated lemon peel)"]),
                                ("Ginger Crumble",
                                 ["&frac12; cup almonds", "&frac12; tablespoon jaggery powder",
                                  "&frac14; teaspoon ginger, grated", "pinch salt"])],
                        method=["Blend all the cheesecake ingredients. Pour into a pan and chill in "
                                "the freezer 5&ndash;6 hours. Once frozen, cut into shapes and keep "
                                "refrigerated until serving.",
                                "Blend all the lime gel ingredients until perfectly smooth. Pour "
                                "into a squeeze bottle and refrigerate.",
                                "For the ginger crumble, quickly pulse the almonds, then mix in the "
                                "rest by hand.",
                                "Sprinkle 3 piles of ginger crumble on a plate, place a piece of "
                                "cheesecake on each, and garnish with lime gel, microgreens and "
                                "edible flowers."],
                        prep=["Soak the cashews in water for 5&ndash;6 hours."],
                        bestfor=bf("An Occasional Treat"),
                    ),
                },
            ],
        },
    ],
}
