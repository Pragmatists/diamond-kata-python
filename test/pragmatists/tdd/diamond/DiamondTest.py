import unittest
import operator


class Diamond(object):
    def print_up_to(self, limit):
        return reduce(
            operator.concat,
            (
                self.build_line(c, limit)
                for c in self.letters_up_to_and_back(limit))
            )

    def letters_up_to_and_back(self, limit):
        letters_from_a_to_limit = range(ord('A'), ord(limit))
        for o in letters_from_a_to_limit:
            yield chr(o)
        yield limit
        for o in reversed(letters_from_a_to_limit):
            yield chr(o)

    def build_line(self, current, limit):
        line = self.indent(current, limit)
        line += current
        line += self.seperator(current)
        if current > 'A':
            line += current
        line += "\n"
        return line

    def indent(self, current, limit):
        return self.spaces(ord(limit) - ord(current))

    def spaces(self, count):
        return " " * count

    def seperator(self, current):
        distance = ord(current) - ord('A')
        return self.spaces(distance * 2 - 1)


class DiamondTest(unittest.TestCase):
    def test_a_gives_single_line(self):
        self.assertEqual("A\n", Diamond().print_up_to('A'))

    def test_b_is_a_diamond(self):
        self.assertEqual(" A\n"
                         "B B\n"
                         " A\n", Diamond().print_up_to('B'))

    def test_c_is_a_bigger_diamond(self):
        self.assertEqual("  A\n"
                         " B B\n"
                         "C   C\n"
                         " B B\n"
                         "  A\n", Diamond().print_up_to('C'))

    def test_d_is_an_even_bigger_diamond(self):
        self.assertEqual("   A\n"
                         "  B B\n"
                         " C   C\n"
                         "D     D\n"
                         " C   C\n"
                         "  B B\n"
                         "   A\n", Diamond().print_up_to('D'))

if __name__ == '__main__':
    unittest.main()
