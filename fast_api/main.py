from fastapi import FastAPI
import random

app = FastAPI()

# we will build two simple get endpoints 
# side_hastles
# mony_quots

side_hastles = [
    "Freelancing",
    "Dropshipping",
    "Stock Marketing",
    "online Earning",
    "Teaching",
    "study"
]

money_quotes = [
    "the way to get started is to quit talking and begin doing,",
    "formal education will make you a living; self-education will make you a fortune",
    "if you don't find a way to make mony whilw yo sleeping yo will work untill you die",
    "money is the tarrible master but an excellent servent",
    "Opportuniteis don't happen. You craete them"
]


@app.get("/side_hustles")
def get_side_hustles():
   
    """Returns as random side sustles idea"""
    return {"side_hustle" : random.choice(side_hastles)}

@app.get("/mony_quotes")
def get_mony_quotes():
   
    return {"mony_quote":random.choice(money_quotes)}