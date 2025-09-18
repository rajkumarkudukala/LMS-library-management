# add_product.py
import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def add_member(name, email):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category":category, "stock":stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    print("1) add_member")
    print("2) add_book")
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
 
        created = add_member(name, email)
        print("Inserted:", created)
    if(ch == 2):
        title = input("Enter title: ").strip()
        author = input("Enter author name: ").strip()
        category = input("Enter category: ").strip()
        stock = int(input("Enter stock: ").strip())
 
        created = add_book(title, author, category, stock)
        print("Inserted:", created)