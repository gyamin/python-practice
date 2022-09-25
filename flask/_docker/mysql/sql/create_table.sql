CREATE TABLE IF NOT EXISTS postal_code (
    postal_code VARCHAR(7) PRIMARY KEY COMMENT '郵便番号',
    address_kana_1 VARCHAR(50)  COMMENT '住所かな１',
    address_kana_2 VARCHAR(50)  COMMENT '住所かな２',
    address_kana_3 VARCHAR(50)  COMMENT '住所かな３',
    address_1 VARCHAR(50)  COMMENT '住所１',
    address_2 VARCHAR(50)  COMMENT '住所２',
    address_3 VARCHAR(50)  COMMENT '住所３',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日'
)
ENGINE = InnoDB
COMMENT ='郵便番号'