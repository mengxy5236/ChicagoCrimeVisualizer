from flask import Flask
from flask_cors import CORS
from api import crime_by_year,crime_by_weekday,crime_by_year_theft,crime_by_time_of_day,crime_arrest_rate,crime_density_by_district,crime_by_location,crime_by_year_arrest_rate,crime_by_iucr,crime_weapon_ratio,crime_by_beat,case_resolution_time_by_year,crime_by_month,type_hour_bar,crime_by_district


app = Flask(__name__)

# 注册蓝图
app.register_blueprint(crime_by_year.bp)
app.register_blueprint(crime_by_weekday.bp)
app.register_blueprint(crime_by_year_theft.bp)
app.register_blueprint(crime_by_time_of_day.bp)
app.register_blueprint(crime_arrest_rate.bp)
app.register_blueprint(crime_density_by_district.bp)
app.register_blueprint(crime_by_location.bp)
app.register_blueprint(crime_by_year_arrest_rate.bp)
app.register_blueprint(crime_by_iucr.bp)
app.register_blueprint(crime_weapon_ratio.bp)
app.register_blueprint(crime_by_beat.bp)
app.register_blueprint(case_resolution_time_by_year.bp)
app.register_blueprint(crime_by_month.bp)
app.register_blueprint(type_hour_bar.bp)
app.register_blueprint(crime_by_district.bp)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)