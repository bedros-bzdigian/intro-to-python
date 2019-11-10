market = {"Dairy":["yogurt" , "cheese"] , "fruits" : ["bannana" , "apple" , "orange" , "lemon" , "apple" , "bannana" , "bannana"]}
print ("The dictionary market before changes: " , market)
market["candies"] = ["mars" , "kinder" , "twix"]
market["fruits"].sort()
market = market.get("fruits")
market  =list(dict.fromkeys(market))
print ("The dictionary market after changes: " , market)