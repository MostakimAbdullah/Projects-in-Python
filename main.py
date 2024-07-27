from Menu import Pizza,Burger,Drinks,Menu
from Restraurant import Restraurent
from User import Chef,Customer,Server,Manager
from Order import Order
def main():
    menu=Menu()
    pizza_1=Pizza("Beef Pizza",600,"large",["Beef","onion"])
    menu.add_menu_item("pizza",pizza_1)
    pizza_2=Pizza("Alu Pizza",400,"large",["Potato","onion","oil"])
    menu.add_menu_item("pizza",pizza_2)
    pizza_3=Pizza("Vegetable Pizza",500,"large",["Capcicum","onion","sausage"])
    menu.add_menu_item("pizza",pizza_3)


    burger_1=Burger("Beef Burger",750,"Beef",["Bread","onion","cheese"])
    menu.add_menu_item("burger",burger_1)
    burger_2=Burger("Chicken Burger",650,"Chicken",["Bread","capsicum","cheese"])
    menu.add_menu_item("burger",burger_2)

    coke=Drinks("Coke",50,True)
    menu.add_menu_item("drinks",coke)
    coffee=Drinks("Black Coffee",300,False)
    menu.add_menu_item('drinks',coffee)
    
    
    menu.show_menu()

    mk_res=Restraurent("MK Restraurent",2000,menu)

    manager=Manager("Akbar Ali",123456,"akbar@email.com","Anderkilla",1500,"Jan 1 2020","core")
    mk_res.add_employee("manager",manager)
    chef=Chef("Rustom ALi",123,"Rustom@gmail.com","Khulshi",1000,"Feb 01 2024","Chef","Pizza")
    mk_res.add_employee("chef",chef)
    server=Server("Kawser",234,"kawser@gmail.com","Oxygen",500,"Feb 01 2024","Server")
    mk_res.add_employee("server",server)

    mk_res.show_employee()

    customer_1=Customer("Mostakim",234567,"mostakim@gmail.com","Rajapukur Lane",100000)

    order_1=Order(customer_1,[burger_1,coke])
    customer_1.place_order(order_1)
    mk_res.add_order(order_1)

    mk_res.receive_payment(order_1,2000,customer_1)
    print("Revenue and Balance of Restraurent from customer 1 :",mk_res.revenue,mk_res.balance)

    customer_2=Customer("Tawhid",234567,"Tawhidim@gmail.com","Raja",105000)

    order_2=Order(customer_2,[pizza_2,pizza_1,burger_1,burger_2,pizza_3,pizza_2,coke])
    customer_2.place_order(order_2)
    mk_res.add_order(order_2)

    mk_res.receive_payment(order_2,10000,customer_2)
    print("Revenue and Balance of Restraurent from customer 2 :",mk_res.revenue,mk_res.balance)
    mk_res.pay_expense(mk_res.rent,'Rent')
    print("After paying Rent",mk_res.revenue,mk_res.balance,mk_res.expense)

    mk_res.pay_salary(manager)
    print("After paying Salary",mk_res.revenue,mk_res.balance,mk_res.expense)






if __name__=='__main__':
    main()