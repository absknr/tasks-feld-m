from db import fetch_one


def run():
    sql = """
    SELECT visitor_id 
    FROM transactions t1
    JOIN (SELECT id, revenue FROM transactions ORDER BY revenue DESC LIMIT 1) t2 
    ON t2.id = t1.id"""

    # Note: db_type="postgres" executes the query over the configured postgres DB
    result = fetch_one(sql, db_type="postgres")

    if result:
        print("Visitor who created the most revenue: {}".format(result[0]))
    else:
        print("No visitors were found")


if __name__ == "__main__":
    run()
