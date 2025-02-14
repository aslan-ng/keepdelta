"""
In this example, we will add delta management as __add__ and __sub__ methods to the class.
"""

import keepdelta as kd


class Profile:

    def __init__(self, name, age, is_student, grades, preferences, attributes, settings):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.grades = grades
        self.preferences = preferences
        self.attributes = attributes
        self.settings = settings

    def __sub__(self, other):
        return kd.create(self.__dict__, other.__dict__)

    def __add__(self, delta):
        return Profile(**kd.apply(self.__dict__, delta))


if __name__ == '__main__':
    profile_old = Profile(
        name='Alice',
        age=30,
        is_student=True,
        grades=[85.5, 90.0, 78],
        preferences=('chocolate', {'sports': {'football', 'tennis'}}),
        attributes=[{'id': 1, 'value': 'active'}, {'id': 2, 'value': 'inactive'}],
        settings={'dark_mode': True, 'font_size': 14, 'scale': 1.25},
    )
    profile_new = Profile(
        name='Alice',
        age=31,
        is_student=False,
        grades=[85.5, 90.0, 78],
        preferences=('coffee', {'sports': {'football', 'bodybuilding'}}),
        attributes=[{'id': 1, 'value': 'inactive'}, {'id': 2, 'value': 'inactive'}],
        settings={'dark_mode': True, 'font_size': 14, 'scale': 1.25}
    )
    delta = profile_old - profile_new  # Create delta
    profile_reconstructed = profile_old + delta  # Apply delta
    print('Reconstruction is successful:', profile_reconstructed.__dict__ == profile_new.__dict__)