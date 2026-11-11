import unittest
from repository import MemoryRepository
from service import LibraryService
class LibraryServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = LibraryService(MemoryRepository(), MemoryRepository())
        self.book = self.service.add_book("Книга", "Автор", 2026)
        self.reader = self.service.register_reader("Читатель")
        self.other = self.service.register_reader("Другой читатель")
    def test_registered_reader_has_empty_book_list(self):
        self.assertEqual(self.reader.borrowed_book_ids, [])
    def test_give_and_return_book(self):
        self.service.give_book(self.book.id, self.reader.id)
        self.assertFalse(self.book.is_available)
        self.assertEqual(self.reader.borrowed_book_ids, [self.book.id])
        self.service.return_book(self.book.id, self.reader.id)
        self.assertTrue(self.book.is_available)
        self.assertEqual(self.reader.borrowed_book_ids, [])
    def test_wrong_reader_cannot_return_book(self):
        self.service.give_book(self.book.id, self.reader.id)
        with self.assertRaises(ValueError):
            self.service.return_book(self.book.id, self.other.id)
        self.assertFalse(self.book.is_available)
        self.assertEqual(self.reader.borrowed_book_ids, [self.book.id])
        self.assertEqual(self.other.borrowed_book_ids, [])
    def test_second_issue_keeps_first_reader(self):
        self.service.give_book(self.book.id, self.reader.id)
        with self.assertRaises(ValueError):
            self.service.give_book(self.book.id, self.other.id)
        self.assertEqual(self.reader.borrowed_book_ids, [self.book.id])
        self.assertEqual(self.other.borrowed_book_ids, [])
    def test_missing_reader_keeps_book_available(self):
        with self.assertRaises(ValueError):
            self.service.give_book(self.book.id, 999)
        self.assertTrue(self.book.is_available)
        self.assertEqual(self.reader.borrowed_book_ids, [])
if __name__ == "__main__":
    unittest.main()