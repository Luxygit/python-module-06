"""proving isolation boundaries, intentionally triggering type errors"""
import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    res = alchemy.create_air()  # type: ignore
    print(f"Testing create_air: {res}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    print(f"{alchemy.create_earth()}")  # type: ignore
