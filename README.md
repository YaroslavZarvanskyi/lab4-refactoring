№,Тест-кейс (назва методу),Що перевіряється,Очікуваний результат,Статус
1,test_add_dish_to_menu,Додавання страви в об'єкт Menu.,Страва з'являється у списку.,PASSED
2,test_dish_properties,Коректність збереження назви та ціни.,Дані збігаються з вхідними.,PASSED
3,test_empty_menu_at_start,Стан меню відразу після створення.,Кількість страв дорівнює 0.,PASSED
4,test_order_creation,Створення об'єкта замовлення для клієнта.,Об'єкт містить посилання на клієнта.,PASSED
5,test_order_has_correct_dishes,Зв'язок замовлення зі списком страв.,Список страв у замовленні не порожній.,PASSED
6,test_failed_search,"Пошук страви, якої немає в меню.",Метод повертає False.,PASSED
7,test_singleton_identity,Паттерн Singleton для бази даних.,Обидві змінні вказують на один об'єкт.,PASSED
8,test_singleton_persistence,Збереження даних у Singleton-об'єкті.,Дані доступні через будь-яку точку доступу.,PASSED
9,test_factory_regular_order,Створення звичайного замовлення через Factory.,Об'єкт має клас RegularOrder.,PASSED
10,test_factory_bulk_order,Створення масового замовлення через Factory.,Об'єкт має клас BulkOrder.,PASSED
11,test_factory_invalid_type,Обробка невідомого типу в Factory.,Викликається виняток ValueError.,PASSED
12,test_observer_notification,Паттерн Observer: сповіщення кухні.,Кухня отримує дані про нове замовлення.,PASSED
13,test_multiple_observers,Сповіщення кількох спостерігачів одночасно.,Усі підписані об'єкти отримали апдейт.,PASSED
14,test_order_flow_integration,Інтеграційний тест: Factory -> DB -> Notifier.,Повний ланцюжок від створення до сповіщення.,PASSED
15,test_customer_naming,Перевірка цілісності імені клієнта.,Ім'я відображається без помилок.,PASSED