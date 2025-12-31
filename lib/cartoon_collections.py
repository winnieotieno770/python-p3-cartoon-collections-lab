def roll_call_dwarves(dwarfs):
    for i,dwarf in enumerate(dwarfs):
        print(f"{i+1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
   p= [f"{planet[0].upper()}{''.join(planet[1:])}!" for planet in planeteer_calls]
   return p

   
def long_planeteer_calls(words):
    long = 4
    for word in words:
        if len(word) > long:
            return True
    return False
        
def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    return  next((item  for item in items  if item in cheeses), None )
