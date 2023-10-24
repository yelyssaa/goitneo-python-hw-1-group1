from datetime import datetime

today = datetime.today().date()

def get_birthdays_per_week(users:list[dict]):

    result = {}
    _, n_week, n_day = today.isocalendar()

    def check_week_day(day, name):
        if day in result:
            result[day].append(name)
        else:
            result[day] = [name]

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        _, u_week, u_day = birthday_this_year.isocalendar()
        print(_, u_week, u_day)
        print(_, n_week, n_day)
        if u_week - n_week == 1:
            week_day = birthday_this_year.strftime('%A')
            check_week_day(week_day, name)
        elif u_week - n_week == 0 and u_day in (6, 7):
            check_week_day('Monday', name)
        
    for day, users in result.items():
        format_users = ''
        for n, u in enumerate(users):
            if n != len(users)-1:
                format_users += f'{u}, '
            else:
                format_users += f'{u}'
        print(f'{day}: {format_users}')