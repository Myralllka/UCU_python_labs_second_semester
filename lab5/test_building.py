#!/bin/env python3

import building
import classroom
import doctest


classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = building.AcademicBuilding('Kozelnytska st. 2a', classrooms)
print(repr(building.address))
for room in building.classrooms:
    print(room)
print(repr(building.total_equipment()))
print(building)
