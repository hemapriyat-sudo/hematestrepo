from datetime import date, datetime


def main():
    while True:
        date_input = input('Enter a future date (YYYY-MM-DD): ')

        try:
            target_date = datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            print('Please enter a valid date in YYYY-MM-DD format.')
            continue

        days_left = (target_date - date.today()).days
        if days_left <= 0:
            print('Please enter a date later than today.')
            continue

        print(f'{days_left} day(s) left until {target_date.isoformat()}.')
        break


if __name__ == '__main__':
    main()