# FilmLocator
A simple web application that shows all films that are filmed in San Francisco. Provide a fancy map view and filters.

# Data source
https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am

# Link to the demo
http://ec2-54-175-160-14.compute-1.amazonaws.com

# Technologies
- Frontend
  - HTML5+CSS
  - JQuery
  - Bootstrap
  - NoUISlider
  - Select2
  - Infobox
  - richmarker
  - markercluster
- Backend
  - SQLite
- Web Framework
  - This web app is written in python using Django framework
- Thrid party API
  - Google Map Javascript API
  - Google Map Places API
  - Google Map Geocoding API

# How to set up and run?
To test and run locally, you can simply clone the repo and execute "python manage.py runserver".

All the data has already been loaded into the database. If you want to reload the data, you can execute the "load_data.py" under data_process folder.

You might need to configure Apache2 or whatever web servere you prefer to host the website publicly.



# Test cases
There are some test cases for the film searching service <a href="https://github.com/zym242/FilmLocator/blob/master/webapp/tests.py">here</a>.

Run the test cases by "python manage.py test"

# Future work
Currently, it's quite hard to ensure the geolocation in this web app is correct and accurate because some addresses are quite confusing and even google map api can not find the correct geolocation.

The current dataset is static and small, so we're able to use SQLite to do the filters and autocompletion. However, if the dataset grows extremely large, we might want to consider using elasticsearch to speed up the search funciontality and autocomletion.

You may notice that it's still a bit slow loading all the data into Google Map. Due to time limit, I didn't find a nice way to improve it right now.



