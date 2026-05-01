from abc import ABC, abstractmethod

class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self._dishes = []

    def add_dish(self, dish: Dish):
        self._dishes.append(dish)

    def contains_dish(self, dish: Dish) -> bool:
        return dish in self._dishes

    def get_all_dishes(self):
        return self._dishes

class Customer:
    def __init__(self, name: str):
        self.name = name


class OrderDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderDatabase, cls).__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def save(self, order):
        self.orders.append(order)


class OrderObserver(ABC):
    @abstractmethod
    def update(self, order):
        pass

class Kitchen(OrderObserver):
    def __init__(self):
        self.received_orders = []

    def update(self, order):
        self.received_orders.append(order)
        print(f"[Кухня] Отримано замовлення від {order.customer.name}")

class KitchenNotifier:
    def __init__(self):
        self._observers = []

    def attach(self, observer: OrderObserver):
        self._observers.append(observer)

    def notify(self, order):
        for observer in self._observers:
            observer.update(order)


class Order(ABC):
    def __init__(self, customer: Customer, dishes: list):
        self.customer = customer
        self.dishes = dishes

class RegularOrder(Order):
    pass

class BulkOrder(Order):
    pass

class OrderFactory:
    @staticmethod
    def create_order(order_type: str, customer: Customer, dishes: list) -> Order:
        if order_type == "regular":
            return RegularOrder(customer, dishes)
        elif order_type == "bulk":
            return BulkOrder(customer, dishes)
        raise ValueError("Unknown order type")
