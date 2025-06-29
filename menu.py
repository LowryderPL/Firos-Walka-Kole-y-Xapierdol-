from marketplace_logic import Marketplace

def show_main_menu():
    print("=== Świat Firos: Magic & Magic ===")
    print("1. Ekwipunek")
    print("2. Zadania")
    print("3. Bestiariusz")
    print("4. Spellbook / Rytuały")
    print("5. Marketplace")
    print("6. Wyjście")

def show_marketplace():
    marketplace = Marketplace()
    print("\n=== MARKETPLACE ===")
    print("Dostępne oferty:")
    offers = marketplace.list_offers()
    for offer in offers:
        print(f"ID: {offer['id']} | {offer['name']} | {offer['rarity']} | TON: {offer.get('price_ton')} | RFN: {offer.get('price_rfn')}")
    choice = input("Podaj ID przedmiotu do zakupu lub ENTER aby wrócić: ")
    if choice:
        item = marketplace.get_offer_by_id(int(choice))
        if item:
            currency = input("Zapłać [TON/RFN]: ").upper()
            result = marketplace.purchase_item(item["id"], buyer="Gracz1", currency=currency)
            print(result)
        else:
            print("Nieprawidłowy ID.")
    print()

def run_game_menu():
    while True:
        show_main_menu()
        option = input("Wybierz opcję: ")
        if option == "1":
            print("[EKWIPUNEK] (placeholder)")
        elif option == "2":
            print("[ZADANIA] (placeholder)")
        elif option == "3":
            print("[BESTIARIUSZ] (placeholder)")
        elif option == "4":
            print("[SPELLBOOK / RYTUAŁY] (placeholder)")
        elif option == "5":
            show_marketplace()
        elif option == "6":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór.\n")

if __name__ == "__main__":
    run_game_menu()
