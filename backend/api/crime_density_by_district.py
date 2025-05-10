from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('crime_density_by_district', __name__)

# 犯罪密度分布柱形图(按地区)

@bp.route('/api/crime_density_by_district')
def get_crime_density_by_district():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT District, COUNT(*) AS Crimes,
            ROUND(COUNT(*) * 1.0 / (SELECT COUNT(*) FROM ChicagoCrime), 4) AS Density
        FROM ChicagoCrime
        GROUP BY District
        ORDER BY Crimes DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'district': r[0], 'crimes': r[1], 'density': r[2]} for r in rows
    ])
