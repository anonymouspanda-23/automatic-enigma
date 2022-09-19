# Name:
# Email ID:

def trace_contacts(patient: str, history: list) -> list:
    infected_people = {
        patient: -7,
    }

    history.sort(key=lambda x: x[2])

    for history_info in history:
        p1 = history_info[0]
        p2 = history_info[1]
        day = history_info[2]

        if p1 in infected_people.keys() or p2 in infected_people.keys():
            if p1 in infected_people.keys():
                relative_infected_day = infected_people[p1]
                if relative_infected_day < day - 1:
                    infected_people[p2] = day
            else:
                relative_infected_day = infected_people[p2]
                if relative_infected_day < day - 1:
                    infected_people[p1] = day

        else:
            continue
    
    infected_people_list = [name for name in infected_people.keys()]
    infected_people_list.remove(patient)

    return infected_people_list