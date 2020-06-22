# python3
# ! Solved using the direct addressing scheme (not optimal in terms of memory) !
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


# ! Solved using the direct addressing scheme (not optimal in terms of memory) !
def process_queries(queries):
    result = []
    # phone numbers are 7-digit nums
    ph_book = [0]*int(1e7)
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            ph_book[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            ph_book[cur_query.number] = 0
        else:
            name = ph_book[cur_query.number]
            if name == 0:
                response = 'not found'
            else:
                response = name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

