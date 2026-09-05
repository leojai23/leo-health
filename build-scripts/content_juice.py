# -*- coding: utf-8 -*-
"""Satvic Juice — the 3-Day Juice Diet (Satvic Movement introduction manual)."""
from helpers import P, H2, H3, UL, OL, NOTE, TIP, recipe

SUBJECT = {
    "id": "juice",
    "name": "Satvic Juice",
    "tag": "3-Day Juice Diet",
    "blurb": "The Satvic Movement 3-day juice fast — a short, guided break from solid "
             "food to give the digestive system a rest. Prep, shopping list, the three "
             "juices, the daily schedule and FAQs.",
    "accent": "#c98a2b",
    "sections": [
        {
            "id": "guide",
            "name": "The Fast",
            "pages": [
                {
                    "id": "intro",
                    "title": "A Letter For You",
                    "body": "\n".join([
                        P("Dear Friends,",
                          "We would like to express our deepest gratitude to you for joining us "
                          "for this juice fast. We are excited that you have taken out three days "
                          "of your life for cleansing your body and spirit. We will be here to "
                          "inspire and hand-hold you at all times.",
                          "During these three days, we&rsquo;ll share with you immense knowledge on "
                          "fasting, watch some very inspiring documentaries together and take lots "
                          "of photos &amp; videos to share with the community. So be prepared for "
                          "three fun-filled, exciting days of a solid food vacation!",
                          "The best part about this juice fast is that we are in this together as a "
                          "community. You are not alone. Not only do you have our support, but also "
                          "the support of hundreds of others who are juice fasting with you in "
                          "their own cities.",
                          "We request that you read this document carefully, as it contains "
                          "information to ensure that you have a great experience.",
                          "We feel blessed to be sharing these three days with you.",
                          "&mdash; Harshvardhan and Subah"),
                        NOTE("Both knowledge sessions and the Q&amp;A are hosted through online "
                             "webinars. Sessions are recorded and the link is shared with you, but "
                             "replays are only available for 24 hours &mdash; the juice fast is "
                             "meant to be a live experience."),
                    ]),
                },
                {
                    "id": "prepare",
                    "title": "How to Prepare for the Fast",
                    "body": "\n".join([
                        P("To get the maximum benefit of the fast, minimise the intake of the "
                          "food items below from now until the fast starts. Doing so takes the "
                          "unnecessary load off the digestive system."),
                        H2("Last meal before the fast"),
                        P("Have a very light meal in the evening of the day before the fast &mdash; "
                          "just a simple bowl of soup or fruit is recommended. This gives your body "
                          "an indication to start preparing for the fast."),
                        H2("Avoid (from now till the fast)"),
                        UL(["Alcohol",
                            "Tea and coffee",
                            "Soda and aerated drinks",
                            "Processed, junk and fried food",
                            "All animal products (milk, cheese, eggs, butter, yoghurt, fish and meat)"]),
                        H2("Add"),
                        UL(["Fruits", "Salads", "Juices"]),
                    ]),
                },
                {
                    "id": "shopping-list",
                    "title": "Shopping List",
                    "body": "\n".join([
                        P("Shopping list for all 3 days:"),
                        UL(["1 big ash gourd (or 2 small ash gourds)",
                            "3 drinking coconuts",
                            "6 apples",
                            "3 beetroots",
                            "12 carrots",
                            "18 big cucumbers",
                            "3 bunches spinach",
                            "2 bunches mint",
                            "2 bunches coriander",
                            "6 pieces ginger",
                            "12 lemons"]),
                        NOTE("If you cannot find any of the ingredients above, don&rsquo;t worry &mdash; "
                             "you can make juices out of any vegetables available. However, please "
                             "try to find all ingredients for the green juice, as it will be your "
                             "most important juice."),
                    ]),
                },
                {
                    "id": "juices",
                    "title": "The Three Juices",
                    "body": "\n".join([
                        P("Approximately 4&ndash;8 glasses of juice per day. We strictly recommend "
                          "<em>not</em> drinking pure fruit juices during the fast &mdash; you may "
                          "add &frac12; an apple to a juice for sweetness, but avoid fruit-only juice."),
                        H2("ABC Juice"),
                        P("<strong>11:30 AM.</strong> Apple &ndash; Beetroot &ndash; Carrot."),
                        UL(["&frac12; apple",
                            "1 beetroot",
                            "3&ndash;4 carrots",
                            "1 inch ginger"]),
                        H2("Ash Gourd Juice / Coconut Water"),
                        P("<strong>7:00 AM.</strong> Make sure to remove the seeds and peel from "
                          "the ash gourd before juicing it. Or simply have fresh coconut water."),
                        H2("Green Juice"),
                        P("<strong>2:00 PM.</strong> Your most important juice."),
                        UL(["2 cucumbers or &frac12; bottle gourd (lauki)",
                            "handful spinach",
                            "&frac12; apple",
                            "handful mint / coriander",
                            "&frac12; lemon",
                            "1 inch ginger"]),
                        NOTE("At 4:30 PM and 9:00 PM you can repeat Ash Gourd Juice OR Coconut Water "
                             "OR Green Juice. If you don&rsquo;t have a juicer, blend the vegetables "
                             "and fruits with a little water and then sieve them."),
                    ]),
                },
                {
                    "id": "daily-schedule",
                    "title": "Daily Schedule",
                    "body": "\n".join([
                        OL([
                            "<strong>7:00 am</strong> &mdash; First Juice: Ash Gourd Juice or Coconut Water",
                            "<strong>10:00 &ndash; 11:30 am</strong> &mdash; Knowledge Session I",
                            "<strong>11:30 am</strong> &mdash; Second Juice: Apple, Beetroot, Carrot (ABC) Juice",
                            "<strong>12:30 &ndash; 2:00 pm</strong> &mdash; Knowledge Session II",
                            "<strong>2:00 pm</strong> &mdash; Third Juice: Green Juice",
                            "<strong>2:30 &ndash; 4:30 pm</strong> &mdash; Take rest + watch documentary",
                            "<strong>4:30 pm</strong> &mdash; Fourth Juice: Ash Gourd Juice / Coconut Water / Green Juice",
                            "<strong>6:00 &ndash; 9:00 pm</strong> &mdash; Q&amp;A Session",
                            "<strong>9:00 pm</strong> &mdash; Fifth Juice (optional): Ash Gourd Juice / Coconut Water / Green Juice",
                        ]),
                        NOTE("Both knowledge sessions and the Q&amp;A are hosted through online webinars."),
                    ]),
                },
                {
                    "id": "faq",
                    "title": "Frequently Asked Questions",
                    "body": "\n".join([
                        H3("What is a juice fast?"),
                        P("We drink only fresh juices for 3 days. No solid food is allowed on this fast."),
                        H3("Is it essential for me to do the fast, or can I just attend to learn about juice fasting?"),
                        P("It is essential to do the 3-day fast with us. Only then will you get the "
                          "maximum benefit from this workshop."),
                        H3("Is it safe?"),
                        P("Yes, it is absolutely safe. People who are pregnant or on very high "
                          "medication need to make a few adjustments &mdash; if you belong in this "
                          "category, please let us know and we will guide you."),
                        H3("I have health problems / I&rsquo;m diabetic, can I still fast?"),
                        P("Yes, you can fast. Just ensure you consult your doctor beforehand."),
                        H3("How many juices can I have in a day?"),
                        P("Approximately 4&ndash;8 glasses of juice per day."),
                        H3("What if I don&rsquo;t have access to the vegetables and fruits you mentioned?"),
                        P("You can prepare juices with any available vegetables. It is not important "
                          "to drink a specific juice &mdash; we just want to give the digestive "
                          "system a break from solid food."),
                        H3("Do I need organic vegetables?"),
                        P("Not necessarily. However, if you can manage to get organic vegetables, that&rsquo;s the best."),
                        H3("I don&rsquo;t have a juicer, can I still participate?"),
                        P("Yes. You can do a coconut water fast, or make juices using a blender / "
                          "mixer &mdash; simply add the vegetables and fruits to the blender and "
                          "then sieve them."),
                        H3("Will I be able to watch the replay of the live webinars later?"),
                        P("All online webinar sessions are recorded and the link is shared with "
                          "you. However, the replays are only available for 24 hours from the time "
                          "the session ends. Unless there are network problems, we insist that you "
                          "watch it live."),
                    ]),
                },
            ],
        },
    ],
}
