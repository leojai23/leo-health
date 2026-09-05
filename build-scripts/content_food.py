# -*- coding: utf-8 -*-
"""Satvic Food — The Food Book (Subah Jain / Subah Saraf). Philosophy, kitchen, meal
plans and the full recipe collection."""
from helpers import P, H2, H3, UL, OL, NOTE, TIP, QUOTE, TABLE, dl, recipe


def bf(*names):
    return list(names)


# ---------------------------------------------------------------- PHILOSOPHY ----
PHILOSOPHY = [
    {
        "id": "what-is-satvic",
        "title": "What Does Satvic Mean?",
        "body": "\n".join([
            P("Lord Krishna, in the Bhagavad Gita, states that all embodied souls work "
              "under the control of three <em>gunas</em> &mdash; modes, or qualities, of "
              "material nature. The thoughts in our head, the activities we perform, the "
              "people we meet and the food we eat can all be classified as Satvic, Rajasik "
              "or Tamasik."),
            dl([
                ("Satvic &mdash; Mode of Goodness",
                 "Purity, happiness, compassion, bliss, love, self-control, satisfaction, "
                 "non-violence, fearlessness, surrender."),
                ("Rajasik &mdash; Mode of Passion",
                 "Arrogance, ego, restlessness, anxiety, anger, impatience, fear, "
                 "uncontrollable desires, distress."),
                ("Tamasik &mdash; Mode of Ignorance",
                 "Laziness, tiredness, depression, lethargy, ignorance, apathy, inertia, illusion."),
            ]),
            P("One person can have multiple modes. When Satvic dominates, we feel happy, "
              "satisfied and in control of our senses. When Rajasik dominates, we feel "
              "restless, anxious and angry. When Tamasik dominates, we feel lazy, tired, "
              "depressed and lethargic. Our modern lifestyle, with its high stress and "
              "toxins, fluctuates between Rajasik and Tamasik &mdash; to achieve happiness "
              "we have to transcend to Satvic."),
            H2("Food in the three modes (Bhagavad Gita, Chapter 17)"),
            QUOTE("Foods in the mode of goodness increase the duration of life, purify "
                  "one&rsquo;s existence and give strength, health, happiness and "
                  "satisfaction. Such foods are juicy, fatty, wholesome, and pleasing to "
                  "the heart.", "Verse 8"),
            QUOTE("Foods that are too bitter, too sour, salty, pungent, dry and hot are "
                  "liked by people in the mode of passion. Such foods cause pain, distress "
                  "and disease.", "Verse 9"),
            QUOTE("Food cooked more than three hours before being eaten, which is tasteless, "
                  "stale, putrid, decomposed and unclean, is liked by people in the mode of "
                  "ignorance.", "Verse 10"),
            H2("Satvic food"),
            P("Foods that are fresh, wholesome (unprocessed, unrefined), juicy "
              "(water-rich), freshly cooked and lightly seasoned. It is living food, with "
              "life energy inside it &mdash; food straight from Nature, with no or minimal "
              "human interference."),
            UL(["<strong>All fresh fruits</strong> &mdash; melons, oranges, papaya, apple, "
                "pear, berries, grapes",
                "<strong>All vegetables</strong> &mdash; bottle-gourd, ridge-gourd, bell "
                "peppers, carrots, spinach, coriander, all leafy greens",
                "<strong>Whole fats</strong> &mdash; coconut, soaked nuts &amp; seeds",
                "<strong>Whole grains</strong> &mdash; whole wheat (with chokar), brown rice"]),
            H2("Rajasik food"),
            P("Foods that are too bitter, sour, salty, pungent, dry and hot &mdash; foods "
              "with excess salt and spices. Examples: excess salt, red chili, garam masala, "
              "asafoetida (heeng), vinegars; very hot water and very hot herbal tea."),
            H2("Tamasik food"),
            P("Foods that are stale (eaten more than 3 hours after cooking), rotten (meat "
              "and fish) and foul (bad-smelling). Tamasik food is dead &mdash; when we eat "
              "dead food, the same death is transferred to our body as disease. Examples: "
              "everything packaged, bottled, tinned or canned; meat, fish &amp; eggs; "
              "stimulants such as onion, garlic, tea, coffee, alcohol, cigarettes, betel "
              "nut (supaari) and betel leaf."),
        ]),
    },
    {
        "id": "effects-of-food",
        "title": "Effects of Satvic vs Rajasik &amp; Tamasik Food",
        "body": "\n".join([
            H2("Effects of Satvic food"),
            P("Satvic food is healing food. It is easy to digest, so when we eat it our "
              "body spends less time digesting and more time healing. By switching to a "
              "Satvic diet and lifestyle we can fully cure chronic disease without "
              "medicines."),
            P("The benefits go beyond the physical body. As we keep eating Satvic food, "
              "our thoughts change &mdash; it brings mental clarity, calmness and humility, "
              "and we elevate to a higher consciousness of fearlessness, becoming closer to "
              "Mother Nature and God."),
            H2("Effects of Rajasik &amp; Tamasik food"),
            P("Eating Rajasik and Tamasik food ruins both bodily and mental health. Over "
              "time we become a victim of diabetes, obesity, high blood pressure, PCOD, "
              "high cholesterol, joint pains and more."),
            P("On a subtler level, they impact our thoughts &mdash; we become arrogant, "
              "restless, anxious and impatient, concentration decreases, and we become dull "
              "and lazy. We eat dead foods, and so our body, emotions and confidence slowly "
              "begin to die."),
            NOTE("Satvic recipes are different from other so-called &lsquo;healthy "
                 "recipes&rsquo;. They follow strict Satvic food laws and are made "
                 "especially for healing and achieving the maximum potential of the human body."),
        ]),
    },
    {
        "id": "four-principles",
        "title": "The 4 Satvic Food Principles",
        "body": "\n".join([
            P("According to the Bhagavad Gita, our food should have four qualities, "
              "abbreviated <strong>LWPW</strong>:"),
            dl([
                ("1 &mdash; Living",
                 "Our food should come straight from the farm to our kitchen, not go to a "
                 "factory in between. Nothing processed, tinned, packaged, bottled or canned."),
                ("2 &mdash; Wholesome",
                 "Our food should be unprocessed and unrefined &mdash; not subtracted of "
                 "its natural elements. Whole grains, dates and brown rice are examples."),
                ("3 &mdash; Plant-based",
                 "Our food should be derived from plants and trees, not animals. No meat, "
                 "fish or eggs."),
                ("4 &mdash; Water-rich",
                 "Our food should be juicy, containing a high amount of water &mdash; "
                 "fruits, vegetables, leafy greens. Nuts, seeds and grains are water-poor."),
            ]),
        ]),
    },
    {
        "id": "living",
        "title": "Principle 1 &mdash; Living Food",
        "body": "\n".join([
            P("Living foods come straight from Nature, without cooking or processing "
              "&mdash; eaten in their pristine, raw state. Take a wheat seed, bury it and "
              "water it, and it grows into a sapling. Plant wheat noodles, and nothing "
              "grows &mdash; they contain no life energy, or <em>prana</em>. They are "
              "dead. How can something dead bring life to our body?"),
            P("Fruits, vegetables, sprouts, coconut, grains, nuts and seeds (if soaked) are "
              "all living foods. When they enter our body they transfer their life energy, "
              "flush out toxins and cure disease."),
            H2("The 3-hour rule"),
            P("According to the Bhagavad Gita (17.10), food should be eaten within 3 hours "
              "of being cooked. After 3 hours it starts to lose its life energy and becomes "
              "Tamasik. If something is cooked on fire, eat it within 3 hours, maximum 5. "
              "Never store cooked food in the refrigerator to eat over several days."),
            P("But why apply the 3-hour rule only to sabzi and chapati? Processed biscuits, "
              "chips, candies, snacks and namkeens were often cooked years in advance and "
              "stored with synthetic chemicals and preservatives. These may increase the "
              "shelf life of the product, but they decrease the shelf life of our body."),
            NOTE("Eat nothing frozen, tinned, packaged or bottled. Eat fruits, vegetables, "
                 "coconut, sprouts, nuts &amp; seeds &mdash; straight from Nature."),
            H2("Sun-cooked, not uncooked"),
            P("At least 70% of the daily diet should be raw &mdash; fruits, vegetables, "
              "salads, smoothies, juices, sprouts. &lsquo;Sun-cooked&rsquo; is a better "
              "term than &lsquo;raw&rsquo;: a fruit ripening on the tree has been cooked by "
              "Mother Nature under the sun. By cooking it on the stove, we&rsquo;re "
              "re-heating it."),
            P("When we cook food on fire, the first thing to go is the vital sun-energy; "
              "the second is the enzymes that make digestion possible. At 118&deg;F "
              "(47.8&deg;C), food enzymes begin to die and the food loses nutritional "
              "value. If you must cook, cook at the lowest temperature for the shortest "
              "time. Steaming is better than boiling."),
            QUOTE("Kill neither men, nor beasts, nor yet the food which goes into your "
                  "mouth. For if you eat living food, the same will quicken you, but if you "
                  "kill your food, the dead food will kill you also.",
                  "Jesus, Essene Gospel of Peace"),
        ]),
    },
    {
        "id": "wholesome",
        "title": "Principle 2 &mdash; Wholesome Food",
        "body": "\n".join([
            P("There is a reason Mother Nature hung dates on trees and not sugar; gives us "
              "coconut and not coconut oil, potatoes and not potato chips. All foods that "
              "come directly from plants and trees are wholesome &mdash; they have not been "
              "subtracted of anything."),
            P("Nature gives each food a specific ratio of protein, fats and nutrients so we "
              "can easily digest and eliminate it. If we fragment it &mdash; consuming only "
              "a part, stripping the outer layer, squeezing the oil out &mdash; we spoil "
              "Nature&rsquo;s design. If Nature gives us rice, she gives us the mechanism of "
              "digesting that rice in the bran that covers it. Throw out the bran and you "
              "throw away the digestive mechanism."),
            P("White rice, sugar, oil, refined flours and refined wheat are all highly "
              "fragmented. Corn on the cob is whole; cornmeal is still whole; dextrose is "
              "not whole; high-fructose corn syrup is the king of not being whole."),
            UL(["Eat <strong>brown rice</strong> instead of white rice.",
                "Eat <strong>dates or jaggery</strong> instead of sugar.",
                "Eat <strong>whole coconut</strong> instead of coconut oil; the whole "
                "almond instead of almond oil.",
                "Eat <strong>whole wheat with the chokar</strong> (bran) &mdash; do not "
                "sieve the flour before making chapatis."]),
        ]),
    },
    {
        "id": "plant-based",
        "title": "Principle 3 &mdash; Plant-Based Food",
        "body": "\n".join([
            P("Nature constructs every organism as either a carnivore or a herbivore. By "
              "looking at our own physical features, we can judge which we are designed to be."),
            TABLE(["", "Carnivore", "Human (herbivore)"], [
                ["Teeth", "Sharp, pointed teeth to tear meat", "Flat teeth, incapable of tearing flesh"],
                ["Nails", "Sharp, pointed claws to rip flesh", "Flat, dull nails; fingers to grab and peel"],
                ["Intestine length", "Short &mdash; 3&ndash;6&times; body length, so meat exits before it rots",
                 "Long &mdash; ~12&times; body length; meat sits, rots and creates toxicity"],
                ["Stomach acidity", "Very strong hydrochloric acid to break down meat",
                 "Hydrochloric acid ~20&times; weaker than carnivores"],
                ["Vision", "Night vision to hunt prey", "No night vision"],
            ]),
            P("If Nature had designed meat as our food, wouldn&rsquo;t she have given us "
              "sharp nails and teeth, shorter intestines, strong acid and night vision? "
              "Nature does not make mistakes."),
            H2("Toxicity in animal sweat"),
            P("Animals about to be slaughtered sweat profusely from fear; large amounts of "
              "toxins are released and retained in the layers between the animal&rsquo;s "
              "skin. Eating meat means eating not just the flesh but all the toxins in its "
              "body, giving rise to inflammation, pain and degenerative ailments."),
            H2("Affects of meat on the mind"),
            P("Food has consciousness. Factory-farmed animals are kept in darkness and "
              "squeezed into cages. If we eat their flesh, their pain, exhaustion and "
              "sorrow is transferred to us, and our body accumulates that death energy as "
              "anger, violence, depression and illness."),
            H2("Where will I get my protein?"),
            P("Overconsumption of protein is a far greater threat to health than not "
              "getting enough. Protein is a building block, needed for growth &mdash; "
              "during childhood, adolescence, for athletes and pregnant women. In "
              "adulthood, and in a sedentary lifestyle, our need is minimal and easily met "
              "by leafy greens, vegetables, fruits, coconut, sprouts, nuts and grains. "
              "Excess makes us prone to cysts, stones, fibroids and disturbed blood "
              "chemistry. Every animal we eat &lsquo;for protein&rsquo; is itself a "
              "vegetarian animal."),
            H2("Milk &mdash; to drink or not to drink?"),
            P("There are three problems with animal milk:"),
            OL([
                "<strong>Commercial milk is highly adulterated</strong> &mdash; treated "
                "with contaminants such as urea, starch, caustic soda, detergents, white "
                "paint and refined oil.",
                "<strong>Cows are often mistreated and tortured</strong> &mdash; tied in "
                "one corner, separated from their calves, injected with hormones to keep "
                "producing milk. Food carries consciousness.",
                "<strong>Milk is difficult to digest</strong> for those curing a disease "
                "or living a sedentary lifestyle. A cow&rsquo;s milk is designed to grow a "
                "90-pound calf into a 2000-pound animal; it contains excessive "
                "growth-promoting hormones.",
            ]),
            P("Vedic Milk (meeting all 8 traditional conditions &mdash; from your own or a "
              "known farm, calf&rsquo;s first right, good grass, no vaccines, only for "
              "athletes or growing children, raw or lightly boiled once, cow alone, treated "
              "as a complete meal) is nearly impossible to find today. The replacement is "
              "fresh homemade <strong>coconut milk</strong> &mdash; called &lsquo;Shree "
              "Phal&rsquo; in the Vedic scriptures, easy to digest, superior to all nuts "
              "and seeds. If fresh coconut is unavailable, use homemade almond milk."),
            H2("Plant-based replacements"),
            TABLE(["Instead of", "Use"], [
                ["Animal milk", "Homemade coconut milk (or almond milk)"],
                ["Butter, cream", "Homemade nut butter (almond &amp; peanut) &mdash; sparingly; avoid while healing"],
                ["Cheese", "Fresh coconut malai / homemade cashew cheese (soaked cashews)"],
                ["Chaas", "Satvic chaas made of coconut milk"],
                ["Ice cream", "Plant-based ice cream made with frozen bananas"],
            ]),
        ]),
    },
    {
        "id": "water-rich",
        "title": "Principle 4 &mdash; Water-Rich Food",
        "body": "\n".join([
            P("Food can be classified as water-rich or water-poor."),
            dl([
                ("Water-rich",
                 "High water content &mdash; melons, berries, apples, grapes, oranges, "
                 "tomatoes, cucumbers; bottle gourd, ash gourd, celery, all leafy greens. "
                 "Light, easy to digest, and act like laxatives."),
                ("Water-poor",
                 "Low water content &mdash; all grains (rice, wheat), millets, lentils, "
                 "beans; starchy vegetables such as potato and yam; all nuts and seeds. "
                 "Harder to digest and can be constipating unless taken in limited amounts."),
            ]),
            P("To identify which a food is, put it in the juicer. If a lot of juice comes "
              "out, it&rsquo;s water-rich. You can&rsquo;t juice a chapati."),
            P("The more water a food contains, the quicker it passes through the digestive "
              "system, freeing the healing power (<em>praanshakti</em>) to cure disease. "
              "Water-poor foods are dense; the time that could have been used for healing "
              "is diverted to digesting them."),
            H2("How much of my diet should be water-rich?"),
            P("About 70% of our body is water, so about 70% of the diet should be "
              "water-rich and the remaining 30% water-poor. Most people eat the exact "
              "opposite ratio &mdash; a heavy grain-rich meal 3&ndash;4 times a day &mdash; "
              "and as a result they&rsquo;re drying up. Without enough water a plant&rsquo;s "
              "branches harden and break; likewise our bones degenerate, giving arthritis, "
              "rheumatism, cervical and back pain."),
            NOTE("The meal plans in this book are designed so that about 70% of your diet "
                 "is automatically water-rich &mdash; juice in the morning, juicy fruits "
                 "for breakfast, composite chapati (50% vegetable) with sabzi for lunch, "
                 "and a soup or salad for dinner."),
            H2("Frequently asked questions"),
            P("<strong>How much water should I drink in a day?</strong> Drink only when "
              "thirsty. Excessive water puts undue pressure on the kidneys; instead of "
              "digesting the last meal, the body redirects energy to process the water. On "
              "a Satvic diet, with lots of fruit and salad, your need for plain water "
              "reduces substantially."),
            P("<strong>Coffee, soda and beer contain water, don&rsquo;t they?</strong> No "
              "&mdash; these act as diuretics: they increase urination and actually cause "
              "us to lose water and become dehydrated."),
        ]),
    },
    {
        "id": "21-laws",
        "title": "The 21 Satvic Food Laws",
        "body": "\n".join([
            P("All recipes in this book are created to adhere to these laws. Follow every "
              "one to receive the true benefit of the Satvic lifestyle."),
            OL([
                "<strong>No animal-based foods</strong> (meat, fish, eggs, animal milk*, "
                "cheese, butter, ghee, paneer). Eat plant-based foods such as fresh "
                "homemade coconut milk and almond milk.",
                "<strong>No dead foods</strong> &mdash; nothing packaged, bottled, tinned "
                "or canned from a factory (chips, namkeens, snacks, vinegar, soya sauce, "
                "readymade sauces or dressings). Eat fresh foods straight from the farm.",
                "<strong>No sugar</strong> (white, brown, sugar-syrups, khaand, maple "
                "syrup, agave). Use natural sweeteners &mdash; fresh fruits, dates, "
                "jaggery, figs, raisins.",
                "<strong>No white rice.</strong> Eat brown rice.",
                "<strong>No oils</strong> (olive, mustard, coconut, palm, refined, "
                "flaxseed). Use whole fats &mdash; grated fresh coconut, soaked nuts and seeds.",
                "<strong>No refined flours</strong> (white flour, maida, sooji). Use whole "
                "wheat flour with chokar.",
                "<strong>No red chili</strong> or red chili powder. Use fresh green chili "
                "or black pepper in limited amounts.",
                "<strong>No strong spices</strong> (garam masala, heeng, turmeric, kala "
                "namak, too much ginger, too much salt). Use fresh herbs &mdash; tulsi, "
                "curry leaves, coriander, basil, lemongrass, oregano, rosemary, thyme, bay "
                "leaf. Mild spices (cardamom, cinnamon, cumin) in moderation.",
                "<strong>No iodised salt.</strong> Use rock salt (sendha namak) in limited amounts.",
                "<strong>No excessive cooking.</strong> Eat most food raw; if needed, cook "
                "minimally for the shortest time. Frying and over-cooking are prohibited. "
                "Fruits, tomato, coconut and coconut milk should not be cooked; sprouts "
                "should not be cooked; steaming beats boiling.",
                "<strong>No metal pots and pans</strong> for cooking. Use clay pots and pans.",
                "<strong>Don&rsquo;t eat much grain.</strong> Maintain a 70&ndash;30 ratio "
                "between vegetables and grains. One composite chapati &rarr; 2 bowls of "
                "sabzi; 1 bowl brown rice &rarr; 3 bowls of vegetables.",
                "<strong>Do not mix multiple grains in the same dish</strong> &mdash; no "
                "rice with chapati, no daal with rice, no multi-grain flour. Eat only one "
                "type of grain at a time, with a sufficiency of vegetables.",
                "<strong>No unseasonal or exotic foods.</strong> Eat foods that are "
                "seasonal and local to your country (skip blueberries, kale, swiss chard, "
                "hazelnuts, macadamia nuts in India).",
                "<strong>Do not use unsoaked nuts.</strong> Always soak nuts 6&ndash;8 "
                "hours before using &mdash; water brings them to life and makes them digestible.",
                "<strong>Do not eat too many nuts and seeds.</strong> Consume sparingly "
                "(~5&ndash;7 a day once cured); best avoided altogether while healing. They "
                "are already added to the salad and dressing recipes.",
                "<strong>Coconut milk is superior</strong> to almond, cashew and other nut "
                "milks &mdash; always prefer fresh homemade coconut milk.",
                "<strong>No soy milk, no tofu.</strong> Soya is very difficult to digest.",
                "<strong>Coconut and tomato should not be cooked directly on flame.</strong> "
                "Add them towards the end, after switching off the stove; let them warm from "
                "the steam. Do not re-heat a dish after adding them.",
                "<strong>In cooked recipes, add salt and lemon towards the end</strong>, "
                "not the beginning &mdash; they should not be cooked on flame.",
                "<strong>Do not add grains to a salad or soup.</strong> Salads and soups "
                "should be grain-free, unless eaten as a grain meal.",
            ]),
            NOTE("*Animal milk is allowed only in a few exceptional cases &mdash; see "
                 "the milk section under Principle 3."),
        ]),
    },
    {
        "id": "digestion",
        "title": "Understanding Digestion",
        "body": "\n".join([
            P("Essential to physical, mental and emotional health is the timely elimination "
              "of toxins. Everything in nature follows a specific order and timing &mdash; "
              "and so does our body."),
            H2("You, your washing machine &amp; cycles"),
            P("A washing machine has three mini-cycles within each complete cycle: fill and "
              "wash, rinse, spin. Your body has: <strong>digestion, assimilation, "
              "elimination</strong>. Stop the machine before the spin and the clothes stay "
              "wet and dirty; skip a mini-cycle and the clothes come out less clean than "
              "you expect."),
            P("Every time you eat, a large portion of your body&rsquo;s energy shifts to "
              "digestion, then to assimilation, then to elimination. If you eat again "
              "before the previous meal is processed, the body shifts energy to the new "
              "food and the residue of the old meal is left to bacteria, yeast and mold "
              "&mdash; producing toxins. Most of us eat by the clock, from boredom, or "
              "whenever we see or smell food. One should eat only when true hunger returns, "
              "after the last meal has been digested, absorbed and eliminated."),
            H2("Intermittent (16-hour) fasting"),
            P("Eat within a span of 8 hours and fast for 16 hours every night. If you eat "
              "dinner at 8 pm, eat no solid food till 12 noon the next day; if dinner is at "
              "6 pm, eat nothing till 10 am. Water and juices (coconut water, ash gourd "
              "juice) are allowed in the fasting window. The body digests and absorbs food "
              "within 5&ndash;6 hours; once digestion is complete it starts healing &mdash; "
              "rebuilding tissue, burning fat cells, fading old scars and curing disease."),
            QUOTE("Work and digestion must be kept apart, so there may be no competition "
                  "between them.", "Acharya K. Lakshmana Sarma, Father of Nature Cure in India"),
        ]),
    },
    {
        "id": "food-combining",
        "title": "Food Combining",
        "body": "\n".join([
            P("Foods are natural chemicals. The more ingredients in a meal, the greater the "
              "chance of a digestive explosion. Even fresh, wholesome food, if paired "
              "incorrectly, can cause indigestion, fermentation, gas, bloating and toxins."),
            H2("The highway analogy"),
            P("Three categories of vehicles enter the highway of our digestive tract: "
              "<strong>scooters</strong> (fruits &mdash; light and quick, ~3 hours), "
              "<strong>cars</strong> (vegetables &mdash; ~6 hours), and "
              "<strong>trucks</strong> (grains, lentils, nuts, seeds &mdash; heavy and "
              "slow, ~18 hours). This is why we feel lazy and sleepy after too many grains."),
            NOTE("Neutral vegetables (lettuce, celery, spinach, coriander, cucumber) digest "
                 "quicker than starchy vegetables (potato, peas, pumpkin, cauliflower)."),
            H2("Six laws of food combining"),
            OL([
                "<strong>Restrict grain to once a day.</strong> Grains take ~18 hours to "
                "digest. Eating them twice or thrice a day accumulates undigested waste. "
                "Easy combination: fruits for breakfast, Satvic sabzi-roti for lunch, salad "
                "for dinner. (Children, athletes and manual labourers can afford grains "
                "more than once a day.)",
                "<strong>Eat only one grain at a time</strong>, with a sufficiency of "
                "vegetables. No rice with chapati; no rajma, daal or chana with rice.",
                "<strong>When eating grains, mix them with 3&times; the vegetables.</strong> "
                "For chapati, use 50% wheat flour and 50% vegetable. One chapati &rarr; 2 "
                "bowls of sabzi; 1 bowl brown rice &rarr; 3 bowls of vegetables.",
                "<strong>Do not eat fruits and cooked food in the same meal.</strong> "
                "Fruits digest best alone or with neutral green vegetables (lettuce, "
                "cucumber, coriander, celery, kale).",
                "<strong>Don&rsquo;t mix sweet fruits with citric fruits.</strong> Sweet "
                "(mango, banana, chikoo, persimmon) and citric (orange, mandarin, "
                "pineapple, lemon) need different digestive juices. Eat similar kinds "
                "together. Bulkier fruits (banana, coconut, avocado) need more digestion time.",
                "<strong>Don&rsquo;t drink while you eat.</strong> Drinking dilutes the "
                "digestive juices. Drink water at least 1 hour before or 2 hours after a "
                "solid meal. If necessary, take 2 sips and hold them in the mouth a while "
                "before swallowing.",
            ]),
        ]),
    },
    {
        "id": "how-you-eat",
        "title": "How You Eat Is More Important Than What You Eat",
        "body": "\n".join([
            OL([
                "<strong>Eat 70% raw, 30% cooked.</strong> Once you cook food, it&rsquo;s "
                "dead. Eat no more than one cooked meal a day; cook on a low flame for as "
                "little time as possible; eat within 3 hours; never refrigerate cooked food "
                "for the next day.",
                "<strong>Always rest after a grain meal.</strong> Digestion takes up to "
                "70% of the body&rsquo;s energy. Take a 30-minute nap or rest after a grain "
                "meal. No rest is needed after a light meal such as fruit or a smoothie. If "
                "work doesn&rsquo;t allow rest after lunch, eat a lighter lunch and your "
                "grain meal at dinner.",
                "<strong>Never overeat.</strong> Always leave the table a little hungry. If "
                "you fill a blender to the top it can&rsquo;t blend; the stomach needs "
                "empty space to mix digestive juices. Even wholesome food, eaten in excess, "
                "becomes toxic filth.",
                "<strong>Eat only when you&rsquo;re hungry.</strong> Before a meal, three "
                "things should have happened: elimination of wastes, adequate rest for the "
                "organs, and a feeling of bodily lightness with sufficient digestive power. "
                "Eat for the third &lsquo;t&rsquo; &mdash; the tummy &mdash; not the tongue "
                "or the time.",
                "<strong>Eat a light breakfast.</strong> On waking, the digestive fire is "
                "still partly asleep. Breakfast, if not renounced, should be light &mdash; "
                "fruit or salad. Lunch can be heavier; supper should be light and finished "
                "at least two hours before sleep.",
                "<strong>Eat neither too cold nor too hot.</strong> Match the food&rsquo;s "
                "temperature to the body. If too hot or cold, hold it on your tongue for "
                "10&ndash;12 seconds first. All recipes in this book are served at room "
                "temperature.",
                "<strong>Always eat in a relaxed state.</strong> Don&rsquo;t eat when "
                "upset, angry, agitated or in a hurry &mdash; vital energy goes to the "
                "mental stress and little remains for digestion.",
                "<strong>Don&rsquo;t mix too much together.</strong> Eat one type of fruit, "
                "vegetable or grain at a time; if drinking liquids, have only liquids. Your "
                "stomach will have just one thing to do.",
                "<strong>Eat seasonal, regional and reasonable.</strong> Unseasonal produce "
                "needs enormous chemicals and pesticides; imported produce carries more "
                "preservatives. Seasonal, local food is also cheaper.",
                "<strong>Chew, chew and chew.</strong> The more you chew, the more saliva "
                "is produced and the easier food is to digest. Eating by this rule, less is "
                "eaten in more time &mdash; so you cannot overeat.",
            ]),
            QUOTE("Therefore, eat not anything which fire, or frost, or water has "
                  "destroyed. For burned, frozen and rotted foods will burn, freeze and rot "
                  "your body also.", "Jesus, Essene Gospel of Peace"),
        ]),
    },
]

