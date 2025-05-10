from flask import Blueprint, jsonify
from db import get_connection

# 犯罪地点分布柱形图(全部犯罪)

bp = Blueprint('api_crime_by_location', __name__)

@bp.route('/api/crime_by_location')
def get_crime_by_location():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Location_Description, COUNT(*) AS Crimes
        FROM ChicagoCrime
        GROUP BY Location_Description
        ORDER BY Crimes DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'location': r[0], 'count': r[1]} for r in rows
    ])
