from marketplace_logic import Marketplace
from inventory import Inventory

def show_main_menu():
    print("=== ŚWIAT FIROS: Magic & Magic ===")
    print("1. Ekwipunek")
    print("2. Zadania")
    print("3. Bestiariusz")
    print("4. Spellbook / Rytuały")
    print("5. Marketplace (kupno/sprzedaż)")
    print("6. Wyjście")

def show_inventory():
    inventory = Inventory()
    items = inventory.get_items()
    print("\n=== TWÓJ EKWIPUNEK ===")
    for i, item in enumerate(items):
        print(f"{i+1}. {item['name']} | Typ: {item['type']} | Rzadkość: {item['rarity']}")
    input("\nWciśnij ENTER aby wrócić do menu...")

def show_marketplace():
    marketplace = Marketplace()
    print("\n=== MARKETPLACE ===")
    print("1. Przeglądaj oferty")
    print("2. Wystaw przedmiot")
    print("3. Wróć")
    choice = input("Wybierz opcję: ")
    
    if choice == "1":
        offers = marketplace.list_offers()
        print("\n--- OFERTY ---")
        for offer in offers:
            print(f"ID: {offer['id']} | {offer['name']} | Rzadkość: {offer['rarity']} | TON: {offer.get('price_ton')} | RFN: {offer.get('price_rfn')}")
        id_choice = input("Podaj ID przedmiotu do zakupu lub ENTER aby wrócić: ")
        if id_choice:
            item = marketplace.get_offer_by_id(int(id_choice))
            if item:
                currency = input("Zapłać [TON/RFN]: ").upper()
                result = marketplace.purchase_item(item["id"], buyer="Gracz1", currency=currency)
                print(result)
            else:
                print("Nie znaleziono przedmiotu.")
    elif choice == "2":
        inventory = Inventory()
        items = inventory.get_items()
        print("\nTwoje przedmioty:")
        for i, item in enumerate(items):
            print(f"{i+1}. {item['name']} ({item['rarity']})")
        pick = input("Wybierz numer przedmiotu do wystawienia: ")
        try:
            idx = int(pick) - 1
            if 0 <= idx < len(items):
                price_ton = input("Cena w TON (lub pusta): ")
                price_rfn = input("Cena w RFN (lub pusta): ")
                marketplace.add_offer(
                    name=items[idx]["name"],
                    seller="Gracz1",
                    price_ton=float(price_ton) if price_ton else None,
                    price_rfn=float(price_rfn) if price_rfn else None,
                    rarity=items[idx]["rarity"],
                    type=items[idx]["type"]
                )
                print("Przedmiot wystawiony!")
            else:
                print("Niepoprawny numer.")
        except Exception as e:
            print(f"Błąd: {e}")
    else:
        return

def run_game_menu():
    while True:
        show_main_menu()
        option = input("Wybierz opcję: ")
        if option == "1":
            show_inventory()
        elif option == "2":
            print("[ZADANIA] – wkrótce.")
        elif option == "3":
            print("[BESTIARIUSZ] – wkrótce.")
        elif option == "4":
            print("[SPELLBOOK / RYTUAŁY] – wkrótce.")
        elif option == "5":
            show_marketplace()
        elif option == "6":
            print("Wyjście z gry.")
            break
        else:
            print("Nieprawidłowy wybór.\n")

if __name__ == "__main__":
    run_game_menu()
