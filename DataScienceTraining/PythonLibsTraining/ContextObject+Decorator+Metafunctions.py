from sqlite3 import connect

class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen_inst, None)


@contextmanager
def temptable(cur):
    cur.execute("create table points(x int, y int)")
    try:
        yield
    finally:
        cur.execute("drop table points")

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute("insert into points (x, y) values (1, 1)")
        cur.execute("insert into points (x, y) values (1, 2)")
        cur.execute("insert into points (x, y) values (2, 3)")
        cur.execute("insert into points (x, y) values (3, 4)")
        for row in cur.execute("select x, y from points"):
            print(row)
        for row in cur.execute("select sum(x * y) from points"):
            print(row)


