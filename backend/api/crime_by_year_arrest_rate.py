from flask import Blueprint, jsonify
from db import get_connection

# 犯罪地点分布柱形图(全部犯罪)

bp = Blueprint('api_crime_by_year_arrest_rate', __name__)

@bp.route('/api/crime_by_year_arrest_rate')
def get_crime_by_year_arrest_rate():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Year,
            COUNT(*) AS Total_Crimes,
            SUM(CASE WHEN Arrest THEN 1 ELSE 0 END) AS Arrests,
            ROUND(SUM(CASE WHEN Arrest THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Arrest_Rate
        FROM ChicagoCrime
        GROUP BY Year
        ORDER BY Year;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([
        {'year': r[0], 'arrest_rate': r[3]} for r in rows
    ])
