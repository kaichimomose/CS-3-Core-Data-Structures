#!python

from _set import Set
import unittest


class SetTest(unittest.TestCase):
    def test_init(self):
        st = Set()
        assert st.list == []
        assert st.size == 0

    def test_init_with_list(self):
        st = Set(["A", "B", "C"])
        assert st.list == ["A", "B", "C"]
        assert st.size == 3

    def test_contains(self):
        st = Set()
        st.add("A")
        assert st.contains("A") is True
        st.add("B")
        assert st.contains("B") is True
        st.add("C")
        assert st.contains("C") is True
        st.remove("C")
        assert st.contains("C") is False
        st.remove("B")
        assert st.contains("B") is False
        st.remove("A")
        assert st.contains("A") is False

    def test_add(self):
        st = Set()
        st.add("A")
        assert st.size == 1
        st.add("B")
        assert st.size == 2
        st.add("C")
        assert st.size == 3
        with self.assertRaises(ValueError):
            st.add("A")

    def test_remove(self):
        st = Set()
        st.add("A")
        assert st.size == 1
        st.add("B")
        assert st.size == 2
        st.add("C")
        assert st.size == 3
        st.remove("C")
        assert st.size == 2
        st.remove("B")
        assert st.size == 1
        st.remove("A")
        assert st.size == 0
        with self.assertRaises(ValueError):
            st.remove("A")

    def test_union_with_other_set_some_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B", "D", "E"])
        union_set = st.union(other_st)
        self.assertCountEqual(union_set.list, ["A", "B", "C", "D", "E"])  # Ignore item order

    def test_union_with_other_set_no_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["D", "E", "F", "G"])
        union_set = st.union(other_st)
        self.assertCountEqual(union_set.list, ["A", "B", "C", "D", "E", "F", "G"])  # Ignore item order

    def test_intersection_with_other_set_some_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B", "D", "E"])
        union_set = st.intersection(other_st)
        self.assertCountEqual(union_set.list, ["A", "B"])  # Ignore item order

    def test_intersection_with_other_set_no_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["D", "E", "F", "G"])
        union_set = st.intersection(other_st)
        self.assertCountEqual(union_set.list, [])  # Ignore item order

    def test_difference_with_other_set_some_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B", "D", "E"])
        union_set = st.difference(other_st)
        self.assertCountEqual(union_set.list, ["C", "D", "E"])  # Ignore item order

    def test_difference_with_other_set_no_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["D", "E", "F", "G"])
        union_set = st.difference(other_st)
        self.assertCountEqual(union_set.list, ["A", "B", "C", "D", "E", "F", "G"])  # Ignore item order

    def test_is_subset(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B"])
        assert st.is_subset(other_st) is True

    def test_is_subset_with_other_set_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B", "C"])
        assert st.is_subset(other_st) is True

    def test_is_subset_with_other_set_some_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["A", "B", "D", "E"])
        assert st.is_subset(other_st) is False

    def test_is_subset_with_other_set_no_same_elements(self):
        st = Set(["A", "B", "C"])
        other_st = Set(["D", "E", "F", "G"])
        assert st.is_subset(other_st) is False

if __name__ == '__main__':
    unittest.main()
