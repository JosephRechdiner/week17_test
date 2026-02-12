class EventsHandler:
    @staticmethod
    def insert_customer(cnx, customer):
        try:
            with cnx.cursor() as cursor:
                statement = """
                INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(statement, (customer["customerNumber"],
                                           customer["customerName"],
                                           customer["contactLastName"],
                                           customer["contactFirstName"],
                                           customer["phone"],
                                           customer["addressLine1"],
                                           customer["addressLine2"],
                                           customer["city"],
                                           customer["state"],
                                           customer["postalCode"],
                                           customer["country"],
                                           customer["salesRepEmployeeNumber"],
                                           customer["creditLimit"],
                                           ))
            cnx.commit()
        except Exception as e:
            raise Exception(f"Could not insert customer to sql db,  Error: {str(e)}")

    @staticmethod
    def insert_order(cnx, order):
        try:
            with cnx.cursor() as cursor:
                statement = """
                INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(statement, (order["orderNumber"],
                                           order["orderDate"],
                                           order["requiredDate"],
                                           order["shippedDate"],
                                           order["status"],
                                           order["comments"],
                                           order["customerNumber"],
                                           ))
            cnx.commit()
        except Exception as e:
            raise Exception(f"Could not insert order to sql db, Error: {str(e)}")
        


