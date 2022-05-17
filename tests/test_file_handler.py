"""
$ python3 -m unittest tests/test_file_handler.py 
"""


class TestFileHandler(unittest.TestCase):
    script_path = None
    subtitles = None
    test_empty_path = None
    test_files_path = None
    txts = None
    videos = None

    def setUp(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.test_files_path = os.path.join(self.script_path, "fakedFiles")
        self.test_empty_path = os.path.join(self.script_path, "emptyPath")
        self.videos = ["video1.mp4", "video2.avi", "video3.mkv"]
        self.subtitles = ["subtitle1.srt", "subtitle2.srt"]
        self.txts = ["txtfile.txt"]

    def test_is_video_ok(self):
        for f in self.videos:
            result = file_handler.is_video(f)
            self.assertTrue(result)

    def test_is_video_fail(self):
        for f in self.txts:
            result = file_handler.is_video(f)
            self.assertFalse(result)

    def test_is_subtitle_ok(self):
        for f in self.subtitles:
            result = file_handler.is_subtitle(f)
            self.assertTrue(result)

    def test_is_subtitle_fail(self):
        for f in self.txts:
            result = file_handler.is_subtitle(f)
            self.assertFalse(result)

    def test_get_videos(self):
        expected = ["video2.mkv", "video1.avi", "video2.mp4"]

        videos = file_handler.get_videos(self.test_files_path)

        self.assertEqual(expected, videos)

    def test_get_videos_empty(self):
        expected = []

        videos = file_handler.get_videos(self.test_empty_path)

        self.assertEqual(expected, videos)

    def test_get_subtitles(self):
        expected = ['subtitle1.srt', 'subtitle2.srt']
        subtitles = file_handler.get_subtitles(self.test_files_path)

        self.assertEqual(expected, subtitles)

    def test_get_subtitles_empty(self):
        expected = []

        subtitles = file_handler.get_subtitles(self.test_empty_path)

        self.assertEqual(expected, subtitles)

    def test_mv_ok(self):
        print("test_file_handler.test_mv_ok")
        orig = "/home/user/orig/file1.mp4"
        dest = "/home/user/dest/file1.mp4"
        testing = True

        file_handler.mv(orig, dest, testing)

        self.assertTrue(True)

    def test_mv_fail(self):
        print("test_file_handler.test_mv_fail")
        orig = "/home/user/orig/file1.mp4"
        dest = "/home/user/dest/file1.mp4"
        testing = False

        self.assertRaises(Exception, file_handler.mv(orig, dest, testing))


if __name__ == "__main__":
    unittest.main()
