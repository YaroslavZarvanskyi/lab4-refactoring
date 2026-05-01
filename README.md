# Restaurant Management System

Система імітує роботу ресторану (меню, замовлення, кухня) з дотриманням принципів SOLID та використанням патернів проектування.

**Використані патерни:**
* **Singleton** (Database)
* **Factory Method** (Orders)
* **Observer** (Kitchen Notifications)

### ✅ Результати тестування (18/18 тестів пройдено)

#### Базовий функціонал (SOLID)
- [x] `test_add_dish_to_menu` — додавання страви в меню
- [x] `test_dish_properties` — валідація назви та ціни
- [x] `test_customer_creation` — створення об'єкта клієнта
- [x] `test_empty_menu_at_start` — початковий стан меню
- [x] `test_multiple_dishes_in_menu` — додавання кількох страв
- [x] `test_order_creation_with_customer` — прив'язка до замовника
- [x] `test_order_has_correct_dishes` — склад замовлення
- [x] `test_notifier_attaching` — реєстрація спостерігача
- [x] `test_failed_search_in_menu` — обробка відсутності страви
- [x] `test_database_storage_initially_empty` — стан бази даних

#### Патерни проектування
- [x] **Singleton**: `test_singleton_identity` — унікальність БД
- [x] **Singleton**: `test_singleton_persistence` — збереження даних
- [x] **Factory**: `test_factory_regular_order` — створення RegularOrder
- [x] **Factory**: `test_factory_bulk_order` — створення BulkOrder
- [x] **Factory**: `test_factory_invalid_type` — обробка помилок типів
- [x] **Observer**: `test_kitchen_receives_notification` — сповіщення кухні
- [x] **Observer**: `test_multiple_observers_notification` — група підписників
- [x] **Integration**: `test_order_flow_integration` — повний цикл системи
