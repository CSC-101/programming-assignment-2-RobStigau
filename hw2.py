import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1 : data.Point, point2 : data.Point):
    if point1.x > point2.x:
        top_left_x = point1.x
        bottom_right_x = point2.x
    else:
        top_left_x = point2.x
        bottom_right_x = point1.x
    if point1.y > point2.y:
        top_left_y = point1.y
        bottom_right_y = point2.y
    else:
        top_left_y = point2.y
        bottom_right_y = point1.y
    top_point_left = data.Point(top_left_x, top_left_y)
    bottom_point_right = data.Point(bottom_right_x, bottom_right_y)
    new_rectangle = data.Rectangle(top_point_left, bottom_point_right)
    return new_rectangle

# Part 2
def shorter_duration_than(duration1 : data.Duration, duration2 : data.Duration):
    duration1_seconds_total = ((duration1.minutes*60) + duration1.seconds)
    duration2_seconds_total = ((duration2.minutes*60) + duration2.seconds)
    if duration1_seconds_total < duration2_seconds_total:
        return True
    else:
        return False

# Part 3
def song_shorter_than(song_list : list[data.Song], duration1 : data.Duration):
    new_song_list = []
    for song in song_list:
        if shorter_duration_than(duration1, song.duration):
            new_song_list.append(song)
        else:
            continue
    return new_song_list

# Part 4
def running_time(song_list : list[data.Song], int_list : list[int]):
    total_duration = 0
    currentm = 0
    currents = 0
    for item in int_list:
        if item >= 0 and item < len(song_list):
            song = song_list[item]
            currentm += song.duration.minutes
            currents += song.duration.seconds
            total_duration = data.Duration(currentm, currents)
        else:
            continue
    currentt = currents // 60
    currents = currents % 60
    currentm += currentt
    total_duration = data.Duration(currentm, currents)
    return total_duration





# Part 5
def validate_route(city_list : list[list[str]], city_names : list[str]) -> bool:
    val = 0
    for cities in city_list:
        if city_names == cities:
            val += 1
            return True
        else:
            continue
    if len(city_names) == 1:
        return True
    if val == 0:
        return False

# Part 6
def longest_repetition(nums : list[int]):
    if len(nums) < 1:
        return None
    max_count = 1
    max_count_index = 0
    current_count = 1
    current_index = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_count_index = current_index
            current_count = 1
            current_index = i + 1
    if current_count > max_count:
        max_count_index = current_index
    return max_count_index
