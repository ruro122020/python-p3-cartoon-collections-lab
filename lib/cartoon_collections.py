def roll_call_dwarves(list):
  for i, dwarf in enumerate(list):
    print(f"{i+1}. {dwarf}")
    

def summon_captain_planet(list):
  return [f"{planeteer.capitalize()}!" for planeteer in list]

def long_planeteer_calls(list):
  words = []
  for word in list:
    if len(word) > 4:
      words.append(word)
  return len(words) > 0

def find_the_cheese(list):
  cheeses = ["cheddar", "gouda", "camembert"]
  for word in list:
    if word in cheeses:
      return word
  
