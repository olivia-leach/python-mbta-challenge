# mbta challenge

red = ['south station', 'park st', 'kendall', 'central', 'harvard', 'porter', 'davis', 'alewife']
green = ['haymarket', 'government center', 'park st', 'bolyston', 'arlington', 'copley']
orange = ['north station', 'haymarket', 'park st', 'state', 'downtown crossing', 'chinatown', 'back bay', 'forest hills']

def mbta(start_line, start_station, end_line, end_station):
    """takes a starting line & station, ending line & station and returns the number of stops"""
    if start_line == end_line:
        if start_line == "red":
            print(abs(red.index(start_station) - red.index(end_station)))
        elif start_line == "green":
            print(abs(green.index(start_station) - green.index(end_station)))
        elif start_line == "orange":
            print(abs(orange.index(start_station) - orange.index(end_station)))
    else:
        if start_line == "red":
            start_stops = abs(red.index(start_station) - red.index('park st'))
        elif start_line == "green":
            start_stops = abs(green.index(start_station) - green.index('park st'))
        elif start_line == "orange":
            start_stops = abs(orange.index(start_station) - orange.index('park st'))

        if end_line == "red":
            end_stops = abs(red.index(end_station) - red.index('park st'))
        elif end_line == "green":
            end_stops = abs(green.index(end_station) - green.index('park st'))
        elif end_line == "orange":
            end_stops = abs(orange.index(end_station) - orange.index('park st'))

        print(start_stops + end_stops)

mbta("green", "bolyston", "red", "alewife")
