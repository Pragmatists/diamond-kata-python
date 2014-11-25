import unittest


class Diamond(object):
    def print_up_to(self, limit):
        return self.seq_for(limit)

    def letters_up_to(self, limit):
        for o in range(ord('A'), ord(limit) + 1):
            yield chr(o)
        for o in reversed(range(ord('A'), ord(limit))):
            yield chr(o)

    def indent(self, current, limit):
        if current != limit:
            return " "
        return ""

    def seq_for(self, limit):
        result = ""
        for current in self.letters_up_to(limit):
            result += self.indent(current, limit)
            result += current
            result += self.seperator(current)
            if current > 'A':
                result += current
            result += "\n"

        return result

    def seperator(self, current):
        if current != 'A':
            return " "
        return ""


class DiamondTest(unittest.TestCase):
    def test_a_gives_single_line(self):
        self.assertEqual("A\n", Diamond().print_up_to('A'))

    def test_b_is_a_diamond(self):
        self.assertEqual(" A\n"
                         "B B\n"
                         " A\n", Diamond().print_up_to('B'))


if __name__ == '__main__':
    unittest.main()
