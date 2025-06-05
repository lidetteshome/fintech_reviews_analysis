import pandas as pd
import oracledb
import os


class OracleDBInserter:
    def __init__(self, csv_path="../../data/sentiment_reviews.csv", user="admin", password="admin", dsn="localhost/XEPDB1"):
        self.csv_path = csv_path
        self.user = user
        self.password = password
        self.dsn = dsn
        self.df = None
        self.conn = None
        self.cursor = None

    def load_data(self):
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"❌ Input CSV not found: {self.csv_path}")
        self.df = pd.read_csv(self.csv_path)
        print(f"📥 Loaded {len(self.df)} records from {self.csv_path}")

    def connect(self):
        self.conn = oracledb.connect(
            user=self.user, password=self.password, dsn=self.dsn)
        self.cursor = self.conn.cursor()
        print("🔌 Connected to Oracle XE")

    def create_tables(self):
        self.cursor.execute("""
        BEGIN
            EXECUTE IMMEDIATE 'CREATE TABLE Banks (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name VARCHAR2(100) UNIQUE
            )';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -955 THEN RAISE; END IF;
        END;
        """)

        self.cursor.execute("""
        BEGIN
            EXECUTE IMMEDIATE 'CREATE TABLE Reviews (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                bank_id NUMBER,
                review_text CLOB,
                rating NUMBER,
                review_date DATE,
                source VARCHAR2(50),
                sentiment_label VARCHAR2(10),
                sentiment_score FLOAT,
                themes VARCHAR2(200),
                FOREIGN KEY (bank_id) REFERENCES Banks(id)
            )';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -955 THEN RAISE; END IF;
        END;
        """)

        print("🛠️ Tables checked/created")

    def insert_data(self):
        # Step 1: Insert banks
        banks = self.df["bank"].unique()
        for bank in banks:
            sql = """
            MERGE INTO Banks b
            USING (SELECT :bank_name AS name FROM dual) src
            ON (b.name = src.name)
            WHEN NOT MATCHED THEN
                INSERT (name) VALUES (src.name)
            """
            self.cursor.execute(sql, {"bank_name": bank})

        # Step 2: Insert reviews
        for _, row in self.df.iterrows():
            self.cursor.execute(
                "SELECT id FROM Banks WHERE name = :1", [row["bank"]])
            bank_id = self.cursor.fetchone()[0]

            self.cursor.execute("""
                INSERT INTO Reviews (
                    bank_id, review_text, rating, review_date, source,
                    sentiment_label, sentiment_score, themes
                ) VALUES (
                    :1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8
                )
            """, [
                bank_id,
                row["review"],
                int(row["rating"]),
                row["date"],
                row["source"],
                row["sentiment_label"],
                float(row["sentiment_score"]),
                row.get("themes", "Uncategorized")
            ])

        self.conn.commit()
        print(f"✅ Inserted {len(self.df)} reviews into the Oracle DB")

    def run(self):
        print("🚀 Running Task 3: Oracle DB Insert")
        self.load_data()
        self.connect()
        self.create_tables()
        self.insert_data()
        self.conn.close()
        print("🔒 Connection closed")
