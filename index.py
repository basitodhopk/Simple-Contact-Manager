import json
import os

CONTACT_FILE = "contacts.json"


# JSON فائل سے ڈیٹا لوڈ کرنے کا فنکشن
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}


# JSON فائل میں ڈیٹا محفوظ کرنے کا فنکشن
def save_contacts(contacts):
    with open(CONTACT_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


# نیا کانٹیکٹ شامل کرنے کا فنکشن
def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print(f"{name} کا کانٹیکٹ محفوظ کر دیا گیا ہے! ✅")


# کانٹیکٹ تلاش کرنے کا فنکشن
def search_contact(name):
    contacts = load_contacts()
    return contacts.get(name, "📌 کانٹیکٹ نہیں ملا!")


# کانٹیکٹ اپڈیٹ کرنے کا فنکشن
def update_contact(name, phone=None, email=None):
    contacts = load_contacts()
    if name in contacts:
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        save_contacts(contacts)
        print(f"{name} کا کانٹیکٹ اپڈیٹ ہو گیا ہے! ✨")
    else:
        print("❌ کانٹیکٹ نہیں ملا!")


# کانٹیکٹ ڈیلیٹ کرنے کا فنکشن
def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} کا کانٹیکٹ ڈیلیٹ ہو گیا ہے! 🗑️")
    else:
        print("❌ کانٹیکٹ نہیں ملا!")


# تمام کانٹیکٹس دکھانے کا فنکشن
def show_all_contacts():
    contacts = load_contacts()
    if contacts:
        print("\n📜 تمام کانٹیکٹس کی لسٹ:")
        print(json.dumps(contacts, indent=4, ensure_ascii=False))  # خوبصورت فارمیٹ میں دکھانے کے لیے
    else:
        print("📭 کوئی کانٹیکٹ موجود نہیں!")


# مین مینو چلانے کا فنکشن
if __name__ == "__main__":
    while True:
        print("\n📞 Contact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("🔹 اپنی پسند کا نمبر درج کریں: ")

        if choice == "1":
            name = input("نام: ")
            phone = input("فون نمبر: ")
            email = input("ای میل: ")
            add_contact(name, phone, email)

        elif choice == "2":
            name = input("🔍 تلاش کریں: ")
            result = search_contact(name)
            if isinstance(result, dict):
                print(f"📞 {name} کا ڈیٹا:")
                print(f"📱 فون: {result['Phone']}")
                print(f"📧 ای میل: {result['Email']}")
            else:
                print(result)

        elif choice == "3":
            name = input("🔄 جس کانٹیکٹ کو اپڈیٹ کرنا ہے اس کا نام: ")
            phone = input("📱 نیا فون نمبر (Enter دبائیں اگر بدلنا نہ ہو): ")
            email = input("📧 نئی ای میل (Enter دبائیں اگر بدلنی نہ ہو): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == "4":
            name = input("❌ جس کانٹیکٹ کو ڈیلیٹ کرنا ہے اس کا نام: ")
            delete_contact(name)

        elif choice == "5":
            show_all_contacts()

        elif choice == "6":
            print("👋 Contact Book بند ہو رہا ہے...")
            break

        else:
            print("❌ غلط انتخاب! دوبارہ کوشش کریں۔")
