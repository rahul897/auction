class Auction:
    def __init__(self,auction_id, lowest_bid_limit, highest_bid_limit,partiticipation_cost, seller):
        self.auction_id = auction_id
        self.lowest_bid_limit = int(lowest_bid_limit)
        self.highest_bid_limit = int(highest_bid_limit)
        self.partiticipation_cost = int(partiticipation_cost)
        self.seller = seller

    def validate(self,amount):
        return self.lowest_bid_limit <= amount <= self.highest_bid_limit