# ------------------------------------------------------------------- KITCHEN ----
KITCHEN = [
    {
        "id": "shopping-list",
        "title": "Shopping List for a Satvic Kitchen",
        "body": "\n".join([
            P("Buy fruits, vegetables and fresh herbs as and when you make the recipes; "
              "buy all the dry ingredients (dry herbs, nuts, seeds, sprouting seeds, "
              "grains, spices, condiments, sweeteners) in advance in one grocery trip."),
            H2("Fresh &mdash; buy as needed"),
            H3("Fruits"),
            P("Lemon, melons, papaya, coconut, apple, pear, orange, mango, banana, "
              "pomegranate, peach, plum, berries, grapes, sapota (chikoo), kiwi, pineapple. "
              "Seasonal and regional; not frozen."),
            H3("Vegetables"),
            P("Ash gourd, bottle gourd, ridge gourd, spinach, lettuce, rocket leaves, "
              "cucumbers, celery, parsley, zucchini, tomatoes, bell peppers, beetroot, "
              "carrots, pumpkin, cabbage, peas, broccoli, green beans, cauliflower, "
              "potatoes. Avoid precut, prepackaged vegetables."),
            H3("Herbs"),
            P("Coriander, mint, bay leaf, curry leaves, thyme, oregano, rosemary, "
              "lemongrass, basil."),
            H2("Dry &mdash; buy in advance"),
            H3("Nuts and seeds"),
            P("Almonds, walnuts, cashews, pistachios, peanuts, pumpkin seeds, sunflower "
              "seeds, poppy seeds, chia seeds, flax seeds, sesame seeds. Always soak before "
              "using."),
            H3("Seeds for sprouting"),
            P("Alfalfa, clover, fenugreek, radish. (Vegetable-seed sprouts are easier to "
              "digest than lentil sprouts.)"),
            H3("Grains and legumes"),
            P("Whole wheat flour, brown rice, quinoa, moong daal."),
            H3("Spices and condiments"),
            P("Rock salt (sendha namak), green chillies, fresh ginger, cinnamon, green "
              "cardamom buds, fennel seeds, cumin, black pepper, black salt, saffron "
              "strands, cacao powder, cacao nibs, carob powder, galangal, vanilla powder."),
            H3("Dry herbs"),
            P("Dried basil, oregano, rosemary, thyme. (Use a 1:3 ratio &mdash; dry herbs "
              "are more concentrated.)"),
            H3("Sweeteners"),
            P("Dates, raisins, chemical-free jaggery."),
        ]),
    },
    {
        "id": "eight-tools",
        "title": "Eight Essential Tools",
        "body": "\n".join([
            dl([
                ("1 &mdash; Blender",
                 "Needed for everything &mdash; soups, dressings, nut milks. An average "
                 "household blender works; a high-speed blender (Vitamix, Blendtec) makes "
                 "the silkiest results."),
                ("2 &mdash; Juicer",
                 "Two types: centrifugal (a fast metal blade generates heat that destroys "
                 "enzymes) and slow / cold-press (crushes then presses, keeping more "
                 "nutrients). Prefer a slow press juicer."),
                ("3 &mdash; Clay pot",
                 "Clay is porous, letting moisture and heat circulate through the food and "
                 "retaining nutrition. If unavailable, use stainless steel (without nickel "
                 "plating). No aluminium or non-stick."),
                ("4 &mdash; Clay tawa",
                 "A chapati cooked on a clay tawa is far more digestible than one cooked on "
                 "metal; an aluminium tawa leaches metal particles into the body."),
                ("5 &mdash; Measuring cups and spoons",
                 "Use the exact amounts in the recipes to get the right taste, consistency "
                 "and texture."),
                ("6 &mdash; Nut milk bag or muslin cloth",
                 "A specially shaped fabric bag to strain blended almond or coconut milk "
                 "and remove pulp, for a smoother consistency."),
                ("7 &mdash; Julienne vegetable peeler",
                 "A peeler with a jagged edge that creates thin strips of vegetables for "
                 "salads &mdash; zucchini, carrots, radish, cucumber, beets, apples. Saves "
                 "time and prevents fatigue."),
                ("8 &mdash; Spiraliser",
                 "Turns fresh hard vegetables (ridge gourd, bottle gourd, zucchini, "
                 "beetroot, cucumber) into noodles &mdash; a sneaky way to eat more vegetables."),
            ]),
        ]),
    },
    {
        "id": "using-tools",
        "title": "How to Use the Tools",
        "body": "\n".join([
            H2("Julienne vegetable peeler"),
            OL([
                "Peel the vegetable with a standard peeler first. Hold it firmly at an "
                "angle and press the julienne peeler against it.",
                "Peel the flesh, sliding the peeler away from you. Turn and repeat until "
                "you can no longer peel comfortably.",
                "Use the resulting vegetable ribbons in salads or wraps.",
            ]),
            H2("Spiraliser"),
            OL([
                "Top and tail the vegetable and insert it into the spiraliser. For most "
                "vegetables you do not need the cap at this stage.",
                "Twist the vegetable into the spiraliser like a pencil sharpener. Near the "
                "bottom, use the cap so you don&rsquo;t injure yourself.",
                "A great dish to make with the resulting noodles is zucchini spaghetti.",
            ]),
        ]),
    },
    {
        "id": "sprouts",
        "title": "How to Grow Sprouts",
        "body": "\n".join([
            P("Sprouts are the very first shoots of germinating seeds, legumes and grains. "
              "Nutritionally they have a long history as a health food &mdash; 10 to 30 "
              "times more nutritious than the best vegetables, because they are baby plants "
              "in their prime. Applying water to a seed releases dormant vitamins, minerals "
              "and enzymes &mdash; most pronounced in the first 12 days of growth. Sprouts "
              "are also biogenic (they create new life when planted) and alive."),
            H2("Leafy sprouts vs lentil / bean sprouts"),
            dl([
                ("Leafy sprouts &mdash; easy to digest, suitable for everyone",
                 "Alfalfa, clover, fenugreek, radish."),
                ("Lentil &amp; bean sprouts &mdash; difficult to digest",
                 "Moong, red lentils, green lentils, chickpea. Suitable only for athletes, "
                 "children and manual labourers; avoid while curing a disease, losing "
                 "weight or maintaining health."),
            ]),
            H2("Six simple steps"),
            OL([
                "Rinse the seeds and place in a glass container. Cover with filtered water "
                "plus an inch. Soak overnight.",
                "Next morning, drain the water. Rinse once and drain again. Put the seeds "
                "in the centre of a cotton cloth.",
                "Tie the cloth tightly so the seeds are contained in a bundle.",
                "Place the bundle in a bowl and cover with a plate. Keep out of direct sunlight.",
                "Rinse the seeds with fresh filtered water twice a day &mdash; morning and "
                "evening &mdash; for 4&ndash;5 days.",
                "When the sprouts are long enough to eat, let them dry completely before "
                "storing. They keep in a covered container in the refrigerator for 5&ndash;7 days.",
            ]),
            H2("Quantity chart"),
            TABLE(["Seed", "Yield", "Rinsing time"], [
                ["Alfalfa", "1 tbsp seeds = 1 cup sprouts", "5 days"],
                ["Clover", "1 tbsp seeds = 1 cup sprouts", "5 days"],
                ["Radish", "2 tbsp seeds = 1 cup sprouts", "5 days"],
                ["Fenugreek", "1 tbsp seeds = 1&frac12; cups sprouts", "3 days"],
                ["Moong", "&frac12; cup seeds = 2 cups sprouts", "3 days"],
                ["Green lentils", "&frac12; cup seeds = 2 cups sprouts", "3 days"],
            ]),
            H2("Sprouting FAQs"),
            P("<strong>Best place to grow:</strong> your kitchen counter. "
              "<strong>Best temperature:</strong> 17&ndash;22&deg;C (65&ndash;75&deg;F). "
              "<strong>Light:</strong> not much &mdash; never direct sunlight, or they cook "
              "and die. <strong>Water:</strong> filtered, room temperature. "
              "<strong>Storage:</strong> refrigerator, covered, completely dry; 5&ndash;7 "
              "days. <strong>Mold:</strong> increase ventilation &mdash; a fan on low in "
              "the room."),
            H2("How to use sprouts in a salad"),
            P("For a fulfilling salad: 30% sprouts, 30% leafy greens, 30% vegetables, 10% "
              "toppings (grated coconut, soaked nuts &amp; seeds, homemade dressings, "
              "dried fruits)."),
        ]),
    },
    {
        "id": "nut-milk",
        "title": "How to Make Nut Milk",
        "body": "\n".join([
            P("Nut milks are made by soaking nuts in water for 6&ndash;8 hours, then "
              "blending with fresh water and straining. Coconut milk is the healthiest "
              "&mdash; easier to digest than any other. Most recipes in this book already "
              "include coconut milk, so there is no need to drink nut milk separately. "
              "Never buy pre-packaged nut milks &mdash; they are full of preservatives, "
              "thickeners and artificial ingredients."),
            H2("Method &mdash; coconut milk (makes 2 cups)"),
            OL([
                "Take 1 cup of fresh dessicated coconut.",
                "Combine with 2 cups of water in a blender.",
                "Blend until smooth.",
                "Pour the mixture over a bowl covered with a nut milk bag or muslin cloth.",
                "Squeeze out the milk with your hand. Use the leftover pulp as a face scrub.",
                "Use immediately or store in the refrigerator for up to 1&ndash;2 days.",
            ]),
            P("For <strong>almond milk</strong>, replace the 1 cup dessicated coconut with "
              "1 cup almonds soaked in water for 5&ndash;6 hours."),
            NOTE("Use only raw, un-fried nuts &mdash; strictly no roasted nuts. Always "
                 "discard the soaking water. Do not make soy milk. Never cook coconut milk "
                 "directly on flame &mdash; when cooked it converts into cholesterol; add "
                 "it towards the end after switching off the stove."),
        ]),
    },
    {
        "id": "perfect-recipes",
        "title": "How to Make Perfect Recipes",
        "body": "\n".join([
            OL([
                "<strong>Use exact measurements.</strong> Measure with proper measuring "
                "cups and spoons &mdash; casual additions give the wrong taste, consistency "
                "or texture.",
                "<strong>Conversion chart:</strong> &frac14; cup = 4 tablespoons; &frac12; "
                "cup = 8 tablespoons; 1 tablespoon = 3 teaspoons; 1 pinch = 1/16 teaspoon.",
                "<strong>When using dry herbs, use less</strong> &mdash; a 1:3 ratio. 1 "
                "tablespoon fresh = 1 teaspoon dry.",
                "<strong>Always soak seeds and nuts</strong> before using &mdash; soaking "
                "removes the enzyme inhibitors that make them hard to digest. Average soak "
                "time is 6 hours; overnight is fine.",
                "<strong>Stick to the recipes exactly.</strong> Do not increase the amount "
                "of grains, nuts or spices &mdash; the recipes are built on strict Satvic "
                "principles.",
            ]),
        ]),
    },
]

