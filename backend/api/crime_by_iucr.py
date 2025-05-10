from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_by_iucr', __name__)

# 犯罪类型分布柱形图(全部犯罪)

@bp.route('/api/crime_by_iucr')
def get_crime_by_iucr():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT IUCR, Primary_Type, COUNT(*) AS Crimes
        FROM ChicagoCrime
        GROUP BY IUCR, Primary_Type
        ORDER BY Crimes DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'iucr': r[0], 'type': r[1], 'count': r[2]} for r in rows
    ])
