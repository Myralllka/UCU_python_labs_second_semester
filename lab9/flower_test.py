from flower import *

def flower_test():
    print("Flower test...")
    flower1 = Flower("red", 10, 15)
    try:
        flower2 = Flower(1, "", [])
        assert (False)
    except Exception:
        pass

    assert (isinstance(flower1, Flower))
    assert (flower1.colour == "red")
    assert (flower1.num == 10)
    assert (flower1.price == 15)


def tulip_test():
    print("Tulit test...")
    tulip1 = Tulip("red", 10, 15)
    try:
        tulip2 = Tulip(1, "", [])
        assert (False)
    except Exception:
        pass

    assert (isinstance(tulip1, Flower))
    assert (isinstance(tulip1, Tulip))
    assert (tulip1.colour == "red")
    assert (tulip1.num == 10)
    assert (tulip1.price == 15)


def rose_test():
    print("Rose test...")
    rose1 = Rose("red", 10, 15)
    try:
        rose2 = Rose(1, "", [])
        assert (False)
    except Exception:
        pass

    assert (isinstance(rose1, Flower))
    assert (isinstance(rose1, Rose))
    assert (rose1.colour == "red")
    assert (rose1.num == 10)
    assert (rose1.price == 15)


def chamomile_test():
    print("Chamomile test...")
    chamomile1 = Chamomile("red", 10, 15)
    try:
        chamomile2 = Chamomile2(1, "", [])
        assert(False)
    except Exception:
        pass
    assert (isinstance(chamomile1, Flower))
    assert (isinstance(chamomile1, Chamomile))
    assert (chamomile1.colour == "red")
    assert (chamomile1.num == 10)
    assert (chamomile1.price == 15)



def flower_set_test():
    flower1 = Rose("red", 10, 15)
    flower2 = Rose("white", 10, 15)
    flower3 = Rose("yellow", 10, 15)
    flower4 = Tulip("white", 10, 10)
    flower_set1 = FlowerSet([flower1, flower2, flower3])
    try:
        flower_set2 = FlowerSet([flower1, flower2, flower3, flower4])
        flower_set3 = FlowerSet([])
        assert False
    except Exception:
        pass

def bucket_test():
    flower1 = Rose("red", 10, 15)
    flower2 = Rose("white", 10, 15)
    flower3 = Rose("yellow", 10, 15)
    flower_set1 = FlowerSet([flower1, flower2, flower3])

    flower5 = Tulip("red", 10, 15)
    flower6 = Tulip("white", 10, 15)
    flower7 = Tulip("yellow", 10, 15)
    flower8 = Tulip("white", 10, 10)
    flower_set2 = FlowerSet([flower5, flower6, flower7, flower8])

    bucket1 = Bucket([flower_set1, flower_set2])
    bucket2 = Bucket([flower_set2])
    try:
        bucket1 = Bucket([])
        assert (False)
    except Exception:
        pass
    assert(bucket1.price_all() == 100)
    assert(bucket2.price_all() == 55)
rose_test()
tulip_test()
flower_test()
bucket_test()
flower_set_test()
chamomile_test()
