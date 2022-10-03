import time
import mousecode as mc

api = mc.MouseAPI()

start = time.perf_counter()
park = api.get_park(mc.EPCOT)
print(f'PARK INFO RETRIEVAL: {time.perf_counter() - start} ns')
print()
start = time.perf_counter()
tb = park.tipboard()
print(f'TIPBOARD RETRIEVAL: {time.perf_counter() - start} ns')


print(tb)