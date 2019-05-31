#!/bin/env python3

import classroom


classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
print(repr(classroom_016.number))
print(repr(classroom_016.capacity))
print(repr(classroom_016.equipment))
print(classroom_016)
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_016.is_larger(classroom_007)
classroom_016.equipment_differences(classroom_007)
