class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age,tracks,score):
        self.name=str(name)
        self.age=int(age)
        self.tracks= tracks
        self.score=float(score)

    print("These are details of a  new student")

    def change_name(self, new_name):
        self.name = new_name
        print("Name : ", self.name)
    def change_age(self, new_age):
        self.age = new_age
        print("Age : ", self.age)
    def add_track(self, add_track):
        self.tracks = add_track
        print("Tracks : ", self.tracks)
    def get_score(self, get_score):
        self.score = get_score
        print("Score : ", self.score)





Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(26.09)
