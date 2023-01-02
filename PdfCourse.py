from Course import Course


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print('Number of pages : ', self.pages)


