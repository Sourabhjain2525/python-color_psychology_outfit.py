mood_dict = {
    "happy": "yellow",
    "sad": "pink",
    "angry": "black",
    "stressed": "blue",
    "relaxed": "green",
    "energetic": "red",
    "confident": "red",
    "calm": "blue",
    "serious": "black",
    "peaceful": "green",
    "motivated": "red",
    "caring": "pink",
    "cheerful": "yellow"
}

outfit_suggestions = {
    "red": ["red blazer", "red sneakers", "red dress"],
    "blue": ["blue jeans", "blue shirt", "blue hoodie"],
    "yellow": ["yellow t-shirt", "yellow sundress", "yellow top"],
    "green": ["green jacket", "green scarf", "green cargo pants"],
    "black": ["black suit", "black boots", "black trousers"],
    "pink": ["pink blouse", "pink sweater", "pink skirt"]
}

def get_user_mood():
    mood = input("How are you feeling today? (e.g., happy, sad, energetic, stressed): ").strip().lower()
    return mood

def get_color_for_mood(mood):
    return mood_dict.get(mood, None)

import random
def suggest_outfit(color):
    if color in outfit_suggestions:
        return random.choice(outfit_suggestions[color])
    return "a neutral outfit (white t-shirt and jeans)"

def main():
    print("🎨 Welcome to the Color Psychology Outfit Recommender!")
    mood = get_user_mood()

    color = get_color_for_mood(mood)
    if color:
        outfit = suggest_outfit(color)
        print(f"Since you're feeling {mood}, we recommend wearing {color} today.")
        print(f"Suggested outfit: {outfit}")
    else:
        print("Sorry, we couldn't identify that mood. Try a different or simpler word (e.g., happy, stressed).")


