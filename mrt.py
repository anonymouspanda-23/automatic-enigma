def find_stations_within_distance(mrt_map: list, orig: str, dist: int) -> list:
    orig_line_indexes = []
    orig_pos_indexes = []
    stations_within_dist = {}
    temp_dict = {}

    for idx, line in enumerate(mrt_map):
        if orig in line:
            orig_line_indexes.append(idx)
            orig_pos_indexes.append(line.index(orig))

    for stn_idx, line_idx in zip(orig_pos_indexes, orig_line_indexes):
        stations_in_line = mrt_map[line_idx]
        for i in range(max(stn_idx - dist, 0), stn_idx):
            stations_within_dist[stations_in_line[i]] = abs(stn_idx - i)
    
        for i in range(stn_idx + 1, min(len(stations_in_line), stn_idx + dist + 1)):
            stations_within_dist[stations_in_line[i]] = abs(stn_idx - i)
    
    # call func for instances where dist from orig to stn less than dist given by user
    for station in stations_within_dist.keys():
        if dist - stations_within_dist[station] > 0:
            temp_dict = temp_dict | find_stations_within_distance(mrt_map, station, dist - stations_within_dist[station])
    
    stations_within_dist = stations_within_dist | temp_dict
    if orig in stations_within_dist.keys():
        del stations_within_dist[orig]
    return stations_within_dist


if __name__ == '__main__':
    mrt_map = [ ['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'],
                ['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'],
                ['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng'] ]
    
    # ['Stevens', 'Newton']
    print(find_stations_within_distance(mrt_map, 'Botanic Gardens', 2))
    print('-' * 20)

    # ['Farrer Park', 'Newton', 'Rochor', 'Dhoby Ghaut']
    print(find_stations_within_distance(mrt_map, 'Little India', 1))
    print('-' * 20)

    # ['Little India', 'Farrer Park', 'Boon Keng', 'Rochor','Newton', 'Stevens', 'Novena']
    print(find_stations_within_distance(mrt_map, 'Dhoby Ghaut', 3))
    print('-' * 20)

    # ['Stevens', 'Botanic Gardens', 'Little India', 'Rocher', 'Dhoby Ghaut', 'Farrer Park', 'Novena', 'Toa Payoh']
    print(find_stations_within_distance(mrt_map, 'Newton', 2))
    print('-' * 20)


