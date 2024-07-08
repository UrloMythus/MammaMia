
def convert_US_date(date):
    us_data = next((country_data for country_data in date['results'] if country_data["iso_3166_1"] == "US"), None)
    if us_data:
        us_release_dates_type_3 = [rd for rd in us_data['release_dates'] if rd['type'] == 3]
        # Sort the list of release dates and get the latest
        us_release_dates_type_3.sort(key = lambda x: x['release_date'], reverse=True)
        if len(us_release_dates_type_3) > 0:
            latest_release_date = us_release_dates_type_3[0]['release_date']
            date = latest_release_date.split('T')[0]
            print('Latest US theatrical release date:', date)
            return date
        else:   
            us_release_dates_type_4 = [rd for rd in us_data['release_dates'] if rd['type'] == 4]
            us_release_dates_type_4.sort(key = lambda x: x['release_date'], reverse=True)
            if len(us_release_dates_type_4) > 0:
                latest_release_date = us_release_dates_type_4[0]['release_date']
                date = latest_release_date.split('T')[0]
                print('Latest US theatrical release date (type 4):', date)
                return date