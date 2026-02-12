class Dal:
    @staticmethod
    def get_top_customer(cnx):
        try:
            with cnx.cursor(dictionary=True) as cursor:
                statement = """
                        SELECT c.customerNumber, COUNT(c.customerNumber) as amount
                        FROM customers c
                        JOIN orders o
                        ON c.customerNumber = o.customerNumber
                        GROUP BY c.customerNumber
                        ORDER BY amount LIMIT 10;
                            """
                cursor.execute(statement)
                customer = cursor.fetchall()
            return customer
        except Exception as e:
            raise Exception(f"Could not fetch top customer from db, Error: {str(e)}")

    @staticmethod
    def get_customers_without_orders(cnx):
        try:
            with cnx.cursor(dictionary=True) as cursor:
                statement = """
                        SELECT customerNumber
                        FROM customers
                        WHERE customerNumber NOT IN (
                            SELECT customerNumber
                            FROM (
                                SELECT c.customerNumber AS customerNumber, COUNT(c.customerNumber) as amount
                                FROM customers c
                                JOIN orders o
                                ON c.customerNumber = o.customerNumber
                                GROUP BY c.customerNumber
                                )
                        );
                            """
                cursor.execute(statement)
                customer = cursor.fetchall()
            return customer
        except Exception as e:
            raise Exception(f"Could not fetch customers without orders from db, Error: {str(e)}")

    @staticmethod
    def get_zero_credit_active_customers(cnx):
        try:
            with cnx.cursor(dictionary=True) as cursor:
                statement = """
                        WITH tmp AS (
                            SELECT *
                            FROM customers
                            WHERE creditLimit = 0
                        )
                        SELECT c.customerNumber, COUNT(c.customerNumber) as amount
                        FROM customers c
                        JOIN tmp t
                        ON c.customerNumber = t.customerNumber
                        GROUP BY c.customerNumber
                            """
                cursor.execute(statement)
                customer = cursor.fetchall()
            return customer
        except Exception as e:
            raise Exception(f"Could not fetch active customers with zero credit from db, Error: {str(e)}")
