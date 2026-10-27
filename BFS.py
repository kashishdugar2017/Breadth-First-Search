from collections import deque
graph = {
    "ME":['Agastya', 'Maryam', 'Rumi', 'Neelu'],
    "Agastya":['Maryam', 'Rumi', 'Neelu', 'Noah'],
    "Maryam":[],
    "Noah":[],
    "Rumi":['Neelu'],
    "Neelu":['Rumi']
         }

def is_seller(name):
    if name == 'Noah':
        return True
    elif name == 'Rumi':
        return True
    else:
        return False

def search():
    search_queue = deque()
    search_queue += graph["ME"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(person, "is a smoothie bowl seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

