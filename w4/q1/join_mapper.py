#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    # Skip headers
    if line.startswith("StudentID") or line.startswith("CourseID"):
        continue

    # Split by comma
    fields = line.split(",")

    if len(fields) != 3:
        continue

    first = fields[0]

    # Students file (S101 etc)
    if first.startswith("S"):
        student_id, name, course_id = fields
        print(f"{course_id}\tS,{student_id},{name}")

    # Courses file (C201 etc)
    elif first.startswith("C"):
        course_id, course_name, sem = fields
        print(f"{course_id}\tC,{course_name},{sem}")
