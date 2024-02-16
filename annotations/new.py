from typing import Dict,Union,List,Optional
def full_name (first_name:str,last_name:str ):
    print('My name is '+first_name+'and my last name is '+last_name)


full_name('Ram','Laxman')

def hobby(my_list:list[int,int,int]):
    #means that the list body has 3 values which are all int 
    fist=my_list[0]

    print(fist)

hobby([4,5,3])

#simillarly i can have

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price) 

process_items(prices={'micah':33.2,'inaband':34.4})

# also we can declare that the variable can be of different types, for that we use Union

def UnionOf(prices:Union[str,int,float]):
        print(prices)

UnionOf('twelve')

def nameis(name:Optional[str]=None):
    if name is not None:
        print(f'name={name}')
    else:
        print('no name included')

nameis()

# Optional[str]=None is actually a replacement for Union[str,None]

