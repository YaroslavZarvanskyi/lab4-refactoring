import unittest

from main import OrderDatabase, Menu, Customer, Dish, RegularOrder, KitchenNotifier, Kitchen, OrderFactory, BulkOrder


class TestRestaurantSystem(unittest.TestCase):

    def setUp(self):
        # Очищуємо Singleton перед кожним тестом (важливо для тестів)
        OrderDatabase._instance = None
        self.db = OrderDatabase()
        self.menu = Menu()
        self.customer = Customer("Ivan")
        self.dish = Dish("Pizza", 200.0)

    # --- Базові тести та TDD ---

    def test_add_dish_to_menu(self):
        self.menu.add_dish(self.dish)
        self.assertTrue(self.menu.contains_dish(self.dish))

    def test_dish_properties(self):
        self.assertEqual(self.dish.name, "Pizza")
        self.assertEqual(self.dish.price, 200.0)

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Ivan")

    def test_empty_menu_at_start(self):
        self.assertEqual(len(self.menu.get_all_dishes()), 0)

    def test_multiple_dishes_in_menu(self):
        d2 = Dish("Pasta", 150)
        self.menu.add_dish(self.dish)
        self.menu.add_dish(d2)
        self.assertEqual(len(self.menu.get_all_dishes()), 2)

    def test_order_creation_with_customer(self):
        order = RegularOrder(self.customer, [self.dish])
        self.assertEqual(order.customer.name, "Ivan")

    def test_order_has_correct_dishes(self):
        order = RegularOrder(self.customer, [self.dish])
        self.assertIn(self.dish, order.dishes)

    def test_notifier_attaching(self):
        notifier = KitchenNotifier()
        kitchen = Kitchen()
        notifier.attach(kitchen)
        self.assertIn(kitchen, notifier._observers)

    def test_failed_search_in_menu(self):
        d2 = Dish("Sushi", 500)
        self.assertFalse(self.menu.contains_dish(d2))

    def test_database_storage_initially_empty(self):
        self.assertEqual(len(self.db.orders), 0)

    # --- Тести паттернів ---

    # Singleton
    def test_singleton_identity(self):
        db2 = OrderDatabase()
        self.assertIs(self.db, db2)

    def test_singleton_persistence(self):
        self.db.save("Order1")
        db2 = OrderDatabase()
        self.assertEqual(len(db2.orders), 1)

    # Factory
    def test_factory_regular_order(self):
        order = OrderFactory.create_order("regular", self.customer, [self.dish])
        self.assertIsInstance(order, RegularOrder)

    def test_factory_bulk_order(self):
        order = OrderFactory.create_order("bulk", self.customer, [self.dish])
        self.assertIsInstance(order, BulkOrder)

    def test_factory_invalid_type(self):
        with self.assertRaises(ValueError):
            OrderFactory.create_order("vip", self.customer, [self.dish])

    # Observer
    def test_kitchen_receives_notification(self):
        notifier = KitchenNotifier()
        kitchen = Kitchen()
        notifier.attach(kitchen)
        order = OrderFactory.create_order("regular", self.customer, [self.dish])
        notifier.notify(order)
        self.assertEqual(len(kitchen.received_orders), 1)
        self.assertEqual(kitchen.received_orders[0].customer.name, "Ivan")

    def test_multiple_observers_notification(self):
        notifier = KitchenNotifier()
        k1, k2 = Kitchen(), Kitchen()
        notifier.attach(k1)
        notifier.attach(k2)
        order = OrderFactory.create_order("regular", self.customer, [self.dish])
        notifier.notify(order)
        self.assertEqual(len(k1.received_orders), 1)
        self.assertEqual(len(k2.received_orders), 1)

    def test_order_flow_integration(self):
        # Factory -> Database -> Notifier
        order = OrderFactory.create_order("regular", self.customer, [self.dish])
        self.db.save(order)
        notifier = KitchenNotifier()
        kitchen = Kitchen()
        notifier.attach(kitchen)
        notifier.notify(order)

        self.assertIn(order, self.db.orders)
        self.assertIn(order, kitchen.received_orders)


if __name__ == '__main__':
    unittest.main()
