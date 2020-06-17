import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_choice(choices):
    chosen = None
    while chosen == None:
        for i, choice in enumerate(choices):
            print("{} {}".format(i, choice))

        try:
            chosen = list(choices)[int(input('Enter choice number: '))]
        except (IndexError, ValueError):
            print("Choose a number from 0 to {}".format(len(choices) - 1))

        return chosen

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_choice(CITY_DATA.keys())

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = get_choice(months + ['all'])
        month = input('Not a valid month. Please select a month from January to June or answer All.').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = get_choice(days + ['all'])

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if df['month'].nunique() > 1:
        print('The most common month is: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    if df['day_of_week'].nunique() > 1:
        print('The most common day of week is: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('The most common start houris: {}'.format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start stations: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: {}'.\
          format(df.groupby(['Start Station', 'End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total trip duration is: {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average trip duration is: {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print('Counts of gender: \n{}'.format(df['Gender'].value_counts()))
    # TO DO: Display earliest, most recent, and most common year of birth
        df['Birth Year'] = df['Birth Year'].fillna(df['Birth Year'].mode()[0]).astype(int)
        print('The earlist year of birth: {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    except KeyError:
        print('Oops, no gender data or birth data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        sample_data = None
        while sample_data == None or sample_data == 'yes':
            sample_data = input('\nWould you like to see some sample data? Enter yes or no.\n')

        while True
            if input('\nWould you like to see some sample data? Enter yes or no.\n').lower() != 'yes':
                break

        sample_data = input('\nWould you like to see some sample data? Enter yes or no.\n')
        i = 0
        while sample_data.lower() == 'yes':
            print(df.iloc[50*i:50*(i+1), :])
            i += 1
            sample_data = input('\nMore data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
