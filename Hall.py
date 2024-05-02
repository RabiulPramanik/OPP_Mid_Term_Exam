# class Star_cinama:
#     hall_list = []
#     def __init__(self) -> None:
#         pass
#     def entry_hall(self,hall_obj):
#         Star_cinama.hall_list.append(hall_obj)
    
# class Hall(Star_cinama):
#     def __init__(self,rows,cols,hall_no) -> None:
#         self.rows = rows
#         self.cols = cols
#         self.hall_no = hall_no
#         self.seats = {}
#         self.show_list = []
#         self.entry_hall(self)
#     # def entry_show(self,id,movie_name,time):
#     #     self.show_list.append = f'{id} {movie_name} {time}'

# print(Star_cinama.hall_list)
# h1 = Hall(12,21,2108015)
# h2 = Hall(12,21,2108015)
# print(Star_cinama.hall_list)
import os

class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        cls.__hall_list.append(hall_obj)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__initialize_seats()
        Star_Cinema.entry_hall(self)

    def __initialize_seats(self):
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                self.__seats[(self.__hall_no, row, col)] = 0

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

    def book_seats(self, id, seats_to_book):
        # for seat in seats_to_book:
        #     if seat not in self.__seats or self.__seats[seat] == "Booked":
        #         raise ValueError("Invalid seat or already booked.")
        # for seat in seats_to_book:
        #     self.__seats[seat] = "Booked"
        for k in self.__seats.keys():
            if(k[0] == id and k[1] == seats_to_book[0] and k[2] == seats_to_book[1]):
                if self.__seats[k] == 0:
                    print("Set Bookking Successful ! ")
                    self.__seats[k] = 1
                    return
                else:
                    print("This set is Not available ! ")
                    return
        print("Not Valid information ! ")
        print("Please Enter Right information ! ")

    def view_show_list(self):
        for k in self.__show_list:
            print(f'{k[0]} {k[1]} {k[2]}')

    def view_available_seats(self, id):
        # for show_id, _, _ in self.__show_list:
        #     if show_id == id:
        #         return [seat for seat, status in self.__seats.items() if status == "Free"]
        # raise ValueError("Invalid show id.")
        for k, v in self.__seats.items():
            if k[0] == id:
                print(f"Set({k[1],k[2]}) = {v}")
            else:
                print("Not valid id.\nPlease right ingormation ! ")
h1 = Hall(5,5,111)

while True:
    os.system('cls')
    print("1. View All Show ! ")
    print("2. View Avialable Sets ! ")
    print("3. Book Ticket ! ")
    print("4. Entry Show ! ")
    print("5. Exit ! ")
    op = int(input("Enter your Option: "))
    if op ==1:
        os.system('cls')
        h1.view_show_list()
    elif op ==2:
        os.system('cls')
        hid = int(input("Enter Hall Id: "))
        h1.view_available_seats(hid)
    elif op == 3:
        os.system('cls')
        hid = int(input("Enter Hall Id: "))
        row = int(input("Enter Row: "))
        col = int(input("Enter Colum: "))
        h1.book_seats(hid,(row,col))
    elif op == 4:
        os.system('cls')
        hid = int(input("Enter Hall Id: "))
        m_name = input("Enter Movie name : ")
        time = input("Enter Time: ")
        h1.entry_show(hid,m_name,time)
    elif op == 5:
        break
    else:
        print("This is Wrong Option ! ")
    
    


# h2 = Hall(10,10,222)
# h1.entry_show(111,'Jawan','12:00 am')
# h1.entry_show(111,'Rajkumar','10:00 am')
# h2.entry_show(222,'Hawa','2:00 pm')
# h1.view_show_list()
# h2.view_show_list()
# h1.book_seats(111,(1,2))
# h2.book_seats(222,(1,2))
# h1.view_available_seats(111)
# h2.view_available_seats(222)




