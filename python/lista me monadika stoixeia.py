def list_set(li):
    # επιστρέφει τη λίστα χωρίς διπλά στοιχεία
    if not type(li) is list :
        return []
    li_new = []
    for i in li:
        if i not in li_new : li_new.append(i)
    return li_new

print(list_set([1,2,3,4,2,3,4,2,3,4]))