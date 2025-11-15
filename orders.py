# You're welcome to use this decorator
# See: https://www.geeksforgeeks.org/python/python-functools-total_ordering/
from functools import total_ordering
import math

from data_structures import List, ArrayR
from data_structures import ArrayMaxHeap
from data_structures import ArrayList

class Order:
    def __init__(self, hunger: int, location: tuple[float, float]):
        """
            Constructor for Order.
            No analysis required.
        """
        self.hunger = hunger
        self.location = location
        self.distance = None
            
    def __str__(self):
        return f"Order(hunger={self.hunger}, distance={round(self.distance, 2)})"

@total_ordering
class dispatchitem:
    def __init__(self, order:Order):
        self.order = order 
    def score(self):
        return 4 * self.order.distance - 5 * self.order.hunger
    def __lt__(self,order1: "dispatchitem") -> bool:
        return self.score() > order1.score()
    def __eq__(self,order1: "dispatchitem") -> bool:
        return self.score() == order1.score()

class OrderDispatch:
    def __init__(self, dispatch_location: tuple[float, float], max_orders: int):
        """
            Constructor for OrderDispatch.
            Complexity Analysis:
            Best: O(1)
            Worst:O(1)
            ...
        """
        self.dispatch_location = dispatch_location
        self.max_orders = max_orders
        self.heap = ArrayMaxHeap(max_orders + 1)
    def __len__(self):
        """
            Return the number of pending orders in the dispatch system.
            No analysis required.
        """
        return len(self.heap)
        
    
    def receive_order(self, order: Order):
        """
            Receive a new Food Flight order into the dispatch system.
            Complexity Analysis:
            Calculating the distance require arithmatic operation which: O(1)
            Wrapping the order inside a dispatch item: O(1)
            Adding to the heap result: O(logN) where N is the number of orders currently stored 
            So the overall complexity is O(logN) + O(1) + O(1): O(logN)
            ...
        """
        if self.heap.is_full():
            raise Exception("Dispatch Orders Exceeded")
        dx = order.location[0] - self.dispatch_location[0]
        dy = order.location[1] - self.dispatch_location[1]
        order.distance = math.sqrt(dx*dx + dy*dy)
        self.heap.add(dispatchitem(order))
        
    def deliver_single(self) -> Order:
        """
            Deliver a single pending order with the lowest
            FoodFast (TM) score.
            See specifications for details.
            Complexity Analysis: 
            Extracting from a max heap requires reheapifying.
            Reheapifying: O(logN) where n is the number orders currently stored in the heap
            Best: O(1) when no swaps are made
            Worst: O(logN)
            ...
        """
        if len(self.heap) == 0:
            raise Exception("No orders to be delivered")
        else:
            item = self.heap.extract_max()
            return item.order
        
    
    def deliver_multiple(self, max_travel: float) -> List[Order]:
        """
            Deliver as many orders, prioritising orders such that
            lower FoodFast (TM) scores are delivered first.
            See specifications for details.
            Complexity Analysis:
            Calls Extract_max() on the heap, which takes O(logN), where N is the number of orders currently stored in the heap. 
            If an order is not delivered we have to add it back to the heap which result in O(logn), where N is the 
            number of orders currently stored in the heap. 
            Therfore the overall complexity: O(k*logN)
            k: number of orders it tried to deliver. 
            
        """
        delivered = ArrayList()
        not_delivered = ArrayList()
        remaining = max_travel
        current_x, current_y = self.dispatch_location
        while len(self.heap) > 0 : 
            item = self.heap.extract_max()
            order = item.order
            dx = order.location[0] - current_x
            dy = order.location[1] - current_y
            to_order = math.sqrt(dx*dx + dy*dy)
            
            hx = order.location[0] - self.dispatch_location[0]
            hy = order.location[1] - self.dispatch_location[1]
            back_home = math.sqrt(hx*hx + hy*hy)
            
            if remaining - to_order - back_home >= 0 : 
                delivered.append(order)
                remaining -= to_order
                current_x, current_y = order.location 
            else : 
                not_delivered.append(item)
                continue
        for i in range(len(not_delivered)):
            self.heap.add(not_delivered[i])
        return delivered
 
    def order_surge_1054(self, surge_batch: ArrayR[Order]):
        """
            Add all orders from surge batch, ensuring this is done as
            efficiently as possible to minimise downtime.
            Complexity Analysis:
            ...
        """
        pass
if __name__ == "__main__":
    # Test your code here

    # Let's create a dispatch and a few orders
    dispatch_location = (2, 3)
    dispatch = OrderDispatch(dispatch_location, max_orders=10)
    
    first_orders = [
        Order(3, (5, 6)),
        Order(4, (6, 4)),
        Order(1, (4, 4))
    ]
    
    second_orders = [
        Order(7, (-4, 3)),
        Order(10, dispatch_location), # Someone ordered FROM the dispatch!
        Order(5, (0, 5))
    ]
    
    for order in first_orders:
        dispatch.receive_order(order)
        
    # Dispatch an order
    first_dispatched = dispatch.deliver_single()
    
    print("1st dispatch:", first_dispatched)
    
    # Now we add the second collection
    for order in second_orders:
        dispatch.receive_order(order)
        
    # Let's see what gets delivered now
    second_dispatched = dispatch.deliver_single()
    
    print("2nd dispatch:", second_dispatched)


