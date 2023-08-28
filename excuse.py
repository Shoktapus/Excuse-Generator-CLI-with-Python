import random


excuse_starters =[
    "I'm sorry but",
    "Unfortunately",
    "I regret to inform you that",
    "Due to unforseen circumstances"
]

excuse_reasons = [
    "my dog ate my homework",
    "I had a sudden heart attack",
    "I couldn't log in cuz technology",
    "there was heavy traffic"
]

excuse_endings = [
    "so now I am behind af.",
    "so instead of bein one hunnit I'm just one.",
    "causing me to doo doo on the due da.",
    "which led to the crap in my dungaries."
]

def generate_excuse():
    #Generate the random excuse
    random_starters = random.choice(excuse_starters)
    random_reasons = random.choice(excuse_reasons)
    random_endings = random.choice(excuse_endings)

    #Concatenate the parts to form the final excuse
    final_excuse = random_starters + " " + random_reasons + " " + random_endings
    return final_excuse

def generate_excuse():
    excuse_parts = []
    excuse_parts.append(random.choice(excuse_starters))
    excuse_parts.append(random.choice(excuse_reasons))
    excuse_parts.append(random.choice(excuse_endings))
    return " ".join(excuse_parts)


#User input for customization 
#int turns the input string into a numerical value
num_excuse = int(input("Enter the number of excusees to generate:" ))

#Generate excuses in bulk
#the underscore _ in the for loop is used to repeat the process instead of
#naming a variable
print("Generated Excuses: ")
for _ in range(num_excuse):
    excuse = generate_excuse();
    print(excuse)
    print("-" * 100) #seperator for better readability 


#Print the excuse
#print("Generating Excuse")
#print(final_excuse)