# 2 - masala

import psycopg2
from colorama import Fore
from db import db_info


def get_connection():
    return psycopg2.connect(**db_info)


def insert_product(name,price,color,image):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('''INSERT INTO product(name,price,color,image) VALUES(%s,%s,%s,%s)''',(name,price,color,image))
        conn.commit()
        print(Fore.LIGHTGREEN_EX + 'Product inserted successfully' + Fore.RESET)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_product(product_id,name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''DELETE FROM product WHERE id = %s and name = %s''',(product_id,name))
    conn.commit()
    print(Fore.LIGHTGREEN_EX + 'Product deleted successfully' + Fore.RESET)

def show_product(product_id,name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM product WHERE id = %s and name = %s ''',(product_id,name))
    products = cur.fetchall()
    for product in products:
        print(product)

def update_product(product_id,name,price,color,image):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''UPDATE product SET  name = %s, price = %s,color = %s, image = %s WHERE id = %s''',(name,price,color,image,product_id))
    conn.commit()
    print(Fore.LIGHTGREEN_EX + 'Product updated successfully' + Fore.RESET)


def main():
    print(Fore.RED + 'Create Product      => 1' + Fore.RESET)
    print(Fore.MAGENTA + 'Show all Product    => 2' + Fore.RESET)
    print(Fore.CYAN + 'Update Product      => 3' + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + 'Delete Product      => 4' + Fore.RESET)
    print(Fore.LIGHTRED_EX + 'Quit                => 5' + Fore.RESET)
    return input(Fore.LIGHTBLUE_EX + 'Enter your choice: ' + Fore.RESET)

def run():
    while True:
        choice = main()
        if choice == '1':
            name = input(Fore.CYAN + 'Enter Product Name: ' + Fore.RESET)
            price = input(Fore.LIGHTYELLOW_EX + 'Enter Product Price: ' + Fore.RESET)
            color = input(Fore.LIGHTWHITE_EX + 'Enter Product Color: ' + Fore.RESET)
            image = input(Fore.LIGHTGREEN_EX + 'Enter Product Image Url: ' + Fore.RESET)
            insert_product(name,price,color,image)

        elif choice == '2':
            product_id = input('Enter Product ID: ')
            name = input('Enter Product Name: ')
            show_product(product_id,name)

        elif choice == '3':
            product_id = input(Fore.LIGHTCYAN_EX + 'Enter Product ID: ' + Fore.RESET)
            name = input(Fore.CYAN + 'Enter Product New Name: ' + Fore.RESET)
            price = input(Fore.LIGHTYELLOW_EX + 'Enter Product New Price: ' + Fore.RESET)
            color = input(Fore.LIGHTWHITE_EX + 'Enter Product New Color: ' + Fore.RESET)
            image = input(Fore.LIGHTGREEN_EX + 'Enter Product New Image Url: ' + Fore.RESET)
            update_product(product_id,name,price,color,image)

        elif choice == '4':
            product_id = input(Fore.LIGHTCYAN_EX + 'Enter Product ID: ' + Fore.RESET)
            name = input(Fore.CYAN + 'Enter Product New Name: ' + Fore.RESET)
            delete_product(product_id,name)

        elif choice == '5':
            print(Fore.MAGENTA + 'Thank You' + Fore.RESET)
            break

        else:
            print('Invalid Choice' + Fore.RESET)

if __name__ == '__main__':
    run()