
import json

class Marketplace:
    def __init__(self, data_file="marketplace_data.json"):
        with open(data_file, "r", encoding="utf-8") as f:
            self.offers = json.load(f)

    def list_offers(self):
        return self.offers

    def get_offer_by_id(self, nft_id):
        for offer in self.offers:
            if offer["id"] == nft_id:
                return offer
        return None

    def filter_by_rarity(self, rarity):
        return [offer for offer in self.offers if offer["rarity"] == rarity]

    def purchase_nft(self, nft_id, buyer, currency="TON"):
        offer = self.get_offer_by_id(nft_id)
        if not offer:
            return "NFT not found."
        if currency == "TON" and offer["price_ton"]:
            return f"{buyer} paid {offer['price_ton']} TON to {offer['seller']}"
        elif currency == "RFN" and offer["price_rfn"]:
            return f"{buyer} paid {offer['price_rfn']} RFN to {offer['seller']}"
        else:
            return "Currency not accepted for this NFT."
