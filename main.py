import sys
from utils import get_coordinates, get_district_by_coordinates


def main():
    if len(sys.argv) != 2:
        print("Использование: python main.py 'адрес'")
        sys.exit(1)

    address = sys.argv[1]

    try:
        coords = get_coordinates(address)
        district = get_district_by_coordinates(coords)
        print(f"Адрес: {address}")
        print(f"Район: {district}")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
