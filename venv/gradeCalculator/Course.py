class Course:
    """This class represents a course and holds info on the course name, students grade, semester it was taken, and the componenents of grading"""
    # class members
    courseName = None
    courseGrade = None
    courseSemester = None
    courseComponents = []

    #Constructor, each parameter will be required
    def __init__(self, name, grade, semester, components):
        self.courseName = name
        self.courseGrade = grade
        self.courseSemester = semester
        self.courseComponents = components

    #Setters and getters
    def setCourseName(self, name):
        self.courseName = name

    def getCourseName(self):
        return self.courseName

    def setCourseGrade(self, grade):
        self.courseGrade = grade

    def getCourseGrade(self):
        return self.courseGrade

    def setCourseSemester(self, semester):
        self.courseSemester = semester

    def getCourseSemester(self):
        return self.courseSemester

    def setCourseComponents(self, components):
        self.courseComponents = components

    def getCourseComponenets(self):
        return self.courseComponents