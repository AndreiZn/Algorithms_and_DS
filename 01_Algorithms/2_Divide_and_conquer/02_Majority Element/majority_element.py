# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def fill_count_array(a):

    max_el = max(a)
    n_un_elements = max_el + 1
    count = [0 for _ in range(n_un_elements)]
    for i in range(len(a)):
        el = a[i]
        count[el] = count[el] + 1
    return count

def counting_sort(elements):

    max_el = max(elements)
    n_un_elements = max_el + 1
    count = fill_count_array(elements)

    pos = [0 for _ in range(n_un_elements)]
    pos[0] = 0
    for j in range(1, n_un_elements):
        pos[j] = pos[j - 1] + count[j - 1]
    # k will occupy range [pos[k]...pos[k+1]-1]

    sorted_array = [0 for _ in range(len(elements))]
    for i in range(len(elements)):
        sorted_array[pos[elements[i]]] = elements[i]
        pos[elements[i]] = pos[elements[i]] + 1

    return sorted_array

def majority_element(elements):
    assert len(elements) <= 10 ** 5
    #count = fill_count_array(elements)
    #n_el, maj_el_count = len(elements), max(count)
    n_el = len(elements)
    if n_el == 1:
        return elements[0]

    m = int(n_el / 2)
    m_l = majority_element(elements[:m])
    m_r = majority_element(elements[m:])

    m_l_count, m_r_count = sum([elements[i] == m_l for i in range(m)]), sum([elements[i] == m_r for i in range(m,n_el)])
    if m_l_count >= m_r_count:
        return m_l
    else:
        return m_r

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    m_el = majority_element(input_elements)
    if sum([input_elements[i] == m_el for i in range(len(input_elements))]) > len(input_elements) / 2:
        print(1)
    else:
        print(0)