from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text


class PostalCode:

    def __init__(self, conn):
        self.conn = conn

    def search_address_by_postal_code(self, postal_code):
        sql = text(
            "select "
            "postal_code, "
            "address_kana_1, "
            "address_kana_2, "
            "address_kana_3, "
            "address_1, "
            "address_2, "
            "address_3, "
            "created_at "
            "from postal_code where postal_code = :code"
        )
        return self.conn.execute(sql, postal_code).fetchall()
