from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_by_weekday', __name__)

# 犯罪周内分布柱形图(全部犯罪)

@bp.route('/api/crime_by_weekday')
def get_crime_by_weekday():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT EXTRACT(DOW FROM Date) AS weekday_num, 
               TO_CHAR(Date, 'FMDay') AS weekday_name, 
               COUNT(*) AS crimes
        FROM ChicagoCrime 
        GROUP BY weekday_num, weekday_name 
        ORDER BY weekday_num;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'weekday': r[1].strip(), 'count': r[2]} for r in rows
    ])