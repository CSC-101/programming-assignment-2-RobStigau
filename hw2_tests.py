import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = data.Point(4, 3)
        point2 = data.Point(5, 2)
        result = hw2.create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(5, 3), data.Point(4, 2))
        self.assertEqual(result, expected)

    def test_create_rectangle2(self):
        point1 = data.Point(9, 4)
        point2 = data.Point(2, 5)
        result = hw2.create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(9, 5), data.Point(2, 4))
        self.assertEqual(result, expected)

    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = data.Duration(14, 34)
        duration2 = data.Duration(5, 12)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(result, expected)

    def test_shorter_duration_than2(self):
        duration1 = data.Duration(8, 34)
        duration2 = data.Duration(7, 95)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3
    def test_song_shorter_than1(self):
        song_lists = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30)),
                      data.Song('October', 'Broken Bells', data.Duration(3, 40)),
                      data.Song('Dust in the Wind', 'Kansas', data.Duration(3, 29)),
                      data.Song('Airplanes', 'Local Natives', data.Duration(3, 58))]
        duration1 = data.Duration(5, 20)
        result = hw2.song_shorter_than(song_lists, duration1)
        expected = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30))]
        self.assertEqual(result, expected)

    def test_song_shorter_than2(self):
        song_lists = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30)),
                      data.Song('October', 'Broken Bells', data.Duration(3, 40)),
                      data.Song('Dust in the Wind', 'Kansas', data.Duration(3, 29)),
                      data.Song('Airplanes', 'Local Natives', data.Duration(3, 58))]
        duration1 = data.Duration(3, 30)
        result = hw2.song_shorter_than(song_lists, duration1)
        expected = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30)),
                    data.Song('October', 'Broken Bells', data.Duration(3, 40)),
                    data.Song('Airplanes', 'Local Natives', data.Duration(3, 58))]
        self.assertEqual(result, expected)


    # Part 4
    def test_running_time1(self):
        song_lists = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30)),
                      data.Song('October', 'Broken Bells', data.Duration(3, 40)),
                      data.Song('Dust in the Wind', 'Kansas', data.Duration(3, 29)),
                      data.Song('Airplanes', 'Local Natives', data.Duration(3, 58))]
        int_lists = [0, 1, 3, 0]
        result = hw2.running_time(song_lists, int_lists)
        expected = data.Duration(18,38)
        self.assertEqual(result, expected)

    def test_running_time2(self):
        song_lists = [data.Song('June Hymn', 'Decemberists', data.Duration(5, 30)),
                      data.Song('October', 'Broken Bells', data.Duration(3, 40)),
                      data.Song('Dust in the Wind', 'Kansas', data.Duration(3, 29)),
                      data.Song('Airplanes', 'Local Natives', data.Duration(3, 58))]
        int_lists = [0, 1, 3, 3, 0, 2]
        result = hw2.running_time(song_lists, int_lists)
        expected = data.Duration(26,5)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'], ['atascadero', 'creston']]
        city_names = ['san luis obispo', 'pismo beach']
        result = hw2.validate_route(city_links, city_names)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'], ['atascadero', 'creston']]
        city_names = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(city_links, city_names)
        expected = False
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repetition1(self):
        num_list = [1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 1, 1]
        result = hw2.longest_repetition(num_list)
        expected = 3
        self.assertEqual(result, expected)

    def test_longest_repetition2(self):
        num_list = [1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4,1, 1]
        result = hw2.longest_repetition(num_list)
        expected = 7
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
