from extract.api_extractor import get_products
from transform.api_transform import transformer

def main():
    products = get_products()
    dataframe = transformer(products)
    print(dataframe)

if __name__ == '__main__':
    main()