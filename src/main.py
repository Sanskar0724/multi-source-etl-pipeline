from extract.api_extractor import get_products
from transform.api_transform import transformer
from load.api_load_postgres import load_data

def main():
    products = get_products()
    dataframe = transformer(products)
    load_data(dataframe)

if __name__ == '__main__':
    main()