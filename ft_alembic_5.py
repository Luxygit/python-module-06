"""importing from subfolder the create_air function using its __init__"""
from alchemy import create_air

if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...")
    res = create_air()
    print(f"Testing create_air: {res}")