# ----------------------------------------------------------------- MEAL PLAN ----
MEAL_PLAN = [
    {
        "id": "meal-plans",
        "title": "Choose Your Meal Plan",
        "body": "\n".join([
            P("It is not enough to eat some Satvic food now and then &mdash; all our meals "
              "must be Satvic. Each meal plan consists of 5 meals: "
              "<strong>Pre-breakfast, Breakfast, Lunch, Mid-Meal, Dinner</strong>."),
            dl([
                ("Blue plan &mdash; children &amp; heavy physical work",
                 "For children below age 16, or people engaged in heavy physical work. "
                 "Grains can be eaten twice a day. No 16-hour fasting needed if healthy."),
                ("Yellow plan &mdash; healing &amp; maintenance",
                 "For those healing a health problem, losing weight, or simply maintaining "
                 "health. Grains not more than once a day. Follow 16-hour fasting &mdash; a "
                 "16-hour gap between the last meal and the first meal. The recipes in this "
                 "book are structured for the yellow plan."),
                ("White plan &mdash; fasting",
                 "No solid food. Follow during an acute disease (cold, cough, fever, sore "
                 "throat, diarrhea), or for 2&ndash;3 days a month as a juice fast to detoxify."),
            ]),
            NOTE("You can adjust timings to your schedule, and swap lunch and dinner in any "
                 "plan. If hungry during the 16-hour fast, drink water or juices &mdash; no "
                 "solid food."),
        ]),
    },
]

