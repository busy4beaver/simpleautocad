# simpleautocad/cli.py
import sys
from .Utility import AutoCAD

def main():
    """Консольная утилита для проверки подключения к AutoCAD."""
    import argparse
    parser = argparse.ArgumentParser(description="Проверка подключения к AutoCAD")
    parser.add_argument("--version", action="store_true", help="Показать версию")
    parser.add_argument("--check", action="store_true", help="Проверить подключение")
    args = parser.parse_args()

    if args.version:
        from .__version__ import __version__
        print(f"simpleautocad v{__version__}")
        return 0

    if args.check:
        try:
            from .Utility import AutoCAD
            app = AutoCAD()
            print(f"Подключено к AutoCAD версии: {app.Version}")
            print("Активный документ:", app.ActiveDocument.Name)
            return 0
        except Exception as e:
            print(f"Ошибка подключения: {e}", file=sys.stderr)
            return 1

    parser.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())