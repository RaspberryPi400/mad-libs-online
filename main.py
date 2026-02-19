# Ask the user which story they want
story = input("Which story would you like? (1. Cooking show) (2. Sci-Fi Mission) (3. Medieval Quest): ")

# If the user chose the first story, then ask these questions:
if story == "1":
    one = input("Type of Liquid: ")
    two = input("Plural Noun (Kitchen Tool): ")
    three = input("Adjective: ")
    four = input("Specific Vegetable: ")
    five = input("Verb (Action): ")
    six = input("Unit of Time: ")
    seven = input("Gross Food Item: ")
    eight = input("Noun: ")

# First story
    cooking_show = f"""Welcome back to Extreme Chef.
Our contestant today is attempting a bold move: deglazing the pan with a splash of {one}.
The judges look nervous, especially since he's using a pair of {two} instead of a spatula.
'This dish needs to feel {three},' the chef whispers, aggressively tossing a handful of shredded {four} into the air.
He begins to {five} around the kitchen, claiming the flavor needs to develop for at least one {six}.
For the final touch, he garnishes the plate with a single, wilted {seven} and serves it on a literal {eight}.
The head judge takes one bite, turns pale, and asks for a trash can."""

# Print the filled-in story
    print("Here is the story you made!")
    print(cooking_show)

# If the user chose the second story:
elif story == "2":
    one = input("Adjective: ")
    two = input("Noun (Part of a Ship): ")
    three = input("Verb (Ending in -ing): ")
    four = input("Number: ")
    five = input("Plural Noun (Living Things): ")
    six = input("Noun: ")
    seven = input("Silly Word: ")
    eight = input("Exclamation: ")

# Second story
    sci_fi_mission = f"""Captain's Log, Stardate {four}. Our mission to the Andromeda Galaxy has hit a {one} snag.
While we were {three} through the Horsehead Nebula, the ship's {two} suddenly began to glow bright purple and hum a low tune.
Before I could hit the emergency eject button, a group of wild {five} teleported onto the bridge.
They didn't want our technology; they just wanted to trade us a mysterious {six} for all of our freeze-dried ice cream.
My first officer shouted, '{eight}!' but it was too late.
We are now drifting toward a black hole named {seven}, and the only thing left to do is hope the engines start working before dinner."""
    
# Print the filled-in story
    print("Here is the story you made!")
    print(sci_fi_mission)

# If the user chose the third story:
elif story == "3":
    one = input("Adjective: ")
    two = input("Noun (Weapon/Tool): ")
    three = input("Verb: ")
    four = input("Mythical Creature: ")
    five = input("Plural Noun (Body Parts): ")
    six = input("Noun (Object): ")
    seven = input("Adverb: ")
    eight = input("Exclamation: ")

# Third story
    medieval_quest = f"""Sir Lancelot set off on a/an {one} journey to rescue the kingdom's crown.
Instead of a sword, he accidentally grabbed a {two} from the castle kitchen.
When he reached the Dark Cave, he tried to {three}, but he was immediately blocked by a giant, three-headed {four}.
The beast looked at him, blinked its six {five}, and offered him a deal:
he could have the crown back if he could successfully balance a/an {six} on his nose for ten minutes.
Lancelot tried to do it {seven}, but he sneezed and shouted '{eight}!' The crown was lost forever, but he did get a free souvenir mug."""
    
# Print the filled-in story.
    print("Here is the story you made!")
    print(medieval_quest)