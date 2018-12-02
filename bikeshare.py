import time
import pandas as pd
import numpy as np
from collections import Counter
import calendar

# Path of Data
path = "C:/Users/fzaju/Udacity/Programming_4_ds/python/Project_Bikeshare/bikeshare-2/"

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Loop for user input until valid entry for city
    # Here without TRY/Exception method
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # ==== City Filtering ====
    city = input('Please enter the desired city : ').lower()

    while True:
        if city not in CITY_DATA:
            print('Ups, sorry no data for this city: Try \n\n Chicago, New York City or Washington')
            city = input().lower()
        else:
            print('Ok', city, 'it\'s your town!')
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    # ==== Month Filtering ====
    # Try to use the handling exception loop from lections for user input
    # I've found a solution to raise an error on stackoverflow: https://stackoverflow.com/questions/35246467/raising-error-if-string-not-in-one-or-more-lists


    month_selection =['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while True:
        try:
            month = str(input(' Please enter a month or just "all" for no filter: ')).lower()
            if month not in month_selection:
                raise ValueError('At least one list does not contain "%s"' % (month))
            break
        except:
            print('Ups that\'s not a filter option, please try again')

        finally:
            # ??? Why this is printed even when the error occurs ???
            # ??? I thought it's is only displayed once when finally leaving the loop???
            print('OK, we show you the data for: ', month)

    print('OK, we show you the data for: ', month)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # ==== DAY Filtering ====
    # Try to use the handling exception loop from lections for user input

    day_selection = list(calendar.day_name)

    print('\n\n PLease use one of these day names: ', day_selection)

    while True:
        try:
            day = str(input(' Please enter a day name or just "all" for no filter: ')).title()
            if day not in day_selection:
                raise ValueError('At least one  list does not contain "%s"' % (day))
            break
        except:
            print('Ups that\'s not a filter option, please try again')

        finally:
            # ??? Why this is printed even when the error occurs ???
            # ??? I thought it's is only displayed once when finally leaving the loop???
            print('OK, we show you the data for: ', day)

    print('OK, we show you the data for: ', day)


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
# Loading Data from selected city incl. path

    df = pd.read_csv(path + CITY_DATA[city])
    df = pd.DataFrame(df)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Week Day:', popular_day)


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ' , popular_end_station)



    # TO DO: display most frequent combination of start station and end station trip
    popular_pair_station = df['End Station'] + '_' + df['Start Station']
    print('Most Popular End Station: ', popular_pair_station.mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Travel time in total: ',df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean travel time : ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Type : ',df['User Type'].value_counts())

    if 'Gender' and 'Birth Year' in df.columns:
        # Cleaning Data by Identifying NaN Values in Columns
        print('How many NaN Vales in Dataset? ', df.isnull().sum())

        # TO DO: Display counts of gender
        df_gender = df['Gender'].dropna()
        print('Counts of Gender : ',df_gender.value_counts())


        # TO DO: Display earliest, most recent, and most common year of birth
        df_year = df['Birth Year'].dropna()
        print('Earliest Year: ',df_year.min())
        print('Recent Year: ',df_year.max())
        print('Most common Year: ',df_year.mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def raw_lines(df):
        yes_no = ['Yes', 'No'] # option for selection

        while True:
            raw_data_display = input(' Do you want to see 5 raw data lines? Yes/No: ').title()
            if raw_data_display in yes_no:
                break
            else:
                print('Ups that\'s not a filter option, please try again')

        counter_lines = 0

        while raw_data_display == 'Yes':
            counter_lines += 5
            print(df.head(counter_lines))
            raw_data_display = input('5 more line? --> Yes/No: ').title()








def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
