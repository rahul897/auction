from dao.DB import DB
from model.Auction import Auction
from model.Bid import Bid
from model.Buyer import Buyer
from model.Seller import Seller
import heapq
import bisect

from model.Transaction import Transaction


class FooBarService:

    @classmethod
    def create_buyer(cls, name):
        buyer = Buyer(name)
        DB.buyers[name] = buyer

    @classmethod
    def create_seller(cls, name):
        seller = Seller(name)
        DB.sellers[name] = seller

    @classmethod
    def create_auction(cls, auction_id, lowest_bid_limit, highest_bid_limit, partiticipation_cost, seller):
        auction = Auction(auction_id, lowest_bid_limit, highest_bid_limit, partiticipation_cost, seller)
        DB.auctions[auction_id] = auction

    @classmethod
    def create_bid(cls, buyer, auction_id, amount):
        bid = Bid(buyer, auction_id, amount)
        auction = DB.auctions[auction_id]
        if auction_id not in DB.auction_participents:
            DB.auction_participents[auction_id] = 0
        if auction.validate(amount):
            if auction_id not in DB.bids:
                DB.bids[auction_id] = []
                DB.amount_bid[auction_id] = {}
            heapq.heappush(DB.bids[auction_id], bid)
            if amount not in DB.amount_bid[auction_id]:
                DB.amount_bid[auction_id][amount] = []
            DB.amount_bid[auction_id][amount].append(bid)
            DB.auction_participents[auction_id] += 1
            print("bid created "+str(bid))
            if buyer not in DB.buyer_auction:
                DB.buyer_auction[buyer] = set()
            DB.buyer_auction[buyer].add(auction_id)
        else:
            DB.auction_participents[auction_id] += 1
            print("amount is out of auction limit ")


    @classmethod
    def update_bid(cls, buyer, auction_id, amount):
        bid = Bid(buyer, auction_id, amount)
        auction = DB.auctions[auction_id]
        if auction.validate(amount):
            ind,old_bid = cls.get_bid(bid,auction_id)
            DB.amount_bid[auction_id][old_bid.amount].remove(old_bid)
            DB.bids[auction_id][ind] = bid
            heapq.heapify(DB.bids[auction_id])
            if amount not in DB.amount_bid[auction_id]:
                DB.amount_bid[auction_id][amount] = []
            DB.amount_bid[auction_id][amount].append(bid)
            print("bid amount updated "+str(bid))
        else:
            print("amount is out of auction limit ")

    @classmethod
    def get_bid(cls,bid,auction_id):
        ind = 0
        old_bid = None
        for i, iter_bid in enumerate(DB.bids[auction_id]):
            if iter_bid == bid:
                ind = i
                old_bid = iter_bid

        return (ind,old_bid)

    @classmethod
    def withdraw_bid(cls, buyer, auction_id):
        bid = Bid(buyer, auction_id, 0)
        ind,old_bid = cls.get_bid(bid,auction_id)
        DB.amount_bid[auction_id][old_bid.amount].remove(old_bid)
        DB.bids[auction_id].remove(old_bid)
        heapq.heapify(DB.bids[auction_id])
        DB.auction_participents[auction_id] += -1
        print("bid withdrawn updated")

    @classmethod
    def close_auction(cls, auction_id):
        winning_bid = None
        while True and len(DB.bids[auction_id])>0:
            winning_bid = heapq.heappop(DB.bids[auction_id])
            if len(DB.amount_bid[auction_id][winning_bid.amount]) == 1 or len(DB.buyer_auction[winning_bid.buyer])>0:
                break
        # auction = DB.auctions[auction_id]
        # if auction.seller not in DB.seller_txns:
        #     DB.seller_txns[auction.seller] = []

        participents = DB.auction_participents[auction_id]
        if winning_bid is None:
            print("no winner")
            DB.txns[auction_id] = Transaction(auction_id, None, participents)
        else:
            print("winner is {}".format(winning_bid.buyer))
            DB.txns[auction_id] = Transaction(auction_id, winning_bid, participents)

    @classmethod
    def get_profit(cls, auction_id):
        profit = 0
        txn = DB.txns[auction_id]
        auction = DB.auctions[auction_id]
        if txn.winning_bid is None:
            profit = txn.participents * auction.partiticipation_cost * .2
        else:
            profit = txn.winning_bid.amount - (
                        auction.highest_bid_limit + auction.lowest_bid_limit) // 2 \
                     + txn.participents * auction.partiticipation_cost * .2
        print("profit for " + auction.seller ,profit)
