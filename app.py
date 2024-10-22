"""
A simple temperature conversion web app using Flask.

This module contains a single class, 'app', which is a Flask web application.
The app has a single route, '/', which accepts GET and POST requests.
The route renders an HTML template 'index.html' using the 'render_template' function
from Flask. The template contains a form which accepts a temperature value and two
units of measurement. If the form is submitted, the route calls the
'convert_temperature' function to convert the temperature and then renders the
template again, passing in the result of the conversion as a variable.

The 'convert_temperature' function takes a float value and two strings representing
units of measurement. Depending on the units, it returns the converted value.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    """
    Converts a temperature value from one unit of measurement to another.

    Args:
        value (float): The value of the temperature to be converted.
        from_unit (str): The unit of measurement of the input temperature.
        to_unit (str): The desired unit of measurement of the output temperature.

    Returns:
        float: The converted temperature value. If the from_unit is the same as the to_unit,
        the original value is returned unchanged.
    """
    value = float(value)
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    return value


@app.route("/", methods=["GET", "POST"])
def index():
    """
    The single route of the app, which handles GET and POST requests to '/'

    If the request is a GET, it renders the 'index.html' template with no arguments.

    If the request is a POST, it retrieves three values from the form data: a temperature value 
    and two strings representing units of measurement.
    It then calls the 'convert_temperature' function with these values and 
    passes the result to the 'render_template' function as a variable.

    In either case, it returns the rendered HTML template as its response.
    """
    result = None
    if request.method == "POST":
        temperature = request.form.get("temperature")
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")

        if temperature:
            result = convert_temperature(temperature, from_unit, to_unit)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
