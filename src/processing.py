
def filter_by_state(to_filter:list, state='EXECUTED'):
    only_states = []
    for element in to_filter:
        if state == element['state']:
            only_states.append(element)

    return only_states

def sort_by_date(to_sort:list, decreasing=True):
    to_sort.sort(key=lambda x: x['date'], reverse=decreasing)
    return to_sort