# ------------------------------------------------------------------- RECIPES ----
PRE_BREAKFAST = [
    {
        "id": "ash-gourd-juice",
        "title": "Ash Gourd Juice",
        "body": recipe(
            sub="Pre-breakfast &mdash; 1st option (best)",
            intro=["Ash gourd (safed petha) is one of the most detoxifying vegetables in "
                   "Nature &mdash; like a sponge in the digestive system, it draws in "
                   "toxins and carries them out. It belongs to the gourd family and is also "
                   "called &lsquo;winter melon&rsquo;. The taste is not bitter at all "
                   "&mdash; quite bland, like water.",
                   "Have this 1&ndash;2 hours after waking, with a 2-hour gap before breakfast."],
            groups=[(None, ["Ash gourd (safed petha)"])],
            method=["Remove the peel of the ash gourd and take out all the seeds from inside.",
                    "Cut into pieces and juice it. Drink about 400 ml (1 glass) every morning."],
        ),
    },
    {
        "id": "ash-coco-juice",
        "title": "Ash Coco Juice",
        "body": recipe(
            sub="Pre-breakfast &mdash; 2nd option",
            intro=["If you do not like the taste of ash gourd, or want to give it to "
                   "children, mix the ash gourd juice with 50% coconut water."],
            groups=[(None, ["50% ash gourd juice", "50% coconut water"])],
            method=["Mix the ash gourd juice with 50% coconut water.",
                    "Drink about 400 ml (1 glass) every morning."],
        ),
    },
    {
        "id": "coconut-water",
        "title": "Coconut Water",
        "body": recipe(
            sub="Pre-breakfast &mdash; 3rd option",
            intro=["Coconut is called &lsquo;Shree Phal&rsquo; in Sanskrit for its healing "
                   "properties. Coconut water is a natural laxative. Use only fresh coconut "
                   "water, not the pre-packaged or bottled version. If unavailable, drink "
                   "the juice of any other fresh green vegetable &mdash; celery, cucumber, "
                   "bottle gourd, spinach."],
            groups=[(None, ["400 ml (about 1 glass) of coconut water"])],
            method=["Open a fresh drinking coconut and drink the water."],
        ),
    },
]

BREAKFAST = [
    {
        "id": "smoothie-basics",
        "title": "Breakfast &amp; Smoothie Basics",
        "body": "\n".join([
            P("For breakfast, have fresh fruits, a smoothie or the pure Satvic salad, "
              "2 hours after your morning detox juice. If you have fruits for breakfast, "
              "have salad for dinner, and vice versa. If diabetic, avoid sweet fruits "
              "(mango, pineapple, chikoo, banana) and stick to neutral fruits (melon, papaya)."),
            H2("Eating fruit"),
            UL(["<strong>1 fruit at a time (best)</strong> &mdash; &lsquo;mono-eating&rsquo;; "
                "a plate of any one seasonal fruit (melon, apple, pear, pineapple, orange, "
                "papaya, peach, pomegranate, berries, guava).",
                "<strong>2 fruits</strong> &mdash; mix same categories; melons only with "
                "melons; don&rsquo;t mix sweet (mango, chikoo) with citric (orange, "
                "pineapple, kiwi).",
                "<strong>2 or more fruits</strong> &mdash; not bad, but slower to digest; "
                "still mix only same categories, never citrus with sweet."]),
            H2("The 4 components of a smoothie"),
            OL([
                "<strong>Liquid</strong> &mdash; coconut milk, coconut water, watery "
                "fruits or drinking water.",
                "<strong>Base</strong> &mdash; any fruit or vegetable: banana, pear, "
                "melon, papaya, beetroot, carrot, spinach, lettuce.",
                "<strong>Sweetener</strong> &mdash; sweet fruits such as mango, banana or dates.",
                "<strong>Flavor</strong> &mdash; herbs such as mint or basil, carob "
                "powder, cacao powder, vanilla powder, ginger.",
            ]),
        ]),
    },
    {
        "id": "pina-colada",
        "title": "Pi&ntilde;a Colada",
        "body": recipe(
            meta="Serves 1, makes 500 ml",
            groups=[(None, ["1 cup pineapple chunks", "1 cup coconut milk",
                            "&frac12; medium banana", "&frac14; cup ice cubes",
                            "2 dates, seedless",
                            "&frac18; teaspoon vanilla bean powder (optional)"])],
            method=["Place everything into a blender and blend until smooth. Serve."],
            notes=["Note: Drink as an occasional treat."],
        ),
    },
    {
        "id": "banana-date-shake",
        "title": "Banana Date Shake",
        "body": recipe(
            meta="Serves 2, makes 700 ml",
            groups=[(None, ["1&frac12; cups coconut milk", "3 bananas", "6 dates, seedless",
                            "4 ice cubes", "&frac12; teaspoon cinnamon powder"])],
            method=["Place coconut milk, bananas, dates, ice and cinnamon into a blender "
                    "and blend until smooth. Serve."],
        ),
    },
    {
        "id": "tropical-smoothie",
        "title": "Tropical Smoothie",
        "body": recipe(
            meta="Serves 1, makes 500 ml",
            groups=[(None, ["1 cup coconut water", "1 cup chopped spinach",
                            "1 cup chopped apple", "1 cup mango chunks",
                            "&frac12; teaspoon lemon juice"])],
            method=["Place all the ingredients into a blender and blend until smooth.",
                    "Let the smoothie cool in the refrigerator for about 20 minutes "
                    "before serving."],
            notes=["Note: If mango is out of season, replace it with 1 cup chopped guava "
                   "and 2 seedless dates."],
        ),
    },
    {
        "id": "pure-satvic-salad",
        "title": "Pure Satvic Salad",
        "body": recipe(
            meta="Serves 2, makes 7 cups",
            intro=["The purest and cleanest salad in this book &mdash; no nuts, seeds, "
                   "dressings, salt or lemon. Yet it&rsquo;s flavourful (coriander and "
                   "coconut) and crunchy (sprouts)."],
            groups=[(None, ["2 cucumbers, chopped", "2 carrots, grated", "2 tomatoes, chopped",
                            "1 small green capsicum, chopped", "1 cup coriander, chopped",
                            "2 big slices of coconut, grated"]),
                    ("For a boost", ["&frac12; cup vegetable sprouts"])],
            method=["Place all the ingredients into a large mixing bowl. Toss together and serve."],
            prep=["(Optional) Prepare vegetable sprouts."],
            notes=["Note: Use vegetable sprouts, not lentil sprouts, unless you are an "
                   "athlete or a child below age 16."],
            bestfor=bf("Breakfast", "Dinner"),
        ),
    },
]

