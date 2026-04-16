#!/usr/bin/env python3
import sys

current_course = None
students = []
course_info = None

for line in sys.stdin:
    line = line.strip()
    course_id, value = line.split("\t")
    tag, *data = value.split(",")

    if current_course != course_id:
        if current_course and course_info:
            for student in students:
                print(f"{student},{course_info[0]},{course_info[1]}")
        current_course = course_id
        students = []
        course_info = None

    if tag == "S":
        students.append(",".join(data))
    elif tag == "C":
        course_info = data

if course_info:
    for student in students:
        print(f"{student},{course_info[0]},{course_info[1]}")
