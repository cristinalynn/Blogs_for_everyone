from helpers import Library

# Main Menu
def main_menu():
    library = Library()

    while True:
        print("\nWelcome To Blog for Everyone!")
        print("1. Manage Authors")
        print("2. Manage Blogs")
        print("3. Manage Readers")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            author_menu(library)
        elif choice == '2':
            blog_menu(library)
        elif choice == '3':
            reader_menu(library)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option!")

# Author Menu
def author_menu(library):
    while True:
        print("\nAuthor Management")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. List Authors")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            library.create_author(name)
            print("Author created!")
        elif choice == '2':
            author_id = int(input("Enter author ID to delete: "))
            library.delete_author(author_id)
            print("Author deleted!")
        elif choice == '3':
            authors = library.get_all_authors()
            for author in authors:
                print(f"Author ID: {author.id}, Name: {author.name}")
        elif choice == '4':
            break
        else:
            print("Please select a valid option.")

# Blog Menu
def blog_menu(library):
    while True:
        print("\nBlog Management")
        print("1. Create Blog")
        print("2. Delete Blog")
        print("3. List Blogs")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter blog title: ")
            author_name = input("Enter author name: ")
            author = library.find_author_by_name(author_name)
            if author:
                library.create_book(title, author.id)
                print("Blog created!")
            else:
                print("Author not found. Please create the author first.")
        elif choice == '2':
            blog_id = int(input("Enter blog ID to delete: "))
            library.delete_blog(blog_id)
            print("Blog deleted!")
        elif choice == '3':
            blogs = library.get_all_blogs()
            for blog in blogs:
                print(f"Blog ID: {blog.id}, Title: {blog.title}, Author: {blog.author.name}")
        elif choice == '4':
            break
        else:
            print("Please select a valid option.")

# Reader Menu
def reader_menu(library):
    while True:
        print("\nReader Management")
        print("1. Create Reader")
        print("2. Delete Reader")
        print("3. List Readers")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter reader name: ")
            library.create_reader(name)
            print("Reader created!")
        elif choice == '2':
            reader_id = int(input("Enter reader ID to delete: "))
            library.delete_reader(reader_id)
            print("Reader deleted!")
        elif choice == '3':
            readers = library.get_all_readers()
            for reader in readers:
                print(f"Reader ID: {reader.id}, Name: {reader.name}")
        elif choice == '4':
            break
        else:
            print("Please select a valid option.")
            
if __name__ == '__main__':
    main_menu()

