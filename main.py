class Book:
    """书籍类，包含书名、作者、ISBN属性，以及可借状态"""
    def __init__(self, title, author, isbn):
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # ISBN
        self.is_borrowed = False  # 借阅状态，默认未借出

    def check_available(self):
        """检查书籍是否可借"""
        return not self.is_borrowed

    def borrow(self):
        """借书操作：若可借则修改状态为已借出"""
        if self.check_available():
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """还书操作：修改状态为未借出"""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "可借" if self.check_available() else "已借出"
        return f"书名：{self.title}，作者：{self.author}，ISBN：{self.isbn}，状态：{status}"


class User:
    """用户类，包含姓名、借书卡号，以及借阅的书籍列表"""
    def __init__(self, name, card_id):
        self.name = name  # 姓名
        self.card_id = card_id  # 借书卡号
        self.borrowed_books = []  # 已借书籍列表

    def borrow_book(self, book):
        """用户借书：调用书籍的borrow方法，成功则加入已借列表"""
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name}成功借阅《{book.title}》")
            return True
        print(f"{self.name}借阅《{book.title}》失败，书籍已被借出")
        return False

    def return_book(self, book):
        """用户还书：调用书籍的return_book方法，成功则从已借列表移除"""
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name}成功归还《{book.title}》")
            return True
        print(f"{self.name}归还《{book.title}》失败，未借阅该书籍或书籍未被借出")
        return False

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"姓名：{self.name}，借书卡号：{self.card_id}，已借书籍：{borrowed_titles if borrowed_titles else '无'}"


# 测试代码
if __name__ == "__main__":
    # 创建书籍
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787115546920")

    # 创建用户
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")

    # 测试借书、还书和检查可借状态
    print(book1)
    user1.borrow_book(book1)
    print(book1)
    user2.borrow_book(book1)
    user1.return_book(book1)
    print(book1)
    user2.borrow_book(book1)

    # 打印用户信息
    print(user1)
    print(user2)
