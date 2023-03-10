from service.FooBarService import FooBarService

if __name__=='__main__':
    #Test Case 1
    FooBarService.create_buyer("Buyer1")
    FooBarService.create_buyer("Buyer2")
    FooBarService.create_buyer("Buyer3")
    FooBarService.create_seller("Seller1")
    FooBarService.create_auction("A1", 10, 50, "1", "seller1")
    FooBarService.create_bid("buyer1", "A1", 17)
    FooBarService.create_bid("buyer2", "A1", 15)
    FooBarService.update_bid("buyer2", "A1", 19)
    FooBarService.create_bid("buyer3", "A1", 19)
    FooBarService.close_auction("A1")
    FooBarService.get_profit("A1")
    print('__________________________')
    # Test Case 2
    FooBarService.create_seller("seller2")
    FooBarService.create_auction("A2", 5, 20, "2", "seller1")
    FooBarService.create_bid("buyer3", "A2", 25)
    FooBarService.create_bid("buyer2", "A2", 5)
    FooBarService.withdraw_bid("buyer2", "A2")
    FooBarService.close_auction("A2")
    FooBarService.get_profit("A2")
    print('__________________________')
    # Test Case 3
    FooBarService.create_auction("A3", 5, 20, "2", "seller2")
    FooBarService.create_bid("buyer3", "A3", 25)
    FooBarService.create_bid("buyer2", "A3", 5)
    FooBarService.create_bid("buyer1", "A3", 5)
    FooBarService.close_auction("A3")
    FooBarService.get_profit("A3")
    print('__________________________')
    # Test Case 4
    FooBarService.create_seller("seller2")
    FooBarService.create_auction("A2", 5, 20, "2", "seller1")
    FooBarService.create_bid("buyer3", "A2", 25)
    FooBarService.create_bid("buyer2", "A2", 5)
    FooBarService.withdraw_bid("buyer2", "A2")
    FooBarService.close_auction("A2")
    FooBarService.get_profit("A2")