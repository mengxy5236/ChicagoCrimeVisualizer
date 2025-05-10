from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_by_time_of_day', __name__)

# 犯罪日内时段分布柱形图(全部犯罪)

@bp.route('/api/crime_by_time_of_day')
def get_crime_by_time_of_day():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT EXTRACT(HOUR FROM Date) AS hour, COUNT(*) AS crimes
        FROM ChicagoCrime
        GROUP BY hour
        ORDER BY hour;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'time_of_day': r[0], 'count': r[1]} for r in rows
    ])
