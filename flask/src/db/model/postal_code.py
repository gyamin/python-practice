from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.sql import select


class PostalCode:

    def __init__(self, conn):
        self.conn = conn
        metadata = MetaData()
        self.postalCode = Table('postal_code', metadata,
                                Column('postal_code', Integer, primary_key=True),
                                Column('address_kana_1', String),
                                Column('address_kana_2', String),
                                Column('address_kana_3', String),
                                Column('address_1', String),
                                Column('address_2', String),
                                Column('address_3', String),
                                Column('created_at', String),
                                )

    def search_address_by_postal_code(self, postal_code):
        """
        郵便番号で住所を返す（RAW SQL）
        :param postal_code:
        :return:
        """
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
        return self.conn.execute(sql, {"code": postal_code}).fetchall()

    def search_address_by_postal_code2(self, postal_code):
        """
        郵便番号で住所を返す（select関数利用）
        :param postal_code:
        :return:
        """
        sql = select(self.postalCode).where(self.postalCode.c.postal_code == postal_code)
        print(str(sql))
        result = self.conn.execute(sql)
        return result

    def search_address_by_prefectures(self, prefectures):
        """
        指定された都道府県のレコードを返す（あえて１都道府県ずつループしてDBからデータ取得して、配列にマージ）
        :param prefectures:
        :return:
        """

        for prefecture in prefectures:
            sql = select(self.postalCode).where(self.postalCode.c.address_1 == prefecture)
            rows = self.conn.execute(sql)

            address = []
            for row in rows:
                buff = {}
                for field in row._fields:
                    buff[field] = row._mapping[field]
                address.append(buff)

        return address
