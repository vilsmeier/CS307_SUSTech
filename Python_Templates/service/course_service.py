from abc import ABC
from typing import List, Optional

from dto import (Course, CourseGrading, CourseSection, CourseSectionClass,
                 DayOfWeek, Prerequisite, Student)


class CourseService(ABC):

    """
        /**
     * Add one course according to following parameters.
     * If some of parameters are invalid, throw {@link cn.edu.sustech.cs307.exception.IntegrityViolationException}
     *
     * @param courseId represents the id of course. For example, CS307, CS309
     * @param courseName the name of course
     * @param credit the credit of course
     * @param classHour The total teaching hour that the course spends.
     * @param grading the grading type of course
     * @param coursePrerequisite The root node of prerequisite.{@link cn.edu.sustech.cs307.dto.prerequisite.Prerequisite}
     */
    """
    async def add_course(self, course_id: str, course_name: str, credit: int,
                         class_hour: int, grading: CourseGrading,
                         course_prerequisite: Optional[Prerequisite]):
        raise NotImplementedError



    """
        /**
     * Add one course section according to following parameters:
     * If some of parameters are invalid, throw {@link cn.edu.sustech.cs307.exception.IntegrityViolationException}
     *
     * @param courseId represents the id of course. For example, CS307, CS309
     * @param semesterId the id of semester
     * @param sectionName the name of section {@link cn.edu.sustech.cs307.dto.CourseSection}
     * @param totalCapacity the total capacity of section
     * @return the CourseSection id of new inserted line, if adding process is successful.
     */
    """
    async def add_course_section(self, course_id: str, semester_id: int,
                                 section_name: str, total_capacity: int
                                 ) -> int:
        raise NotImplementedError


    '''
    /**
     * Add one course section class according to following parameters:
     * If some of parameters are invalid, throw {@link cn.edu.sustech.cs307.exception.IntegrityViolationException}
     *
     * @param sectionId
     * @param instructorId
     * @param dayOfWeek
     * @param weekList
     * @param classStart
     * @param classEnd
     * @param location
     * @return the CourseSectionClass id of new inserted line.
     */'''
    async def add_course_section_class(self, section_id: int,
                                       instructor_id: int,
                                       day_of_week: DayOfWeek) -> int:
        raise NotImplementedError



    async def remove_course(self, course_id: str):
        raise NotImplementedError

    async def remove_course_section(self, section_id: int):
        raise NotImplementedError

    async def remove_course_section_class(self, class_id: int):
        raise NotImplementedError


    '''
        /**
     *
     * @param sectionId the id of {@code CourseSection}
     * @return
     */
     '''
    async def get_course_sections_in_semester(self, course_id: str,
                                              semester_id: int
                                              ) -> List[CourseSection]:
        raise NotImplementedError

    async def get_course_by_section(self, section_id: int) -> Course:
        raise NotImplementedError

    async def get_course_section_classes(self, section_id: int) \
            -> List[CourseSectionClass]:
        raise NotImplementedError

    async def get_course_section_by_class(self, class_id: int) \
            -> CourseSection:
        raise NotImplementedError

    async def get_enrolled_students_in_semester(self, course_id: str,
                                                semester_id: int
                                                ) -> List[Student]:
        raise NotImplementedError
