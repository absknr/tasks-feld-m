from db import fetch_one

def run():
    # Re-implementing task1 using Postgres
    sql = """
    SELECT visitor_id 
    FROM transactions t1
    JOIN (SELECT id, max(revenue) FROM transactions) t2 
    ON t2.id = t1.id"""

    result = fetch_one(sql)

    if result:
        print("Visitor who created the most revenue: {}".format(result[0]))
    else:
        print("No visitors were found")


if __name__ == "__main__":
    run()

