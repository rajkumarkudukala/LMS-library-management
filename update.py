# update_stock.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def update_stock(product_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", product_id).execute()
    return resp.data
def update_email(product_id, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("member_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    print("1) update email")
    print("2) update stock")
    ch = int(input("Enter choice: "))
    if ch == 1:
        pid = int(input("Enter member_id to update: ").strip())
        new_stock = input("Enter new email: ").strip()
    
        updated = update_email(pid, new_stock)
        if updated:
            print("Updated record:", updated)
        else:
            print("No record updated — check product_id.")
    if ch == 2:
        pid = int(input("Enter book_id to update: ").strip())
        new_stock = int(input("Enter new stock value: ").strip())
    
        updated = update_stock(pid, new_stock)
        if updated:
            print("Updated record:", updated)
        else:
            print("No record updated — check product_id.")