#!/usr/bin/python3

# Дана строка и набор букв.
# В заданной строке найти минимальную по длине подстроку, содержащую все буквы из указанного набора.
# Регистр имеет значение. Буквы в наборе не повторяются.
# Сложность решения O(n)


class HashDeque:
    class Element:
        def __init__(self, key, value, prev_element=None, next_element=None):
            self.key = key
            self.value = value
            self.prev = prev_element
            self.next = next_element

    def __init__(self):
        self.dict = {}
        self.first_key = None
        self.last_key = None

    def add(self, key, val):
        if len(self.dict) == 0:
            new_el = self.Element(key, val)
            self.dict[key] = new_el
            self.last_key = self.first_key = key
        elif key not in self.dict:
            last_el = self.dict[self.last_key]
            new_el = self.Element(key=key, value=val, prev_element=last_el)
            last_el.next = new_el
            self.dict[key] = new_el
            self.last_key = key
        else:
            self.delete(key)
            self.add(key, val)

    def delete(self, key):
        el = self.dict[key]
        if el.prev is not None:
            el.prev.next = el.next
        if el.next is not None:
            el.next.prev = el.prev
        if key == self.first_key:
            self.first_key = None if el.next is None else el.next.key
        if key == self.last_key:
            self.last_key = None if el.prev is None else el.prev.key

        del self.dict[key]

    def get_first_value(self):
        if self.first_key is not None:
            return self.dict[self.first_key].value

    def get_last_value(self):
        if self.last_key is not None:
            return self.dict[self.last_key].value


def get_smallest(string, letters):
    hash_deque = HashDeque()
    min_len = float("+inf")
    segments = []
    for i in range(len(string)):
        char = string[i]
        if char in letters:
            hash_deque.add(char, i)
            if len(hash_deque.dict) == len(letters):
                first_pos = hash_deque.get_first_value()
                last_pos = hash_deque.get_last_value()
                segment = (first_pos, last_pos)
                length = last_pos - first_pos
                if length < min_len:
                    min_len = length
                    segments = [segment]
                elif length == min_len:
                    segments.append(segment)
    return segments

if __name__ == "__main__":
    result = get_smallest(
        string="aanhubcpbcyyyaaab",
        letters={"a", "b", "c"}
    )
    for segment in result:
        print(segment)