LUNCH = [
    {
        "id": "lunch-guidelines",
        "title": "Lunch Guidelines",
        "body": OL([
            "Eat only one type of grain at a time &mdash; no chapati with rice, no rice "
            "with cheelas, no daliya with quinoa.",
            "Eat less grain and more vegetable &mdash; 1 bowl grain to 3 bowls vegetable.",
            "Satvic chapati with Satvic sabzi on most days; khichadi, daliya, cheelas or "
            "quinoa on the remaining days.",
            "Do not eat rice (even brown rice) more than twice a week.",
            "After lunch, rest for 20 minutes so energy is diverted to digestion.",
            "You may have your grain meal for dinner and the soup / salad meal for lunch instead.",
        ]),
    },
    {
        "id": "composite-chapati",
        "title": "Composite Chapati",
        "body": recipe(
            groups=[(None, ["50% wheat flour", "50% any seasonal vegetable (grated)"])],
            method=["Take 1 cup of any seasonal grated vegetable and 1 cup of wheat flour.",
                    "Combine, using water if required. Make a dough and divide into balls. "
                    "Dip the balls in flour and flatten them.",
                    "Roll the balls with a rolling pin.",
                    "Heat a clay tawa on low heat and cook the chapati on it. Do not use "
                    "oil or ghee."],
        ),
    },
    {
        "id": "satvic-sabzi",
        "title": "Satvic Sabzi",
        "body": recipe(
            meta="Serves 2",
            groups=[(None, ["Any 1 or 2 seasonal vegetables"]),
                    ("Gravy", ["4 tomatoes", "100 g grated coconut", "&frac12; teaspoon rock salt",
                               "1 small green chili", "cumin powder, to taste", "2 coins ginger",
                               "curry leaves"])],
            method=["Soak the seasonal vegetables in water for about 2 hours to reduce the "
                    "impact of chemicals.",
                    "Peel and chop the vegetables. Add to a clay pot with some water. Close "
                    "the lid and cook in water until soft.",
                    "Meanwhile, blend the tomatoes, coconut, salt, chili, cumin and curry "
                    "leaves until smooth.",
                    "Combine the gravy with the boiled vegetables. Close the lid, switch "
                    "off the stove and let the gravy cook through the steam for 10 minutes. "
                    "Top with coriander and serve."],
            notes=["Note: Do not re-heat sabzi after adding the gravy &mdash; coconut and "
                   "tomatoes should never be cooked."],
        ),
    },
    {
        "id": "satvic-khichadi",
        "title": "Satvic Khichadi",
        "body": recipe(
            meta="Serves 3",
            intro=["Brown rice is wholesome but still a grain, so this is a comfort food "
                   "rather than a healing recipe &mdash; still far healthier than "
                   "traditional khichadi made with ghee, lentils, white rice and spices."],
            groups=[(None, ["&frac34; cup soaked brown rice", "6 cups water",
                            "1 cup finely chopped green beans", "1 cup grated carrot",
                            "1 cup grated bottle gourd", "1 teaspoon turmeric powder",
                            "1 cup finely chopped spinach",
                            "2 small green chillies, finely crushed", "1 cup chopped tomato",
                            "&frac12; cup coconut kernel, sliced then blended",
                            "2 teaspoons rock salt", "&frac12; cup chopped coriander",
                            "Green Chutney, to serve"])],
            method=["Place the brown rice with 6 cups water. Cook on a low flame till soft "
                    "(about 45 minutes), stirring in between.",
                    "Add the beans, carrot, bottle gourd and turmeric; cook another 15 "
                    "minutes, adding water if required.",
                    "Add the spinach and green chillies. Stir and cook 5 minutes.",
                    "Turn off the stove. Add the tomatoes, coconut and salt. Keep covered 5 minutes.",
                    "Top with coriander and serve with green chutney."],
            prep=["Soak brown rice in water for about 3 hours."],
        ),
    },
    {
        "id": "satvic-daliya",
        "title": "Satvic Daliya",
        "body": recipe(
            meta="Serves 2&ndash;3",
            intro=["Less grain, more vegetables &mdash; a 1:3 ratio, so the body spends "
                   "less time digesting and more time healing."],
            groups=[(None, ["1 cup broken wheat porridge (daliya)",
                            "1&frac12; teaspoons cumin seeds",
                            "1 cup green beans, finely chopped",
                            "1 cup carrots, finely chopped", "1 cup green peas",
                            "2 small green chilies, very finely crushed", "4 cups water",
                            "2 teaspoons rock salt", "handful fresh coriander",
                            "Green Chutney, to serve"])],
            method=["Roast the broken wheat porridge lightly in a pan till light brown. Set aside.",
                    "In another pan on medium flame, roast the cumin seeds till dark brown. "
                    "Add the beans, carrots and peas and stir well. Add the crushed chilies "
                    "and stir again.",
                    "Add 4 cups water and bring to a boil. Add the roasted porridge. Cover "
                    "and cook on medium flame till the porridge absorbs all the water.",
                    "Turn off the stove. Add rock salt and keep covered 5 minutes.",
                    "Garnish generously with coriander and enjoy with green chutney. Eat "
                    "within 3&ndash;4 hours."],
        ),
    },
    {
        "id": "spinach-cheelas",
        "title": "Spinach Cheelas",
        "body": recipe(
            meta="Makes 8&ndash;10 cheelas",
            intro=["Instead of only lentils, we use 1 cup lentils to 2 cups spinach "
                   "&mdash; unless you&rsquo;re an athlete or a growing child, eat lentils "
                   "sparingly."],
            groups=[("For the cheelas",
                     ["1 cup green split moong dal", "1 teaspoon rock salt",
                      "1 small green chili, chopped", "2 cups spinach pur&eacute;e*"]),
                    ("For the filling",
                     ["4 carrots, thickly grated", "4 tomatoes, chopped finely",
                      "&frac12; cup grated coconut", "&frac12; cup coriander, chopped",
                      "1 teaspoon rock salt", "Green Chutney, to serve"])],
            method=["Blend the soaked moong dal, salt and chili until smooth. Transfer to a "
                    "bowl, add the spinach pur&eacute;e and stir well.",
                    "Heat a pan (tava), sprinkle a little water and wipe with a muslin "
                    "cloth. Pour a ladle of batter and spread in a circular motion into a "
                    "thin circle. Cook on medium flame till brownish-green.",
                    "For the filling, combine the carrots, tomatoes, coconut, coriander and "
                    "salt. Fill the cheelas and serve immediately with green chutney."],
            prep=["Soak moong dal in water for about 3 hours.",
                  "*2&frac12; cups chopped spinach, blended, gives 2 cups pur&eacute;e."],
        ),
    },
    {
        "id": "moong-bowl",
        "title": "Moong Bowl",
        "body": recipe(
            meta="Serves 3 as a main meal",
            intro=["A fully raw, refreshing bowl &mdash; easy to make and good for people "
                   "with little time to cook."],
            groups=[(None, ["&frac12; cup split moong dal with skin",
                            "1&frac12; cup finely chopped fresh methi leaves",
                            "1 cup finely chopped coriander", "1&frac12; cup diced apple",
                            "1&frac12; cup chopped grapes", "1&frac12; cup pomegranate",
                            "2 tablespoons chia seeds", "2 tablespoons pumpkin seeds",
                            "2 tablespoons white sesame seeds"]),
                    ("Flavoring",
                     ["1 teaspoon grated fresh ginger", "2 tablespoons lemon juice",
                      "1 teaspoon rock salt", "1 green chili, crushed",
                      "&frac18; teaspoon asafoetida (hing)"])],
            method=["Place the moong dal, methi, coriander, apple, grapes, pomegranate, "
                    "chia, pumpkin and sesame seeds into a large bowl. Mix well.",
                    "Mix all the flavoring ingredients together in a small bowl so they infuse.",
                    "Add the flavouring to the rest, mix well and serve."],
            prep=["Soak split moong dal in water for about 4 hours."],
        ),
    },
    {
        "id": "sprout-wraps",
        "title": "Sprout Wraps",
        "body": recipe(
            meta="Makes 3 rolls",
            intro=["Raw sprouts wrapped in nori sheets. Nori is a sea vegetable and, like "
                   "sprouts, a nutritional powerhouse &mdash; get untoasted nori if you can."],
            groups=[(None, ["4 nori sheets", "4 lettuce leaves",
                            "2 cups homegrown sprout mix (alfalfa, clover, radish)",
                            "1 small cucumber, cut lengthwise", "1 small carrot, cut lengthwise",
                            "1 red bell pepper, cut lengthwise",
                            "&frac14; red cabbage, cut lengthwise",
                            "1 avocado (optional), peeled and cut lengthwise"]),
                    ("Peanut Dressing",
                     ["2 tablespoons peanuts, soaked", "1 tablespoon lemon juice",
                      "&frac18; small green chili", "&frac12; teaspoon rock salt",
                      "1 tablespoon powdered jaggery", "2 tablespoons water"])],
            method=["Place a nori sheet shiny side down on a bamboo mat. At the bottom "
                    "half, place a lettuce leaf.",
                    "Add a handful of the sprout mix, cucumber, carrot, bell pepper, "
                    "cabbage and avocado.",
                    "Wrap the roll tightly, using a little water to seal the ends.",
                    "Cut each roll into 3 pieces with a sharp knife.",
                    "Blend all the dressing ingredients together. Add inside the roll or "
                    "serve alongside."],
            prep=["Prepare vegetable sprouts."],
        ),
    },
    {
        "id": "coco-quinoa-bowl",
        "title": "Coco Quinoa Bowl",
        "body": recipe(
            meta="Serves 2&ndash;3 as a main meal",
            intro=["Quinoa is technically a seed, but we classify it as a grain because it "
                   "has the same digestibility. The herbs come together to create an "
                   "exquisite flavour."],
            groups=[(None, ["1 cup quinoa", "3&frac12; cups water", "1 cup green peas",
                            "3 cups chopped cauliflower", "2 small potatoes, diced",
                            "1 teaspoon ginger, grated", "1 teaspoon green chili, crushed",
                            "1 tablespoon fresh thyme (or 1 teaspoon dried)",
                            "2 cups coconut milk", "2&frac12; teaspoons rock salt",
                            "1 tablespoon lemon juice", "&frac12; cup chopped coriander"])],
            method=["Wash the quinoa. Cook in a saucepan with 2&frac12; cups water on low "
                    "flame till the water is absorbed, adding more if necessary.",
                    "In another saucepan, cook the peas, cauliflower and potatoes in 1 cup "
                    "water till soft to bite. Remove the vegetables; keep the broth aside.",
                    "Add the vegetables to the quinoa and stir well.",
                    "Add ginger, chili and thyme and stir for &frac12; a minute.",
                    "Switch off the stove and immediately add coconut milk, salt and lemon. "
                    "Keep covered 5 minutes so the ingredients cook in the steam, not on flame.",
                    "Top with coriander, stir well and serve immediately."],
            prep=["Prepare coconut milk."],
        ),
    },
    {
        "id": "green-chutney",
        "title": "Green Chutney",
        "body": recipe(
            groups=[(None, ["1 cup coriander leaves", "&frac12; cup mint leaves",
                            "&frac12; cup unripe mango, roughly chopped",
                            "1 teaspoon cumin seeds", "1 teaspoon rock salt",
                            "1 small green chili"])],
            method=["Blend all ingredients together. Serve as a condiment with sabzi, "
                    "khichdi or cheela.",
                    "Store in the refrigerator for 2&ndash;3 days."],
        ),
    },
    {
        "id": "date-chutney",
        "title": "Date Chutney",
        "body": recipe(
            groups=[(None, ["&frac13; cup water", "10 dates, seedless",
                            "2 teaspoons lemon juice", "1 teaspoon cumin seeds",
                            "1 teaspoon rock salt", "1 small green chili"])],
            method=["Blend all the ingredients together until smooth. Serve as a condiment "
                    "with Indian dishes such as vegetable tikki.",
                    "Store in the refrigerator for 2&ndash;3 days."],
        ),
    },
]

MID_MEAL = [
    {
        "id": "mid-meal-guidelines",
        "title": "Mid-Meal Guidelines",
        "body": "\n".join([
            P("About 2&ndash;3 hours after lunch you might feel like snacking. Stick to "
              "fresh juices &mdash; no namkeens, biscuits or chips. If juices aren&rsquo;t "
              "enough, have herbal tea, fresh coconut slices or a small piece of fruit."),
            P("You can repeat any of the pre-breakfast detox juices "
              "(<a href=\"#food-ash-gourd-juice\">Ash Gourd Juice</a>, "
              "<a href=\"#food-ash-coco-juice\">Ash Coco Juice</a>, "
              "<a href=\"#food-coconut-water\">Coconut Water</a>) &mdash; just take them "
              "out fresh again."),
        ]),
    },
    {
        "id": "pink-power-juice",
        "title": "Pink Power Juice",
        "body": recipe(
            meta="Serves 2, makes 600 ml",
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
            meta="Serves 2, makes 600 ml",
            groups=[(None, ["2 cups chopped cucumber", "1 cup chopped bottle gourd",
                            "1 cup roughly chopped spinach, tightly packed",
                            "&frac14; cup mint leaves, tightly packed",
                            "2 cups chopped apple", "1 teaspoon lemon juice"])],
            method=["Juice all the ingredients together.",
                    "Add the lemon juice from the top and serve."],
            notes=["Tip: When juicing leafy greens like spinach and mint, alternate them "
                   "with watery ingredients such as cucumber and apple to keep the juicer moving."],
        ),
    },
    {
        "id": "clean-carrot-juice",
        "title": "Clean Carrot Juice",
        "body": recipe(
            meta="Serves 2, makes 600 ml",
            groups=[(None, ["2 cups chopped carrots", "3 cups chopped papaya", "2 oranges",
                            "1 coin ginger"])],
            method=["Juice all the ingredients together and serve."],
            notes=["Note: You can replace oranges with kinnow."],
        ),
    },
    {
        "id": "herbal-tea",
        "title": "Herbal Tea (Lemongrass)",
        "body": recipe(
            meta="Serves 2",
            intro=["A replacement for traditional Indian tea &mdash; no milk, no tea "
                   "leaves. It helps get rid of tea addiction. Use any fresh herb; "
                   "lemongrass is our favourite."],
            groups=[(None, ["2&ndash;3 inches lemongrass stems, chopped",
                            "cinnamon sticks, 2 inches", "6 green cardamom buds",
                            "&frac12; inch coin ginger", "2 cups water",
                            "1 teaspoon jaggery (optional)"])],
            method=["Bring the water to a boil in a saucepan.",
                    "Crush the lemongrass, cinnamon, cardamom and ginger in a mortar and "
                    "pestle. Add to the water and cover for 3 minutes to let the flavours infuse.",
                    "Strain the tea into cups.",
                    "If you like it sweetened, add jaggery from the top and serve."],
            notes=["Note: Instead of lemongrass, use rosemary, curry leaves, tulsi or rose."],
        ),
    },
]

