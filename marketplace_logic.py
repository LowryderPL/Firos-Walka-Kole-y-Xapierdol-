import json

class Marketplace:
    def __init__(self, data_file="marketplace_data.json"):
        with open(data_file, "r", encoding="utf-8") as f:
            self.offers = json.load(f)

    def list_offers(self, item_type=None):
        if item_type:
            return [offer for offer in self.offers if offer.get("type") == item_type]
        return self.offers

    def get_offer_by_id(self, item_id):
        for offer in self.offers:
            if offer["id"] == item_id:
                return offer
        return None

    def filter_by_rarity(self, rarity):
        return [offer for offer in self.offers if offer.get("rarity") == rarity]

    def purchase_item(self, item_id, buyer, currency="TON"):
        offer = self.get_offer_by_id(item_id)
        if not offer:
            return "Item not found."

        if currency == "TON" and offer.get("price_ton"):
            return f"{buyer} paid {offer['price_ton']} TON to {offer['seller']} for {offer['name']}"
        elif currency == "RFN" and offer.get("price_rfn"):
            return f"{buyer} paid {offer['price_rfn']} RFN to {offer['seller']} for {offer['name']}"
        else:
            return "Currency not accepted for this item."

    def add_offer(self, name, seller, price_ton=None, price_rfn=None, rarity="common", type="nft"):
        new_offer = {
            "id": len(self.offers) + 1,
            "name": name,
            "seller": seller,
            "price_ton": price_ton,
            "price_rfn": price_rfn,
            "rarity": rarity,
            "type": type
        }
        self.offers.append(new_offer)
        self._save_data()
        return new_offer

    def _save_data(self):
        with open("marketplace_data.json", "w", encoding="utf-8") as f:
            json.dump(self.offers, f, indent=2, ensure_ascii=False)
