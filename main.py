from repository import MemoryRepository
from service import LibraryService
MENU = """
1. зарегистрировать читателя
2. показать читателей
3. добавить книгу
4. показать все книги
5. выдать книгу читателю
6. вернуть книгу в библиотеку
0. выйти из программы
"""
def read_id(prompt):
    try:
        item_id = int(input(prompt))
    except ValueError:
        raise ValueError("id должен быть целым числом") from None
    if item_id < 1:
        raise ValueError("id должен быть больше нуля")
    return item_id
def main():
    service = LibraryService(MemoryRepository(), MemoryRepository())
    while True:
        try:
            print(MENU)
            choice = input("выберите действие: ").strip()
            if choice == "0":
                print("программа завершена")
                break
            elif choice == "1":
                name = input("имя читателя: ")
                reader = service.register_reader(name)
                print(f"читатель зарегистрирован, id: {reader.id}")
            elif choice == "2":
                readers = service.get_readers()
                if not readers:
                    print("читателей пока нет")
                for r in readers:
                    print(f"{r.id}. {r.name} (книг на руках: {len(r.borrowed_book_ids)})")
            elif choice == "3":
                title = input("название книги: ")
                author = input("автор: ")
                year = int(input("год издания: "))
                book = service.add_book(title, author, year)
                print(f"книга добавлена, id: {book.id}")
            elif choice == "4":
                books = service.get_books()
                if not books:
                    print("книг пока нет")
                for b in books:
                    status = "доступна" if b.is_available else "выдана"
                    print(f"{b.id}. «{b.title}» — {b.author}({b.year}г.) ({status})")
            elif choice == "5":
                book_id = read_id("id книги: ")
                reader_id = read_id("id читателя: ")
                service.give_book(book_id, reader_id)
                print("книга успешно выдана")
            elif choice == "6":
                book_id = read_id("id книги: ")
                reader_id = read_id("id читателя: ")
                service.return_book(book_id, reader_id)
                print("книга возвращена в библиотеку")
            else:
                print("такого действия нет, выберите пункт меню")
        except (ValueError, TypeError) as error:
            print(f"ошибка: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nпрограмма завершена")
            break
if __name__ == "__main__":
    main()