'''
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
'''

def getCourseOrder(courses: dict):
    def rGetCourseOrder(remaining_courses, completed, course_order):
        # No courses left, we are done. Return the course_order.
        if not remaining_courses:
            return course_order

        # Find courses where all prerequisites are in completed.
        newly_completed = set()
        for course, prereq_list in remaining_courses.items():
            meets_prereqs = True
            for prereq in prereq_list:
                if prereq not in completed:
                    meets_prereqs = False
                    break
            # Add to newly_completed if prerequesites are met.
            if meets_prereqs:
                newly_completed.add(course)

        # Case where no new courses were completed, so there is no ordering path.
        if not newly_completed:
            return None

        # Add newly_completed courses to the course_order, and remove it from remaining_courses
        for course in newly_completed:
            course_order.append(course)
            del remaining_courses[course]

        # Recur with current parameters.
        return rGetCourseOrder(remaining_courses, completed.union(newly_completed), course_order)

    # OPTION: Import and use copy.deepcopy() here if you don't want to modify the original parameter.

    return rGetCourseOrder(courses, set(), [])

course_list = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}

print(getCourseOrder(course_list))

invalid_course_list = {
    'CSC400': ['CSC300'],
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': [],
    'CSC100': ['CSC400']
}

print(getCourseOrder(invalid_course_list))