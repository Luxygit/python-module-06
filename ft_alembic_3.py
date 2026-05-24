""""""
from alchemy.elements import create_air

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accesing alchemy/elements.py using 'from ... import ...' structure")
    res = create_air()
    print(f"Testing create_air: {res}")
