import sys, json

def move(command):
    record = { 'moves': [command] }
    print(json.dumps(record))
    sys.stdout.flush()

name = sys.argv[1]

for line in sys.stdin:
    state = json.loads(line)
    with open (name + ".txt", "a") as testfile:
        testfile.write(line)
    # find planet with most ships
    my_planets = [p for p in state['planets'] if p['owner'] == name]
    other_planets = [p for p in state['planets'] if p['owner'] != name]

    if not my_planets or not other_planets:
        move(None)
    else:
        planet = max(my_planets, key=lambda p: p['ship_count'])
        dest = min(other_planets, key=lambda p: p['ship_count'])
        move({
            'origin': planet['name'],
            'destination': dest['name'],
            'ship_count': planet['ship_count'] - 2
        })
