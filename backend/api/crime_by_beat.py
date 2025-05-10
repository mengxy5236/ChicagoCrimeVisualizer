from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_by_beat', __name__)

# 犯罪地点(按beat地区)分布柱形图

@bp.route('/api/crime_by_beat')
def get_crime_by_beat():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Beat, COUNT(*) AS Crimes
        FROM ChicagoCrime
        GROUP BY Beat
        ORDER BY Crimes DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {
            'beat': r[0],
            'count': r[1]
        } for r in rows
    ])
