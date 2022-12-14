import bico_scheduling as bs


def test():
    d = bs.bmc.get_data_list_of_dicts("brynmawr/data/Fall2007.csv")
    bs.bmc.write_constraints_to_file(d, "test/bconstraints.txt")
    bs.bmc.write_prefs_to_file(d, "test/bprefs.txt")

    d = bs.hav.get_data_list_of_dicts(
        "haverford\haverfordEnrollmentDataS14.csv")
    bs.hav.write_constraints_to_file(d, "test/hconstraints.txt")
    bs.hav.write_prefs_to_file(d, "test/hprefs.txt")

    # students, classes, rooms, times, profs = bs.prep_data(
    #     "test/bconstraints.txt", "test/bprefs.txt", "test/hconstraints.txt", "test/hprefs.txt")

    students, classes, rooms, times, profs = bs.prep_data(
        "test/hconstraints.txt", "test/hprefs.txt")

    # students, classes, rooms, times, profs = bs.prep_data(
    #     "test/bconstraints.txt", "test/bprefs.txt")

    class_p = bs.class_priority(classes)
    student_p = bs.student_priority(students)
    student_athletes = bs.student_athletes(students, .386)

    custom_times = bs.custom_times(8, 16, 1)
    schedule, reg_students = bs.make_schedule(
        students, classes, rooms, custom_times, profs,
        student_p, class_p)

    print("schedule rating:", bs.schedule_rating(schedule, students))
    bs.schedule_to_file(schedule, "test/schedule.txt")


if __name__ == "__main__":
    test()
