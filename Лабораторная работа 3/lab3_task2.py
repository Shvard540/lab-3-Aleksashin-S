def find_common_participants(gr1, gr2, arg=","):

    t1 = gr1.split(arg)
    t2 = gr2.split(arg)
    nt1 = set(t1)
    all = nt1.intersection(t2)
    all = list(all)
    all.sort()
    return all


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