DINNER_SALADS = [
    {
        "id": "dinner-guidelines",
        "title": "Dinner Guidelines",
        "body": P("For dinner, have a light meal &mdash; a salad or soup, or both, "
                  "depending on convenience. Have fruits for dinner if you ate your salad "
                  "meal for breakfast; have your grain meal for dinner if you ate your "
                  "salad meal for lunch."),
    },
    {
        "id": "carrot-raisin-salad",
        "title": "Carrot Raisin Salad",
        "body": recipe(
            meta="Serves 2 as a main meal",
            intro=["The raisins, tahini and carrots combine into an absolutely yummy dish. "
                   "Tahini is a paste made from sesame seeds, common in Mediterranean cuisine."],
            groups=[(None, ["3 cups shredded carrots",
                            "1 cup homegrown vegetable sprouts (alfalfa, clover, radish)",
                            "2 tablespoon finely chopped mint",
                            "&frac14; cup soaked cashews, chopped",
                            "3 tablespoons raisins (kishmish)"]),
                    ("Tahini Dressing",
                     ["1 cup white sesame seeds or 4 tablespoons homemade tahini",
                      "&frac12; cup water", "4 dates, seedless", "2 tablespoons lemon juice",
                      "1 tablespoon powdered jaggery", "&frac14; green chili",
                      "&frac12; teaspoon rock salt"])],
            method=[("Tahini",
                     ["Toast the sesame seeds in a saucepan over medium heat, stirring "
                      "constantly, until fragrant and very lightly coloured (not brown), "
                      "3&ndash;5 minutes. They burn quickly.",
                      "Once completely cooled, blend to a smooth paste, about 30 seconds "
                      "&mdash; extra smooth, not gritty."]),
                    ("Salad",
                     ["Blend 4 tablespoons tahini with water, dates, lemon juice, jaggery, "
                      "chili and salt until smooth.",
                      "Place the carrots, sprouts, mint, cashews and raisins in a large "
                      "mixing bowl. Pour the dressing on top and serve."])],
            prep=["Prepare vegetable sprouts."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "cheesy-salad",
        "title": "Cheesy Salad",
        "body": recipe(
            meta="Serves 2 (with a soup)",
            intro=["We don&rsquo;t need real cheese for a cheesy flavour &mdash; blend "
                   "soaked cashews with flavourings and it tastes even better than Parmesan."],
            groups=[(None, ["&frac12; cup cashews, soaked", "&frac14; cup coconut milk",
                            "&frac12; small green chili", "1 cup broccoli florets",
                            "1 cup thinly sliced baby corn", "1 cup chopped red bell pepper",
                            "1 cup chopped yellow bell pepper", "1 teaspoon rock salt",
                            "1 tablespoon dried oregano leaves"])],
            method=["Blend the cashews, coconut milk and green chili until smooth.",
                    "Steam the broccoli and baby corn together for about 5 minutes.",
                    "Pour the blended mixture into a mixing bowl. Add red and yellow bell "
                    "pepper, steamed broccoli, steamed baby corn, salt and oregano.",
                    "Mix well and serve."],
            prep=["Soak cashews in water for 6 hours.", "Prepare coconut milk."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "thai-papaya-salad",
        "title": "Thai Papaya Salad",
        "body": recipe(
            meta="Serves 2&ndash;3",
            intro=["A cleaner version of the Thai dish, made with only fresh, wholesome "
                   "ingredients. Crunchy and amazingly delicious."],
            groups=[(None, ["&frac12; small unripe green papaya", "1 large mango",
                            "1 medium carrot", "2 medium tomatoes",
                            "&frac12; cup fresh coriander"]),
                    ("Peanut Dressing (makes &frac13; cup)",
                     ["2 tablespoons soaked peanuts", "1 tablespoon lemon juice",
                      "&frac18; small green chili", "&frac12; teaspoon rock salt",
                      "1 tablespoon jaggery", "2 tablespoons water"]),
                    ("Topping", ["1 tablespoon raw peanuts, chopped"])],
            method=["Peel the skin of the papaya.",
                    "Cut the papaya and carrot into thin long strips (a julienne peeler works well).",
                    "Cut the mango and tomatoes into thin long strips with a knife.",
                    "Place the papaya, carrot, mango, tomatoes and coriander in a large "
                    "bowl and mix well.",
                    "Blend all the dressing ingredients until smooth.",
                    "Combine the dressing with the salad and mix well.",
                    "Top with chopped peanuts for an extra crunch."],
            prep=["Soak raw peanuts in water for about 3 hours."],
            notes=["Tip: Use the unripened green papaya &mdash; firm, green outside and "
                   "pale yellow inside &mdash; not the soft ripe orange one.",
                   "Note: When mango is not in season, use a soft pear."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "beet-rocket-salad",
        "title": "Beet Rocket Salad",
        "body": recipe(
            meta="Serves 2",
            intro=["A quick, simple salad that tastes wonderfully gourmet. Rocket leaves "
                   "have a spicy, mustard-like flavour balanced by the dates and beetroot."],
            groups=[(None, ["2 small beetroots, peeled", "2 cups chopped spinach leaves",
                            "1 cup chopped rocket leaves", "6 walnuts, soaked and crushed",
                            "&frac14; cup grated coconut",
                            "&frac12; avocado, chopped (optional)"]),
                    ("Middle Eastern Dressing",
                     ["&frac12; cup chopped cucumber", "4 dates, seedless",
                      "&frac14; cup coriander", "1&frac12; tablespoon lemon juice",
                      "&frac14; teaspoon cumin powder"])],
            method=["Chop the beetroot and steam until soft.",
                    "Place the steamed beetroot in a large mixing bowl with the spinach, "
                    "rocket, coconut, walnuts and avocado.",
                    "Blend all the dressing ingredients until smooth.",
                    "Pour the dressing over the salad, toss well and serve."],
            notes=["Note: If rocket leaves are not available, replace them with spinach leaves.",
                   "Tip: Add vegetable sprouts for maximum nutrition."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "zucchini-spaghetti",
        "title": "Zucchini Spaghetti",
        "body": recipe(
            meta="Serves 3 (with a soup)",
            intro=["Raw vegetables in place of cooked pasta &mdash; loaded with nutrients "
                   "and living enzymes. Serve with a fresh green salad."],
            groups=[("Spaghetti Sauce",
                     ["1&frac12; cup cherry tomatoes", "6 dates, seedless",
                      "1&frac12; tablespoon oregano",
                      "3 tablespoons fresh basil leaves (or 1 teaspoon dry)",
                      "1&frac12; tablespoon lemon juice", "2 teaspoons rock salt"]),
                    ("Zucchini Noodles", ["3 medium zucchinis"]),
                    ("Topping",
                     ["1 tablespoon crushed cashews",
                      "1 tablespoon thinly sliced sun-dried tomatoes",
                      "8 cherry tomatoes, halved", "&frac14; cup basil leaves"])],
            method=["Blend all the sauce ingredients until well combined.",
                    "Make spaghetti-style noodles from the zucchini with a spiraliser.",
                    "Right before serving, stir the sauce through the noodles. Don&rsquo;t "
                    "combine too far in advance or the zucchini releases water.",
                    "Top with cashews, sun-dried tomatoes, cherry tomatoes and basil. Serve."],
            bestfor=bf("Dinner"),
        ),
    },
]

DINNER_SOUPS = [
    {
        "id": "pumpkin-soup",
        "title": "Pumpkin Soup",
        "body": recipe(
            meta="Serves 2, makes 1200 ml",
            intro=["Rich, creamy and satisfying. The rosemary and thyme create a unique flavour."],
            groups=[("Soup Base",
                     ["&frac12; kg red pumpkin, with peel", "3 cups coconut milk",
                      "2 tablespoons fresh thyme (or 2 teaspoons dry)",
                      "1 stem fresh rosemary (or &frac12; teaspoon dry)",
                      "1 tablespoon rock salt", "&frac12; small green chili, chopped"]),
                    ("Toppings",
                     ["2 tablespoons pumpkin seeds", "&frac12; red bell pepper, in strips",
                      "&frac14; small coconut, in strips"])],
            method=["Chop the pumpkin into chunks &mdash; keep the peel on. Steam for about "
                    "20 minutes until soft.",
                    "Once cooled, blend with the coconut milk, thyme, rosemary, salt and "
                    "chili until smooth.",
                    "Pour into bowls, add the toppings and serve."],
            prep=["Prepare coconut milk."],
            notes=["Tip: Do not re-heat &mdash; never cook coconut milk on the stove.",
                   "Tip: Rosemary and thyme carry all the flavour; use dried if fresh is "
                   "unavailable."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "papaya-corn-soup",
        "title": "Papaya Corn Soup",
        "body": recipe(
            meta="Serves 2, makes 1400 ml",
            intro=["Green (unripe) papaya creates a beautiful symphony of flavours with "
                   "lemongrass, ginger and coconut."],
            groups=[("Soup Base",
                     ["3 cups peeled &amp; chopped green papaya (~1 small)",
                      "&frac12; small green chili, chopped", "2 teaspoons coriander seeds",
                      "1 teaspoon chopped ginger",
                      "1&frac12; tablespoons chopped lemongrass stalks",
                      "2&frac14; cups water", "1&frac12; tablespoon lemon juice",
                      "2 teaspoons rock salt", "2 cups coconut milk"]),
                    ("Topping", ["&frac14; cup corn, boiled", "&frac14; cup chopped coriander"])],
            method=["Steam the papaya until soft.",
                    "Meanwhile, dry roast the green chili, coriander seeds, ginger and "
                    "lemongrass together. Add &frac14; cup water and cook 2&ndash;3 minutes "
                    "till the flavours soak in.",
                    "Blend this spice mixture with the steamed papaya, 2 cups water, lemon "
                    "juice and salt until absolutely smooth.",
                    "Right before serving, add coconut milk and stir well.",
                    "Top with corn and coriander and serve. Do not re-heat."],
            prep=["Prepare coconut milk."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "spinach-singhara-soup",
        "title": "Spinach Singhara Soup",
        "body": recipe(
            meta="Serves 2, makes 1400 ml",
            intro=["Hearty and comforting. The coconut milk gives a subtle sweetness and "
                   "helps thicken it."],
            groups=[("Soup Base",
                     ["&frac12; kg spinach", "3 cups water",
                      "&frac34; cup singhara (water chestnuts), peeled and thinly sliced",
                      "2&frac12; teaspoons rock salt", "&frac12; teaspoon black pepper",
                      "&frac12; cup coconut milk"]),
                    ("Garnish",
                     ["microgreens (optional)", "marigold petals (optional)"])],
            method=["Heat the spinach and water on a low flame till the spinach is soft "
                    "(about 15 minutes).",
                    "Puree with a hand blender until smooth.",
                    "Pour through a sieve to remove any stalks.",
                    "Return to the stove on low flame. Add the sliced singhara and cook "
                    "about 3 minutes.",
                    "Turn off the heat and add salt and pepper.",
                    "Right before serving, add the coconut milk and stir well. Do not re-heat."],
            prep=["Prepare coconut milk."],
            notes=["Note: If singhara is not available, use potato."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "pea-carrot-soup",
        "title": "Pea Carrot Soup",
        "body": recipe(
            meta="Serves 2, makes 900 ml",
            groups=[("Soup Base",
                     ["1 cup fresh peas", "1 cup chopped carrot", "&frac12; cup chopped potatoes",
                      "2 small bay leaves", "&frac12; inch coin of ginger, chopped",
                      "3 cups water", "2 teaspoons lemon juice", "2 teaspoons rock salt"]),
                    ("Topping",
                     ["&frac12; cup fresh peas", "&frac12; cup chopped carrots, diced",
                      "&frac14; cup chopped coriander"])],
            method=[("Soup base",
                     ["Cook the peas, carrots, potatoes, bay leaves, ginger and water, "
                      "covered, on a low flame for about 15 minutes until soft.",
                      "Remove the bay leaves.",
                      "Puree with a hand blender until smooth.",
                      "Add lemon juice and salt from the top."]),
                    ("Topping",
                     ["Steam or boil the peas and carrots until soft.",
                      "Add the boiled peas, carrots and coriander to the soup base. Stir "
                      "well and serve warm."])],
            notes=["Note: Use only fresh peas (not frozen) and red winter carrots."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "broccoli-potato-soup",
        "title": "Broccoli Potato Soup",
        "body": recipe(
            meta="Serves 2&ndash;3, makes 1&frac12; litres",
            groups=[("Soup Base",
                     ["2&frac12; cups fresh broccoli, roughly cut",
                      "1&frac12; cups potatoes, roughly cut", "3 cups water",
                      "1&frac12; teaspoons rock salt", "1 inch fresh ginger, grated",
                      "&frac14; teaspoon black pepper powder", "1 cup coconut milk"]),
                    ("Topping",
                     ["1 cup fresh broccoli, roughly cut", "&frac12; carrot, in circles",
                      "&frac14; cup fresh coriander, chopped", "1 tablespoon pumpkin seeds"])],
            method=[("Soup base",
                     ["Add the broccoli, potato and water to a saucepan over medium heat. "
                      "Cover and cook 20 minutes, until the potatoes are fork-tender.",
                      "Add the ginger and cook another 3&ndash;4 minutes.",
                      "Remove from the stove and puree with an immersion blender.",
                      "Add the salt and pepper and mix well.",
                      "Right before serving, add the coconut milk."]),
                    ("Topping",
                     ["Steam the broccoli and carrot until soft. Add to the soup with "
                      "coriander and pumpkin seeds. Serve warm."])],
            prep=["Prepare coconut milk."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "tomato-soup",
        "title": "Tomato Soup",
        "body": recipe(
            meta="Serves 1&ndash;2, makes 700 ml",
            intro=["We do not cook tomatoes &mdash; their delicate Vitamin C is destroyed "
                   "by heat. Here we only blanch them to preserve their nutrition."],
            groups=[(None, ["8 medium tomatoes", "&frac14; cup chopped bottle gourd",
                            "&frac14; cup chopped carrot", "&frac14; cup chopped potato",
                            "&frac14; cup chopped red bell pepper", "1&frac12; cups water",
                            "&frac12; teaspoon dry rosemary", "&frac34; teaspoon rock salt",
                            "&frac14; teaspoon black pepper powder",
                            "&frac12; teaspoon dry oregano"])],
            method=["Dip the tomatoes in hot water for 15 minutes, covered with a plate. "
                    "Then peel off the skin and remove the seedy part.",
                    "Cook the bottle gourd, carrot, potato and bell pepper in 1&frac12; "
                    "cups water, covered, for 15 minutes.",
                    "Blend these vegetables and water with the peeled, de-seeded tomatoes "
                    "and rosemary until smooth.",
                    "Mix in the salt, pepper and oregano. Serve."],
            bestfor=bf("Dinner"),
        ),
    },
    {
        "id": "carrot-cumin-soup",
        "title": "Carrot Cumin Soup",
        "body": recipe(
            meta="Serves 2, makes 1 litre",
            groups=[("Soup Base",
                     ["1 teaspoon cumin seeds", "1 inch coin of ginger, chopped",
                      "&frac12; teaspoon coriander powder", "2 cups chopped carrots",
                      "1 cup cauliflower florets", "3 cups water", "1 bay leaf",
                      "1 cup coconut milk", "2 teaspoons rock salt",
                      "&frac12; teaspoon black pepper"]),
                    ("Topping",
                     ["2 tablespoons chopped coriander", "2 tablespoons chopped mint"])],
            method=["Heat a saucepan over medium heat. Add cumin seeds, ginger and "
                    "coriander powder and cook one minute till fragrant.",
                    "Add the carrot and cauliflower and cook 5 minutes, stirring occasionally.",
                    "Pour in the water and add the bay leaf. Bring to a boil, then partially "
                    "cover, reduce heat and simmer 20 minutes.",
                    "Blend with a hand blender.",
                    "Add salt and pepper and stir well.",
                    "Right before serving, add coconut milk and stir.",
                    "Garnish with coriander and mint and serve warm."],
            prep=["Prepare coconut milk."],
            bestfor=bf("Dinner"),
        ),
    },
]

OCCASIONAL = [
    {
        "id": "occasional-intro",
        "title": "Occasional Recipes",
        "body": P("Exotic and delicious recipes for Satvic dinner parties &mdash; to "
                  "inspire friends and family to join you in eating in sync with Mother "
                  "Nature. Eat these occasionally, not daily."),
    },
    {
        "id": "coconut-chaas",
        "title": "Coconut Chaas",
        "body": recipe(
            meta="Serves 2, makes 750 ml",
            groups=[(None, ["2 cups coconut milk", "1 cup water", "&frac14; cup mint leaves",
                            "2&frac12; tablespoon lemon juice", "1&frac12; teaspoon rock salt",
                            "1 teaspoon roasted cumin powder (bhuna jeera)"])],
            method=["Blend everything except the roasted cumin powder until smooth.",
                    "Add the roasted cumin powder from the top and stir well. Cool in the "
                    "refrigerator for a while and serve."],
        ),
    },
    {
        "id": "thandai",
        "title": "Thandai",
        "body": recipe(
            meta="Serves 3, makes 600 ml",
            groups=[(None, ["8 almonds, soaked &amp; drained",
                            "1 tablespoon fennel, soaked 1 hour &amp; drained",
                            "1 tablespoon poppy seeds, soaked 1 hour &amp; drained",
                            "1&frac12; cups coconut milk", "&frac12; cup water",
                            "4 dates, seedless", "1 teaspoon powdered jaggery",
                            "&frac18; teaspoon rock salt", "&frac18; teaspoon black pepper"]),
                    ("Garnish", ["chopped pistachio, saffron &amp; dried rose petals"])],
            method=["Blend everything except coconut milk until smooth.",
                    "Add coconut milk and blend again.",
                    "Cool in the refrigerator for a while. Garnish and serve."],
        ),
    },
    {
        "id": "chocolate-smoothie-bowl",
        "title": "Chocolate Smoothie Bowl",
        "body": recipe(
            meta="Serves 2, makes 700 ml",
            groups=[(None, ["3 frozen bananas", "&frac14; cup water",
                            "1 cup coconut cream (malai)*", "1 coin ginger",
                            "2 dates, seedless",
                            "1 tablespoon cacao powder or carob powder",
                            "&frac12; teaspoon cinnamon powder",
                            "seasonal fruits and nuts for topping"])],
            method=["Blend the frozen bananas, water, coconut cream, cacao powder, ginger "
                    "and cinnamon.",
                    "Pour into bowls and top with fresh seasonal fruits and nuts (banana, "
                    "grapes, kiwi, figs, almonds, cacao nibs, chia seeds)."],
            prep=["Peel, slice and freeze the bananas for about 6 hours."],
            notes=["Note: *If coconut cream (malai) is unavailable, use fresh grated coconut.",
                   "Tip: Focus on fresh, water-rich fruits for the topping; go easy on nuts and seeds."],
            bestfor=bf("Breakfast", "An Occasional Treat"),
        ),
    },
    {
        "id": "blush-smoothie-bowl",
        "title": "Blush Smoothie Bowl",
        "body": recipe(
            meta="Serves 2, makes 700 ml",
            intro=["Pure, clean, oxygen-powered energy &mdash; the perfect post-workout breakfast."],
            groups=[(None, ["2 frozen bananas", "3 chopped soft pears*",
                            "&frac12; cup chopped beetroot",
                            "any seasonal fruits and nuts for topping"])],
            method=["Blend the pears, beetroot and frozen bananas until smooth.",
                    "Pour into bowls and top with fresh seasonal fruits and nuts (papaya, "
                    "chikoo, kiwi, coconut, pumpkin seeds, goji berries, chia seeds)."],
            prep=["Peel, slice and freeze the bananas for about 6 hours."],
            notes=["Note: *If pear is unavailable, use soft apples.",
                   "Tip: Use the soft variety of pears &mdash; they should give a little "
                   "when pressed with your thumb."],
            bestfor=bf("Breakfast", "An Occasional Treat"),
        ),
    },
    {
        "id": "spinach-smoothie-bowl",
        "title": "Spinach Smoothie Bowl",
        "body": recipe(
            meta="Serves 2, makes 600 ml",
            intro=["Delicious and simple &mdash; just 10 minutes, raw, only fruits and "
                   "vegetables. It makes a big breakfast, so eat occasionally."],
            groups=[(None, ["4 frozen bananas", "&frac34; cup shredded coconut",
                            "2 cups spinach", "4 dates, seedless",
                            "&frac12; teaspoon cinnamon powder", "2 teaspoons lemon juice",
                            "any seasonal fruits and nuts for topping"])],
            method=["Blend the shredded coconut, spinach, dates, cinnamon, lemon juice and "
                    "frozen bananas until smooth.",
                    "Pour into bowls and top with fresh seasonal fruits and nuts (kiwi, "
                    "strawberries, grapes, almonds, sunflower seeds, chia seeds)."],
            prep=["Peel, slice and freeze the bananas for about 6 hours."],
            bestfor=bf("Breakfast", "An Occasional Treat"),
        ),
    },
    {
        "id": "thai-curry",
        "title": "Thai Curry with Brown Rice",
        "body": recipe(
            meta="Serves 3, makes 900 ml",
            intro=["An easy Thai curry packed with vegetables. No need for pre-packaged "
                   "curry paste when you can make it with fresh herbs at home."],
            groups=[("Paste",
                     ["&frac12; cup water", "2 teaspoons coriander seeds",
                      "2 teaspoons cumin seeds", "1 inch coin galangal",
                      "1 tablespoon powdered jaggery",
                      "&frac14; cup chopped lemongrass stalks", "1 teaspoon lemon zest",
                      "12 kaffir lime leaves", "&frac12; teaspoon black peppercorns",
                      "1 small green chili"]),
                    ("Curry",
                     ["3 cups lightly boiled vegetables (carrots, broccoli, sweet potato, "
                      "beans, baby corn)", "&frac14; cup chopped bell peppers",
                      "1&frac12; cup thick coconut milk", "2 teaspoon lemon juice",
                      "1 tablespoon rock salt",
                      "2 tablespoon peanuts, roasted and crushed", "Brown rice, cooked"])],
            method=["Blend all the paste ingredients until absolutely smooth.",
                    "Pour the paste into a pan and cook on a low flame for 5 minutes.",
                    "Add the lightly boiled vegetables and bell peppers and stir well for 5 minutes.",
                    "Switch off the stove. Add the coconut milk, lemon juice and salt. Stir "
                    "well &mdash; do not cook coconut directly over the stove.",
                    "Add the crushed roasted peanuts.",
                    "Serve with brown rice."],
            prep=["Prepare thick coconut milk by blending 1 cup coconut with 1 cup water "
                  "and straining."],
            notes=["Note: If galangal is unavailable, use fresh ginger."],
            bestfor=bf("Lunch", "An Occasional Treat"),
        ),
    },
    {
        "id": "vegetable-tikki",
        "title": "Vegetable Tikki",
        "body": recipe(
            meta="Makes 7 tikkis",
            intro=["Made of only vegetables &mdash; bottle gourd replaces potato to make "
                   "them easily digestible. Delicious with the two chutneys."],
            groups=[(None, ["&frac34; cup bottle gourd, finely grated",
                            "&frac12; cup cauliflower, chopped", "&frac18; cup green peas",
                            "&frac18; cup carrot, chopped",
                            "1&frac12; tablespoon flax seed, powdered*",
                            "1 tablespoon coriander, chopped",
                            "&frac12; tablespoon mint leaves, chopped",
                            "1 teaspoon green chillies, finely chopped",
                            "&frac12; teaspoon cumin seeds", "1 teaspoon lemon juice",
                            "&frac14; teaspoon rock salt",
                            "extra flax seed powder for rolling",
                            "Date Chutney &amp; Green Chutney, to serve"])],
            method=["Blend all ingredients except salt and bottle gourd until combined. "
                    "Take the batter out in a bowl.",
                    "Squeeze the water out of the grated bottle gourd, then combine it with "
                    "the batter.",
                    "Add salt right before rolling the tikkis.",
                    "Divide into 7 balls and flatten each into a thin tikki. Roll in flax "
                    "powder till evenly coated.",
                    "Cook on a medium flame, pressing with a spatula, till golden brown on "
                    "both sides. Do not use oil.",
                    "Serve hot with Sweet Date Chutney and Green Chutney."],
            notes=["Note: *Flax seed powder is made by blending dry flax seeds in a blender."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "chia-pudding",
        "title": "Chia Pudding",
        "body": recipe(
            meta="Serves 2&ndash;3, makes 500 ml",
            intro=["Super easy &mdash; make it in advance so it has time to thicken. Fully raw."],
            groups=[(None, ["1 cup coconut milk", "1&frac12; tablespoon powdered jaggery",
                            "&frac12; ripe banana", "&frac18; teaspoon rock salt",
                            "2 tablespoons chia seeds",
                            "1 cup chopped mixed fruits (banana, mango, grapes, pear, kiwi, "
                            "orange, pomegranate, berries)"]),
                    ("Garnish", ["edible flowers (optional)", "fresh seasonal fruits"])],
            method=["Blend coconut milk, jaggery, banana and salt until smooth.",
                    "Pour over the chia seeds and let them soak for about 2 hours on the "
                    "counter &mdash; they swell up and thicken the mixture.",
                    "Add the chopped fruits. Refrigerate 30 minutes before serving."],
            prep=["Prepare coconut milk."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "satvic-kheer",
        "title": "Satvic Kheer",
        "body": recipe(
            meta="Serves 4&ndash;5, makes 1 litre",
            intro=["Kheer that is healthy &mdash; no sugar, no milk, no ghee."],
            groups=[(None, ["1 cup soaked almonds", "&frac12; cup quinoa", "3&frac12; cups water",
                            "6 tablespoons powdered jaggery",
                            "&frac14; teaspoon cardamom powder",
                            "20 strands of saffron (approx.)", "&frac18; teaspoon rock salt"]),
                    ("Topping",
                     ["1 tablespoon chopped almonds", "1 tablespoon chopped pistachios",
                      "1 tablespoon raisins"])],
            method=["Cook the quinoa in a saucepan with 2 cups water; bring to a boil, then "
                    "simmer about 45 minutes until fully cooked.",
                    "Meanwhile, blend the peeled almonds with 1&frac12; cups water until very smooth.",
                    "Add jaggery, cardamom, saffron and salt and blend again.",
                    "Pour into a bowl, add the boiled quinoa and stir well.",
                    "Refrigerate at least 30 minutes &mdash; the quinoa swells and the "
                    "kheer thickens.",
                    "Top with almonds, pistachios and raisins and serve."],
            prep=["Soak the almonds in water for about 6 hours, then peel them."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "satvic-gajar-halwa",
        "title": "Satvic Gajar Halwa",
        "body": recipe(
            meta="Serves 6",
            groups=[(None, ["4 cups finely shredded red carrots", "20 strands of saffron",
                            "&frac13; cup powdered jaggery",
                            "1 teaspoon green cardamom powder", "&frac14; teaspoon rock salt",
                            "1 teaspoon lemon juice"]),
                    ("Thick Coconut Milk",
                     ["&frac12; cup dessicated coconut", "&frac12; cup water"]),
                    ("Date Paste",
                     ["&frac12; cup chopped dates, seedless", "&frac14; cup warm water"]),
                    ("Topping",
                     ["&frac14; cup chopped almonds (soaked)",
                      "&frac14; cup chopped cashews (soaked)",
                      "2 tablespoons chopped pistachios"])],
            method=["Cook the grated carrots and saffron on medium heat for about 30 "
                    "minutes, till all the water is absorbed and the carrots are soft.",
                    "Meanwhile, blend the dates and warm water into a smooth paste.",
                    "Blend the coconut and water for the thick coconut milk; strain through "
                    "a nut milk bag / muslin cloth and keep the liquid.",
                    "Once the carrots are cooked, reduce the flame to low. Add jaggery and "
                    "date paste and stir 30 seconds.",
                    "Switch off the stove. Add the thick coconut milk, stir and immediately "
                    "close the lid &mdash; let it cook from the heat inside the pan, not on flame.",
                    "Add cardamom, lemon and salt. Stir.",
                    "Add almonds, cashews and pistachios. Stir and serve warm."],
            notes=["Tip: Use red carrots (available only in winter).",
                   "Tip: Refrigerate for 30 minutes before serving for even better taste."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "kulfi",
        "title": "Kulfi",
        "body": recipe(
            meta="Serves 2&ndash;3, makes 1&frac12; cups",
            intro=["No ice cream maker needed. The base is cashew and coconut."],
            groups=[("Kulfi Ice Cream",
                     ["&frac12; cup soaked cashews", "1 cup coconut malai",
                      "&frac14; cup jaggery, powdered", "4 dates, seedless",
                      "&frac13; cup coconut water", "10 strands of saffron",
                      "&frac18; teaspoon green cardamom powder", "&frac18; teaspoon rock salt"]),
                    ("Topping", ["1 tablespoon chopped pistachios"])],
            method=["Blend all the ice cream ingredients until smooth.",
                    "Pour into a shallow glass dish or steel container and freeze for about 6 hours.",
                    "Before serving, thaw on the counter 15&ndash;30 minutes until soft enough to scoop.",
                    "Top with chopped pistachios and serve."],
            prep=["Soak the cashews in water for about 6 hours."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "peanut-butter-ice-cream",
        "title": "Peanut Butter Ice Cream",
        "body": recipe(
            meta="Serves 3, makes 1&frac12; cups",
            intro=["Ultra creamy, nutty and sweet &mdash; no sugar, no cream, no milk."],
            groups=[("For the peanut butter", ["1 cup peanuts"]),
                    ("For the ice cream",
                     ["6 dates, seedless", "&frac14; cup water", "4 frozen bananas",
                      "1 tablespoon peanut butter", "&frac12; tablespoon powdered jaggery",
                      "&frac18; teaspoon rock salt"]),
                    ("Topping",
                     ["1 tablespoon almonds, chopped",
                      "1 tablespoon date paste (optional)", "few banana slices"])],
            method=[("Peanut butter",
                     ["Heat a pan, add the peanuts and reduce the flame to low. Roast, "
                      "stirring continuously, for 4&ndash;5 minutes.",
                      "Blend for 2&ndash;3 minutes till creamy &mdash; it first turns to "
                      "powder, then creamy. Add no water."]),
                    ("Ice cream",
                     ["Blend the dates and water into a paste.",
                      "Add the frozen bananas, peanut butter, jaggery and salt and blend "
                      "again until smooth. Do not over-blend.",
                      "Scoop into bowls, top with almonds, date paste and banana slices, "
                      "and serve immediately."])],
            prep=["Peel, slice and freeze the bananas for about 6 hours."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "satvic-ladoo",
        "title": "Satvic Ladoo",
        "body": recipe(
            meta="Makes 12 ladoos",
            groups=[(None, ["1 dry coconut (gola)", "1 tablespoon almond butter*",
                            "2 tablespoons powdered jaggery",
                            "2 tablespoons soaked almonds, crushed"])],
            method=["Break the dry coconut into pieces and shred it finely.",
                    "Blend the shredded coconut in a high-speed blender until creamy, "
                    "scraping down the sides &mdash; it first turns to powder, then soft "
                    "and buttery (5&ndash;7 minutes). Let it cool if it overheats.",
                    "Add the coconut butter to a bowl with the almond butter, jaggery and "
                    "chopped almonds. Mix well with your hands.",
                    "Shape into small ladoos. Garnish with dry rose petals and serve."],
            prep=["Soak the almonds in water for 5&ndash;6 hours."],
            notes=["Note: *Almond butter &mdash; soak 1 cup almonds 4&ndash;6 hours, drain, "
                   "dry roast 5&ndash;7 minutes, cool, then blend until creamy (powder "
                   "first, then creamy). Store in the refrigerator up to 1 week."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
    {
        "id": "lemon-cheesecake",
        "title": "Lemon Cheesecake",
        "body": recipe(
            meta="Serves 5",
            intro=["No dairy, cheese or sugar &mdash; but it contains lots of cashews, so "
                   "eat sparingly."],
            groups=[("Cheesecake",
                     ["1 cup cashews, soaked", "3 tablespoons powdered jaggery",
                      "&frac14; cup water", "3 tablespoons lemon juice"]),
                    ("Lime Gel",
                     ["&frac14; cup cashews, soaked overnight", "&frac14; cup powdered jaggery",
                      "4 medium leaves of spinach", "&frac12; tablespoon lemon juice",
                      "&frac12; tablespoon lemon zest (finely grated lemon peel)"]),
                    ("Ginger Crumble",
                     ["&frac12; cup almonds", "&frac12; tablespoon jaggery powder",
                      "&frac14; teaspoon ginger, grated", "pinch salt"]),
                    ("Garnish (optional)", ["microgreens", "edible flowers"])],
            method=["Blend all the cheesecake ingredients. Pour into a pan and chill in the "
                    "freezer 5&ndash;6 hours. Once frozen, cut into shapes and keep "
                    "refrigerated until serving.",
                    "Blend all the lime gel ingredients until perfectly smooth. Pour into a "
                    "squeeze bottle and refrigerate.",
                    "For the ginger crumble, quickly pulse the almonds, then mix in the "
                    "rest by hand.",
                    "Sprinkle 3 piles of ginger crumble on a plate, place a piece of "
                    "cheesecake on each, and garnish with lime gel, microgreens and edible "
                    "flowers."],
            prep=["Soak the cashews in water for 5&ndash;6 hours."],
            bestfor=bf("An Occasional Treat"),
        ),
    },
]

SKINCARE = [
    {
        "id": "rose-cleanser",
        "title": "Rose Cleanser for Face &amp; Body",
        "body": recipe(
            meta="Makes 1 batch",
            intro=["A 3-ingredient face and body cleanser, 100% natural and edible, under "
                   "5 minutes to make. Good for all skin types &mdash; dry, oily and sensitive."],
            groups=[(None, ["1 cup oats", "10 almonds", "&frac14; cup dry rose petals"])],
            method=["Blend all the ingredients together into a powder. Store in an airtight "
                    "container for up to 2 weeks.",
                    "To use, take a spoonful in a small cup and mix with water to form a paste.",
                    "Rinse your skin with running water. Apply the paste to your face or "
                    "body, massaging in a circular motion for 3&ndash;5 minutes so the "
                    "granules remove dead skin cells.",
                    "Rinse off well &mdash; your skin looks and feels refreshed."],
            notes=["Tip: Keep water out of the container or the powder may grow mold."],
        ),
    },
]

SUBJECT = {
    "id": "food",
    "name": "Satvic Food",
    "tag": "The Food Book",
    "blurb": "The Satvic Food philosophy &mdash; what Satvic means, the 4 principles, the "
             "21 food laws, digestion and food combining &mdash; plus how to set up a "
             "Satvic kitchen, the meal plans, and the full recipe collection from "
             "pre-breakfast to occasional treats.",
    "accent": "#4f7bb0",
    "sections": [
        {"id": "philosophy", "name": "Food Philosophy", "pages": PHILOSOPHY},
        {"id": "kitchen", "name": "Setting Up a Satvic Kitchen", "pages": KITCHEN},
        {"id": "meal-plan", "name": "Satvic Meal Plan", "pages": MEAL_PLAN},
        {"id": "pre-breakfast", "name": "Recipes &middot; Pre-Breakfast", "pages": PRE_BREAKFAST},
        {"id": "breakfast", "name": "Recipes &middot; Breakfast", "pages": BREAKFAST},
        {"id": "lunch", "name": "Recipes &middot; Lunch", "pages": LUNCH},
        {"id": "mid-meal", "name": "Recipes &middot; Mid-Meal", "pages": MID_MEAL},
        {"id": "dinner-salads", "name": "Recipes &middot; Dinner: Salads", "pages": DINNER_SALADS},
        {"id": "dinner-soups", "name": "Recipes &middot; Dinner: Soups", "pages": DINNER_SOUPS},
        {"id": "occasional", "name": "Recipes &middot; Occasional", "pages": OCCASIONAL},
        {"id": "skincare", "name": "Skin Care", "pages": SKINCARE},
    ],
}
