from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_by_year', __name__)

# 犯罪年分布柱形图(全部犯罪)

@bp.route('/api/crime_by_year')
def get_crime_by_year():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Year, COUNT(*) 
        FROM ChicagoCrime 
        GROUP BY Year 
        ORDER BY Year;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'year': int(r[0]), 'count': r[1]} for r in rows])