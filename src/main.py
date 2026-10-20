import sys

def main():
    if "--test" in sys.argv:
        print("[Тест]: Бот успешно запущен и готов к работе!")
    else:
        print("Бот запущен. Ожидание команд...")

if __name__ == "__main__":
    main()
