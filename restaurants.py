# You're welcome to use this decorator
# See: https://www.geeksforgeeks.org/python/python-functools-total_ordering/
from functools import total_ordering
import math
from data_structures.array_max_heap import ArrayMaxHeap
from typing import Iterator
from data_structures import ArrayR
from data_structures import ArrayList
from better_bst import BetterBinarySearchTree

class MenuItem:
    def __init__(self, name: str, rating: float):
        """
            Constructor for Restaurant.
            No analysis required.
        """
        self.name = name
        self.rating = rating
        
        
    def __str__(self):
        """
            String representation method for MenuItem class.
            Implementation optional - perhaps useful for debugging.
            No analysis required.
        """
        return f"{self.name} {self.rating}"
        


class Restaurant:
    def __init__(self, name: str, block_number: int, initial_menu: ArrayR[MenuItem]):
        """
            Constructor for Restaurant.
            Complexity Analysis: 
            Copying itsms from ArrayR to ArrayList takes O(n) times 
            Best: ArrayList is already sorted O(n)
            Worst: It's in reverse order so insertion sort takes O(n^2) 
            n: Number of items in the ArrayList 
            ...
        """
        self.name = name
        self.block_number = block_number
        self.menu = ArrayList()
        for i in range(len(initial_menu)):
            self.menu.append(initial_menu[i])
        self._sort_()
    
    def _sort_(self):
        menu = self.menu
        for i in range(1,len(menu)):
            current = menu[i]
            j =  i - 1 
            while j >= 0 : 
                if menu[j].rating < current.rating:
                    menu[j+1] = menu[j]
                elif menu[j].rating == current.rating and menu[j].name > current.name:
                    menu[j+1] = menu[j]
                else:
                    break
                j -= 1 
            menu[j+1] = current
    
    def __str__(self):
        """
            String representation method for Restaurant class.
            Implementation optional - perhaps useful for debugging.
            No analysis required.
        """
        return f"{self.name} {self.block_number}"
    
@total_ordering
class RankItem:
    def __init__(self,item: MenuItem, r_index: int):
        self.item = item 
        self.r_index = r_index
            
    def __lt__(self,other):
        if self.item.rating != other.item.rating:
            return self.item.rating < other.item.rating
        return self.item.name > other.item.name
    def __eq__(self,other):
        return (self.item.rating == other.item.rating and self.item.name == other.item.name)
        

class FoodFlight:
    def __init__(self):
        """
            Constructor for FoodFlight.
            Complexity Analysis:
            ...
            Overall Complexity: O(1)
        """
        self.restaurant = BetterBinarySearchTree()
        
    
    def add_restaurant(self, restaurant: Restaurant):
        """
            Register a `restaurant` in the FoodFlight app.
            Complexity Analysis:
            Performs insertion into a BST which takes O(h) time. 
            h: height of the tree
            Since tree is always balanced;
            Overall Complexity: O(logN) N; number of restraunts stored
            ...
        """
        self.restaurant[restaurant.name] = restaurant
        
    
    def get_menu(self, restaurant_name: str):
        """
            Return all menu items for a restaurant in decreasing order of their ratings.
            Complexity Analysis:
             Search in a BST takes O(h)
            Returning takes O(1) time. 
            Since tree is balanced:
            Overall Complexity: O(logN)
            h; heigh of the tree
            N; number of retaurants stored
            ...
        """
        try: 
            restaurant = self.restaurant[restaurant_name]
        except KeyError: 
            raise("Restaurant name not found")
        return restaurant.menu
    

    def add_to_menu(self, restaurant_name: str, new_items: ArrayR[MenuItem]):
        """
            Add an ArrayR of MenuItems to a Restaurant's menu.
            Complexity Analysis:  
            Best Case: Occurs when new items have lower rating so it is appended to the end of the list. Each append takes O(1): O(m)
            Worst Case: Occurs when the new item has the highest rating so needed to be added to the front of the list. Append takes O(n)
            So the worst Case: (m*n)
            m: new items to be added 
            n: number items currently in the menu
            ...
        """
        try: 
            restaurant = self.restaurant[restaurant_name]
        except KeyError: 
            raise("Restaurant name not found")
        
        for i in range (len(new_items)):
            item = new_items[i]
            inserted = False
            
            for j in range(len(restaurant.menu)):
                current = restaurant.menu[j]
                
                if (item.rating > current.rating) or (item.rating == current.rating and item.name < current.name):
                    restaurant.menu.insert(j,item)
                    inserted = True
                    break
            if inserted == False: 
                restaurant.menu.append(item)
 
    def meal_suggestions(self, user_block_number: int, max_walk: int) -> Iterator[MenuItem]:
            #Yield all menu items within max_walk blocks of the user's current block.
            #Complexity Analysis (across all __next__ calls): 
            #Best Case: O(N) there are no restraunts in max_walk distance so the generator return immediately. 
            #Worst Case: O(N + MlogR)
            #Occurs when all retaurants are in distance of max_walk and all menu items are processed. 
            #This includes scanning retaurnts O(N) creating the heap O(R) and
            #repeated heap extract/insert operations for each menu item (M * O(logR)).
            #N: Number of retaurants in the BST 
            #M: total menu items yielded 
            #R: number of retaurants in walking distance. 
        
        
        restaurant_reach = ArrayList()
        for name, restaurant in self.restaurant:
            if abs(restaurant.block_number-user_block_number)<= max_walk:
                restaurant_reach.append(restaurant)
        if len(restaurant_reach) == 0 : 
            def empty():
                if False:
                    yield None 
            return empty()
        
        heap = ArrayMaxHeap(len(restaurant_reach)+1)
        positions = ArrayR(len(restaurant_reach))
        for i in range(len(positions)):
            positions[i] = 0 
        for i, restaurant in enumerate(restaurant_reach):
            if len(restaurant.menu) > 0: 
                heap.add(RankItem(restaurant.menu[0],i))
                
        def generator():
            while len(heap) > 0 : 
                top = heap.extract_max()
                yield top.item
                positions[top.r_index] += 1 
                pos = positions[top.r_index]
                menu = restaurant_reach[top.r_index].menu
                if pos < len(menu):
                    heap.add(RankItem(menu[pos], top.r_index))
        return generator()

if __name__ == "__main__":
    # Test your code here
    
    # First restaurant with no initial menu items
    first_restaurant = Restaurant("Testaurant", 3, ArrayR(0))
    
    # Add to the FF app
    ff = FoodFlight()

    ff.add_restaurant(first_restaurant)
    
    # Add to Testaurant's menu
    new_items = ArrayR(3)
    new_items[0] = MenuItem("Chips", 2)
    new_items[1] = MenuItem("Pizza", 4)
    new_items[2] = MenuItem("Burger", 3)
    
    ff.add_to_menu("Testaurant", new_items)
    
    # Get the best item from the menu
    print("Best menu item:", ff.get_menu("Testaurant")[0]) 