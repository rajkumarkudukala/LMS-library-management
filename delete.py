# delete_product.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def delete_member(member_id):
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

def delete_book(book_id):
    resp = sb.table("products").delete().eq("book_id", book_id).execute()
    return resp.data
 
if __name__ == "__main__":
    print("1) Delete member")
    print("2) Delete Book")
    ch = int(input("Enter choice: "))
    if ch == 1:
        pid = int(input("Enter member_id to delete: ").strip())
        confirm = input(f"Are you sure you want to delete member {pid}? (yes/no): ").strip().lower()
        if confirm == "yes":
            deleted = delete_member(pid)
            if deleted:
                print("Deleted:", deleted)
            else:
                print("No product deleted — check product_id.")
        else:
            print("Delete cancelled.")
    if ch == 2:
        pid = int(input("Enter book_id to delete: ").strip())
        confirm = input(f"Are you sure you want to delete book {pid}? (yes/no): ").strip().lower()
        if confirm == "yes":
            deleted = delete_book(pid)
            if deleted:
                print("Deleted:", deleted)
            else:
                print("No product deleted — check product_id.")
        else:
            print("Delete cancelled.")