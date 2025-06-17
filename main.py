from lenta.lenta import load_data as lenta_load_data
from magnit.magnit import load_data as magnit_load_data

if __name__ == "__main__":
    lenta_load_data("lenta/lenta_result.json")
    magnit_load_data("magnit/magnit_result.json")