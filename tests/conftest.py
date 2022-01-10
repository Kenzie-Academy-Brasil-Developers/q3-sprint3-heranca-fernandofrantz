from pytest import fixture
from classes.copo import Copo
from classes.recipient import Recipient


@fixture
def copo_comum():
    return Copo(300)


@fixture
def rec_comum():
    return Recipient(100)


@fixture
def rec_negativo():
    return Recipient(-1000)
