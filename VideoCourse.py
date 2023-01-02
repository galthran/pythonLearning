from Course import Course


class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print('Video Length : ', self.length_video)
