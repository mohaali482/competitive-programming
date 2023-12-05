def find(key, dictionary):
    for k, v in dictionary.items():
        if v[0] <= key < v[1]:
            return k + key - v[0]
    
    return key

def solution():
    seeds = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}
    windows = {1:seed_to_soil, 2: soil_to_fertilizer, 3:fertilizer_to_water, 4:water_to_light, 5:light_to_temperature, 6:temperature_to_humidity, 7:humidity_to_location,}
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        counter = 1
        seeds = [int(i) for i in lines[0].split()[1:]]
        win = windows[counter]
        i = 3
        while i < len(lines):
            line = lines[i]
            if line == "":
                counter += 1
                win = windows[counter]
                i += 2
            else:
                x, st, en = map(int, line.split())
                win[x] = (st, st+en)
                i += 1
        
        min_location = float("inf")
        set_seeds = set()
        for i in range(0, len(seeds), 2):
            seed_range = seeds[i], seeds[i] + seeds[i+1]
            for i in range(seed_range[0], seed_range[1]):
                if i not in set_seeds:
                    set_seeds.add(i)
        for seed in set_seeds:
            soil = find(seed, seed_to_soil)
            fertilizer = find(soil, soil_to_fertilizer)
            water = find(fertilizer, fertilizer_to_water)
            light = find(water, water_to_light)
            temperature = find(light, light_to_temperature)
            humidity = find(temperature, temperature_to_humidity)
            location = find(humidity, humidity_to_location)
            min_location = min(min_location, location)
        
        return min_location


    

            



if __name__ == "__main__":
        print(solution())