from configparser import ConfigParser
from pathlib import Path
import psycopg2

from service import *


class ServiceFactory:
    def __init__(self):
        config = ConfigParser()
        config.read(Path(__file__).parent / 'config.ini')
        self.connect_to_postgresql = psycopg2.connect(database = config.get('database','database'),user = config.get('database','username'),password = config.get('database','password'),host = config.get('database','host'),port = config.get('database','port'))
        

    def create_course_service(self) -> CourseService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_department_service(self) -> DepartmentService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_instructor_service(self) -> InstructorService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_major_service(self) -> MajorService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_semester_service(self) -> SemesterService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_student_service(self) -> StudentService:
        # TODO: return an instance of your implementation
        raise NotImplementedError

    def create_user_service(self) -> UserService:
        # TODO: return an instance of your implementation
        raise NotImplementedError
