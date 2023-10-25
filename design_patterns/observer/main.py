from follower import Follower
from insta_vip import InstaVIP


account_1 = Follower('@the real account 1')
account_2 =  Follower('@account 2 official')

cristiano_ronaldo = InstaVIP()

cristiano_ronaldo.registerObserver(account_1)
cristiano_ronaldo.registerObserver(account_2)
cristiano_ronaldo.newPost()