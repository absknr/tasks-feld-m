## System Preparation for Task 5

In **task 5**, a system installation of **PostgreSQL** is needed. PostgreSQL is required for **psycopg2**(PostgreSQL driver for Python) to install successfully. Kindly refer postgres [documentation](https://www.postgresql.org/download/) for installation instructions of your OS.

If you are using **MacOS/Linux** and have `homebrew` installed, you can install PostgreSQL by simply running:

```
$ brew install postgresql
```

**WARNING:** The following commands assume a **latest homebrew** installation of PostgresSQL on **MacOS**. Kindly refer homebrew docs to find the equivalent command for your environment and OS.

**Start the PostgreSQL server:**

```
$ pg_ctl -D /opt/homebrew/var/postgres start
```

Replace the `/opt/homebrew/var/postgres` argument in the command with the equivalent path on your system where postgres is installed. To stop the server, replace `start` with `stop`.

**Connect to server:**

```
$ psql postgres
```

The above command starts the Postgres CLI. It should look like this:

```
postgres=# 
```

Run the following commands in the Postgres CLI.

**Create DB:**

```
create database transactions;
```

**Change to the newly created DB:**

```
\connect transactions;
```

**Create tables:**

```
CREATE TABLE Devices(
    id     INTEGER,
    device_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE TRANSACTIONS(
    id SERIAL,
    datetime TIMESTAMP,
    visitor_id BIGINT,
    device_type INTEGER,
    revenue REAL,
    tax REAL,
    PRIMARY KEY(id),
    FOREIGN KEY(device_type) REFERENCES Devices(id)
);
```

**Insert records:**

```
INSERT INTO devices (id, device_name) VALUES (1, 'Desktop'), (2, 'Tablet'), (3, 'Mobile Phone'), (4, 'Unknown');

INSERT INTO transactions (datetime, visitor_id, device_type, revenue, tax)
VALUES
('2019-10-05 00:00:00',1016870803637,1,173.3314596961336,0.19),
('2019-10-11 00:00:00',48076008851343,4,290.10535175922513,0.07),
('2019-08-19 00:00:00',72300317870324,2,511.4181420476257,0.07),
('2019-10-14 00:00:00',84516511452821,3,593.8755045649982,0.19),
('2019-09-10 00:00:00',44780848857001,3,674.2801956714196,0.07);
```

## Instructions

`pipenv` is used to manage python packages in this project. To install, run

```
$ pip install pipenv
```
After successful installation, open the project folder and and install all dependencies:

```
$ cd tasks-feld-m
$ pipenv install
```

Next, activate the virtual environment:

```
$ pipenv shell
```

Now, we `cd` into the **project** folder and start executing scripts.

```
$ cd project
```

To run each task script individually, just run the script with the task name using the `python` command like:

```
$ python task1.py
```
To execute all tasks, run:

```
$ python run.py
```

