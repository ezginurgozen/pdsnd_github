#bikeshare.py analyzes and provides statistical data regarding bike rental data for 3 cities:
#Chicago, New York City, and Washington for the 1st 6 months of year 2017.
#The data is in 3 different .csv files: chicago.csv, new_york_city.csv, washington.csv

import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Get User Data - ENG
    while(True):
        try:
            city = input('Enter city name to query. Options: "chicago, new york city, washington": ')
            city = city.lower()
            if(CITY_DATA.get(city) == None):
                continue
            else:
                break
        except:
            print('Wrong City Data.')
            print('Please enter city again. Options: "chicago, new york city, washington": ')

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        try:
            month = input('Please enter month. If you want to see data for all months, type "all". Options: "all, january ,february, march, april, may, june": ')
            month = month.lower()
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            if month in months:
                month = months.index(month)
                break
            else:
                print('Wrong Month Data.')
                print('Options: "all, january ,february, march, april, may, june": ')
                continue
        except:
            print('Wrong Month Data.')
            print('Please enter month again. If you want to see data for all months, type "all". Options: "all, january ,february, march, april, may, june": ')

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        try:
            day_of_week = input('Please enter day of the week. If you want to see data for all days, type "all". Options: "all, monday, tuesday, wednesday, thursday, friday, saturday, sunday": ')
            day_of_week = day_of_week.lower()
            days_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            print("DAY OF WEEK IS: ", day_of_week)
            if day_of_week in days_of_week:
                break
            else:
                print('Wrong Day Data.')
                print('Options: "all, monday, tuesday, wednesday, thursday, friday, saturday, sunday": ')
                continue
        except:
            print('Wrong Day Data.')
            print('Please enter day of the week again. If you want to see data for all days, type "all". Options: "all, monday, tuesday, wednesday, thursday, friday, saturday, sunday": ')

    print('-'*50)
    return city, month, day_of_week
#    return city, month, days_of_week[day_of_week]

def load_data(city, month, day_of_week):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'], format="%Y%m%d %H:%M:%S")
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 0:
        df = df[df['month'] == month]
        print("Month Filter Set")

    if day_of_week != 'all':
        df = df[df['day_of_week'] == day_of_week.title()]
        print("Day Filter Set")

    return df

def show_raw():
    print("SHOWING RAW")
    while(True):
        try:
            city = input('Enter city name to query. Options: "chicago, new york city, washington": ')
            city = city.lower()
            if(CITY_DATA.get(city) == None):
                continue
            else:
                df = pd.read_csv(CITY_DATA[city])
                break
        except:
            print('Wrong City Data.')
            print('Please enter city again. Options: "chicago, new york city, washington": ')
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time Datetime'] = pd.to_datetime(df['Start Time'], format="%Y%m%d %H:%M:%S")

    # TO DO: display the most common month
    df['month'] = df['Start Time Datetime'].dt.month
    popular_month = df['month'].mode()[0]
    print("Popular month: ", popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time Datetime'].dt.day
    popular_day = df['day'].mode()[0]
    print("Popular day: ", popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time Datetime'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print("Popular hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Popular start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Popular end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = (df['Start Station'] + " & " + df['End Station']).mode()[0]
    print("Popular start and end station combination: ", popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df.groupby(['User Type'])['User Type'].count()
    print("Count of user types: \n", count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df.groupby(['Gender'])['Gender'].count()
        print("Count of user gender: ", count_gender)
    else:
        print("No gender data exists for location. \n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_bd = df['Birth Year'].min()
        print("Min birth year is: ", earliest_bd)
        most_recent_bd = df['Birth Year'].max()
        print("Most recent birth year is: ", most_recent_bd)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year is: ", most_common_birth_year)
    else:
        print("No birth year data exists for location.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        try:
            choice = input('Would you like to see raw data OR filter by month/day? Enter "raw" OR "filter": ')
            choice = choice.lower()
            if choice == 'raw':
                df = show_raw()
                n = 0
                while choice == 'raw':
                    print(df.iloc[n:n+5])
                    choice = input('Type "raw" to see another 5 rows of raw data. Type "filter" to exit raw data view: ')
                    choice = choice.lower()
                    n += 5
            elif choice == 'filter':
                #get city, month, day from user and return the df containing the data you want - ENG
                city, month, day_of_week = get_filters()
                #instead of the predefined values, ask for user input  - ENG
                df = load_data(city, month, day_of_week)

                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
            else:
                print('Invalid input.')
        except:
            print('ERROR. Please try again.')

        ## See the column names in the dataframe - informative - ENG
#        for col in df.columns:
#            print(col)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
