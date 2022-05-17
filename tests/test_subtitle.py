"""
$ python3 -m unittest tests/test_subtitle.py 
"""


class TestSubtitle(unittest.TestCase):
    path = None
    file_name = None
    testing = None

    def setUp(self):
        self.path = "/home/user/testpath/"
        self.testing = True

    def test_set_new_name_espanol_espana_ok(self):
        self.file_name = "Subtitle 0x00 (Español (España)).srt"
        expected = "Subtitle 0x00 VOSE.srt"
        sub = Subtitle(self.path, self.file_name, self.testing)
        self.assertEqual(sub.new_file_name, expected)

    def test_set_new_name_espanol_latinoamerica_ok(self):
        self.file_name = "Subtitle 0x00 (Español (Latinoamérica)).srt"
        expected = "Subtitle 0x00 VOSE.srt"
        sub = Subtitle(self.path, self.file_name, self.testing)
        self.assertEqual(sub.new_file_name, expected)

    def test_set_new_name_fail(self):
        self.file_name = "Subtitle 0x00.srt"
        Subtitle(self.path, self.file_name, self.testing)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
