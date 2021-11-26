import unittest, json, os
from src import statement as s
from assertpy import assert_that

basedir = os.path.dirname(os.path.abspath("lab07"))


class StatementTest(unittest.TestCase):
    def setUp(self):
        self.invoice = json.load(open(os.path.join(basedir, "data", "Invoice.json").replace("\\", "/"), "r"))
        self.plays = json.load(open(os.path.join(basedir, "data", "Plays.json").replace("\\", "/"), "r"))

    def test_statement_wrongPlayType(self):
        self.plays["hamlet"] = {"name": "Hamlet", "type": "action"}
        self.assertRaises(ValueError, s.statement, self.invoice, self.plays)

    def test_statement_tragedy_audience_lt30(self):
        assert_that(s.statement(self.invoice, self.plays)).ends_with("You earned 25 credits\n")

    def tearDown(self):
        self.invoice = None
        self.plays = None

