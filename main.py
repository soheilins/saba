import datetime

def main():
    print("=" * 40)
    print("Hello from GitHub Actions!")
    print(f"Current time (UTC): {datetime.datetime.now(datetime.UTC)}")
    print("Your scheduled workflow is running successfully.")
    print("=" * 40)

if __name__ == "__main__":
    main()
