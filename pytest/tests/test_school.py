import pytest
from src.school import Classroom, Student, Teacher, ToomanyStudentsError

# Fixtures
@pytest.fixture
def harry_potter_classroom():
    """Fixture to provide a Hogwarts-themed classroom."""
    teacher = Teacher(name="Minerva McGonagall")
    students = [
        Student(name="Harry Potter"),
        Student(name="Hermione Granger"),
        Student(name="Ron Weasley"),
        Student(name="Neville Longbottom"),
        Student(name="Luna Lovegood"),
        Student(name="Ginny Weasley"),
    ]
    return Classroom(teacher=teacher, students=students, course_title="Defense Against the Dark Arts")

@pytest.fixture
def student_draco():
    """Fixture for Draco Malfoy."""
    return Student(name="Draco Malfoy")

# Parameterized Test Cases
@pytest.mark.parametrize("student_name", [
    "Fred Weasley", "George Weasley", "Cedric Diggory"
])
def test_add_student(harry_potter_classroom, student_name):
    """Test adding students to the classroom."""
    new_student = Student(name=student_name)
    harry_potter_classroom.add_student(new_student)
    assert new_student in harry_potter_classroom.students

def test_add_student_error(harry_potter_classroom):
    """Test that adding more than 10 students raises an error."""
    extra_students = [
        Student(name=f"Extra Student {i}") for i in range(5)
    ]
    for student in extra_students[:4]:  # Fill up to 10 students
        harry_potter_classroom.add_student(student)
    with pytest.raises(ToomanyStudentsError):
        harry_potter_classroom.add_student(extra_students[4])

def test_remove_student(harry_potter_classroom):
    """Test removing a student from the classroom."""
    harry_potter_classroom.remove_student("Harry Potter")
    assert all(student.name != "Harry Potter" for student in harry_potter_classroom.students)

def test_remove_non_existent_student(harry_potter_classroom):
    """Test removing a student who isn't in the classroom (no errors)."""
    harry_potter_classroom.remove_student("Draco Malfoy")
    assert len(harry_potter_classroom.students) == 6  # Original number of students

def test_change_teacher(harry_potter_classroom):
    """Test changing the teacher of the classroom."""
    new_teacher = Teacher(name="Remus Lupin")
    harry_potter_classroom.change_teacher(new_teacher)
    assert harry_potter_classroom.teacher.name == "Remus Lupin"

# Marker for edge cases
@pytest.mark.edge_case
def test_empty_classroom():
    """Test behavior with an empty classroom."""
    empty_classroom = Classroom(teacher=Teacher(name="Severus Snape"), students=[], course_title="Potions")
    assert len(empty_classroom.students) == 0
    empty_classroom.add_student(Student(name="Draco Malfoy"))
    assert len(empty_classroom.students) == 1
