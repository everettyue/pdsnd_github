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
    city = ''
    f = ''
    month =''
    day = ''
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    month_list = ["january", "february", "march", 'april', 'may', 'june']
    
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n")
        city = city.lower()
        if city == "chicago" or city == "new york city" or city == "washington":
            break
        else:
            print("Invalid city, please try again.")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        f = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for not time filter\n")
        f = f.lower()
        if f == 'month' or f == 'day' or f == 'both' or f == 'none':
            break
        else:
            print("Invalid filter, please try again.")
    if f == 'month':
        while True:
            month = input ("Which month - January, February, March, April, May, or June?\n")
            month = month.lower()
            if month in month_list:
                break
            else:
                print("Invalid month, please try again.")
    elif f == 'day':
        while True:
            day = input ("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n")
            day = day.lower()
            if day in day_list:
                break
            else:
                print("Invalid day, please try again.")
    elif f == 'both':
        while True:
            month = input ("Which month - January, February, March, April, May, or June?\n")
            month = month.lower()
            if month in month_list:
                break
            else:
                print("Invalid month, please try again.")
        while True:
            day = input ("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n")
            day = day.lower()
            if day in day_list:
                break
            else:
                print("Invalid day, please try again.")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
       

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
    df['hour'] = df['Start Time'].dt.hour
    
    if month != '':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != '':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    print("Most popular Month:", df['month'].value_counts().idxmax())
    # TO DO: display the most common day of week
    print("Most popular Month:", df['day_of_week'].value_counts().idxmax())
    # TO DO: display the most common start hour
    print("Most popular Month:", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['conbine'] = df['Start Station'] + " to " + df['End Station']
    # TO DO: display most commonly used start station
    print("Most popular start station:", df['Start Station'].value_counts().idxmax()) 

    # TO DO: display most commonly used end station
    print("Most popular end station:", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("Most popular combination of start station and end station:", df['conbine'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean of travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type Count:\n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("Gender Count:\n",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth: ", int(df['Birth Year'].min()))
    print("The most recent year of birth: ", int(df['Birth Year'].max()))
    print("The most common year of birth: ", int(df['Birth Year'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw(df):
    while True:
        view = input("Would you like to view the raw data? 'Yes' or 'No' \n")
        view = view.lower()
        if view == 'yes' or view == 'no':
            break
        else:
            print("Invalid option, please try again.")
    if view == 'yes':        
        print(df.head())

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
