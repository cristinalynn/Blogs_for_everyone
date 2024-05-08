from helpers import Library

# Main Menu
def main_menu():
    library = Library()

    while True:
        print("\nWelcome To Blogs for Everyone!")
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
        print("\n---------------------------------")
        print("\nAuthor Management")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. List Authors")
        print("4. List Author Information")
        print("5. Go Back")

        choice = input("Select an option: ")
        # CREATE AUTHOR
        if choice == '1':
            print("\n---------------------------------")
            name = input("Enter author name: ")
            library.create_author(name)
            print("Author created!")
        # DELETE AUTHOR
        elif choice == '2':
            print("\n---------------------------------")
            print("Select an author to delete:")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}.{author.name}")
            author_index = int(input("Enter author number to delete: ")) - 1
            if 0 <= author_index < len(authors):
                library.delete_author(authors[author_index].id)
                print("Author deleted!")
            else:
                print("invalid author number!")
        # LIST ALL AUTHORS    
        elif choice == '3':
            print("\n---------------------------------")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}.{author.name}")
        #VIEW AUTHOR DETAILS - CHOOSE FROM LIST
        elif choice == '4':
            print("\n---------------------------------")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author.name}")
            author_index = int(input("Enter author number to view details: "))
            if 1 <= author_index <= len(authors):
                author = authors[author_index - 1]
                print("\n---------------------------------")
                print(f"Author Details:")
                print(f"Name: {author.name}")
                print("Blogs Written:")
                for i, blog in enumerate(author.blogs, 1):
                    print(f"{i}. Title: {blog.title}")
            else:
                print("Invalid author number.")
        # RETURN TO MAIN MENU
        elif choice == '5':
            print("\n---------------------------------")
            break #Return to main menu
        else:
            print("Please select a valid option")

# Blog Menu
def blog_menu(library):
    while True:
        print("\n---------------------------------")
        print("\nBlog Management")
        print("1. Create Blog")
        print("2. Delete Blog")
        print("3. List Blogs")
        print("4. Go Back")

        choice = input("Select an option: ")
        # CREATE BLOG
        if choice == '1':
            print("\n---------------------------------")
            title = input("Enter blog title: ")
            author_name = input("Enter author name: ")
            existing_author = library.find_author_by_name(author_name)
            if existing_author:
                author_id = existing_author.id
            else:
                author_id = library.create_author(author_name).id
                print("Author created")
            library.create_blog(title, author_id)
            print("Blog created!")
        # DELETE BLOG
        elif choice == '2':
            print("\n---------------------------------")
            blogs = library.get_all_blogs()
            print("\nSelect Blog to Delete:")
            for i, blog in enumerate(blogs, 1):
                if blog.author:
                    print(f"{i}. {blog.title} by {blog.author.name}")
                else:
                    print(f"{i}. {blog.title} by Unknown")
            blog_choice = input("Enter blog number to delete: ")
            try:
                blog_index = int(blog_choice) - 1
                if 0 <= blog_index < len(blogs):
                    library.delete_blog(blogs[blog_index].id)
                    print("Blog deleted!")
                else:
                    print("Invalid blog number.")
            except ValueError:
                print("Please enter a valid number.")
        # LIST ALL BLOGS
        elif choice == '3':
            print("\n---------------------------------")
            blogs = library.get_all_blogs()
            for i, blog in enumerate(blogs, 1):
                if blog.author:
                    print(f"{i}. Title: {blog.title}\n  Author: {blog.author.name}\n ")
                else:
                    print(f"{i}. Title: {blog.title}\n  Author: Unknown\n ")
        # RETURN TO MAIN MENU
        elif choice == '4':
            print("\n---------------------------------")
            break #Return to main menu
        else:
            print("Please select a valid option")

# Reader Menu
def reader_menu(library):
    while True:
        print("\n---------------------------------")
        print("\nReader Management")
        print("1. Create Reader")
        print("2. Delete Reader")
        print("3. List Readers")
        print("4. Go Back")

        choice = input("Select an option: ")
        # CREATE READER
        if choice == '1':
            print("\n---------------------------------")
            name = input("Enter reader name: ")
            library.create_reader(name)
            print("Reader created!")
        # DELETE READER
        elif choice == '2':
            print("\n---------------------------------")
            print("Select a reader to delete:")
            readers = library.get_all_readers()
            for i, reader in enumerate(readers, 1):
                print(f"{i}. {reader.name}")
            reader_index = int(input("Enter reader number to delete: ")) - 1
            if 0 <= reader_index < len(readers):
                library.delete_reader(readers[reader_index].id)
                print("Reader deleted!")
            else:
                print("Invalid reader number!")
        # LIST READERS
        elif choice == '3':
            print("\n---------------------------------")
            readers = library.get_all_readers()
            for i, reader in enumerate(readers, 1):
                print(f"{i}. {reader.name}")
        # RETURN TO MAIN MENU
        elif choice == '4':
            print("\n---------------------------------")
            break #Return to main menu
        else:
            print("Please select a valid option")
        
            
if __name__ == '__main__':
    main_menu()

