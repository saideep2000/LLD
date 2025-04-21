from library_management_system import LibraryManagementSystem
from member import Member
from book import Book


class LibraryManagementSystemDemo:
    def run():
        lms = LibraryManagementSystem.get_instance()

        new_book = Book("123", "MyFirstBook", "Saideep", 2025)

        new_member = Member("Saideep", 100, "Boston")

        lms.add_book(new_book)

        lms.register_a_member(new_member)

        print(lms.borrow_book(100, "123"))



        
if __name__ == "__main__":
    LibraryManagementSystemDemo.run()


# python3 4.Examples/2.LibraryManagementSystem/library_management_system_demo.py