'''
    student system
'''

from c4_1_source import students

class NotArgError(Exception):
    def __init__(self, message):
        self.message = message


class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def get_user_by_id(self, student_id):
        return self.students.get(student_id)    # students is dict, get func is return value

    def get_all_students(self):
        for id_, value in self.students.items():
            print('student number：{0}，name：{1}，age：{2}，gender：{3}，class：{4}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students

    def add_students(self, **kw):
        try:
            self.check_user_info(**kw)
        except Exception as e:
            raise e

        self.__add(**kw)

    def adds(self, new_students):
        for student in new_students:
            try:
                self.check_user_info(**student)
            except Exception as e:
                print(e, student.get('name'))
                continue

            self.__add(**student)

    def __add(self, **kw):
        new_id = max(self.students) + 1
        self.students[new_id] = kw


    def delete_student(self, student_id):
        if student_id not in self.students:
            print('{0} is not existing'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('student number is{0}，student {1} has been deleted!'.format(student_id, user_info))

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print('{0} is not existing'.format(id_))
                continue
            user_info = self.students.pop(id_)['name']
            print('student number is {0}，student {1} has been deleted!'.format(id_, user_info))


    def update_student(self, student_id, **kw):
        if student_id not in self.students:
            print('this student number is not existing')
            return

        try:
            self.check_user_info(**kw)
        except Exception as e:
            raise e

        self.students[student_id] = kw
        print('student info has been updated successfully!')

    def updates(self, update_students):
        for student in update_students:
            try:
                id_ = list(student.keys())[0]
            except Exception as e:
                print(e)
                continue
            if id_ not in self.students:
                print('this student number {0} is not existing'.format(id_))
                continue

            user_info = student[id_]

            try:
                self.check_user_info(**user_info)
            except Exception as e:
                print(e)
                continue

            self.students[id_] = user_info
        print('all info updated successfully!')


    def search_users(self, **kw):
        assert len(kw) == 1, 'should only have 1 key in a search '

        values = list(self.students.values())
        key = None
        value = None
        result = []

        if 'name' in kw:
            key = 'name'
            value = kw[key]
        elif 'sex' in kw:
            key = 'sex'
            value = kw[key]
        elif 'age' in kw:
            key = 'age'
            value = kw[key]
        elif 'class_number' in kw:
            key = 'class_number'
            value = kw[key]
        else:
            raise NotArgError('search no found!!!')

        for user in values:
            if value in user[key]:
                result.append(user)

        return result

    def check_user_info(self, **kw):
        assert len(kw) == 4, 'should have 4 values'


        if 'name' not in kw:
            raise NotArgError('student name no found!!!')
        if 'sex' not in kw:
            raise NotArgError('student sex no found!!!')
        if 'age' not in kw:
            raise NotArgError('student age no found!!!')
        if 'class_number' not in kw:
            raise NotArgError('student class number no found!!!')


        name_value = kw['name']
        sex_value = kw['sex']
        age_value = kw['age']
        class_number_value = kw['class_number']
        if not isinstance(name_value, str):
            raise TypeError('name should be string!!!')
        if not isinstance(age_value, int):
            raise TypeError('age should be Int')
        if not isinstance(sex_value, str):
            raise TypeError('sex should be string!!!')
        if not isinstance(class_number_value, str):
            raise TypeError('class number should be string!!!')


if __name__ == '__main__':
    student_info = StudentInfo(students)
    user = student_info.get_user_by_id(1)
    print(user)
    student_info.add_students(name='GGG', sex='female', age=18, class_number='801')
    student_info.get_all_students()

    users = [{'name': 'XXX', 'age': 80, 'class_number': '1501', 'sex': 'male'},
             {'name': 'YYY', 'age': 80, 'class_number': '1501', 'sex': 'female'}
             ]
    student_info.adds(users)
    student_info.get_all_students()
    print('**************')
    student_info.deletes([7,8])
    student_info.get_all_students()
    print('**************')
    student_info.updates([
        {1: {'name': 'XXX', 'age': 80, 'class_number': '1501', 'sex': 'male'}},
        {2: {'name': 'YYY', 'age': 80, 'class_number': '1501', 'sex': 'female'}}
    ])
    student_info.get_all_students()
    print('**************')
    result = student_info.search_users(class_number='5')
    print(result)