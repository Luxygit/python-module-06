"""importing all functions from a subfolder"""
import alchemy.elements

if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accesing alchemy/elements.py using 'import ...' structure")
    res = alchemy.elements.create_earth()
    print(f"Testing create_earth: {res}")
