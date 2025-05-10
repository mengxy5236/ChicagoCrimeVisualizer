from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_arrest_rate', __name__)

# 犯罪类型逮捕率柱形图(全部犯罪)

@bp.route('/api/crime_arrest_rate')
def get_crime_arrest_rate():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Primary_Type, 
            COUNT(*) AS Total_Crimes,
            SUM(CASE WHEN Arrest THEN 1 ELSE 0 END) AS Arrests,
            ROUND(SUM(CASE WHEN Arrest THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS Arrest_Rate
        FROM ChicagoCrime
        GROUP BY Primary_Type
        HAVING COUNT(*) > 1000
        ORDER BY Arrest_Rate DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {
            'type': r[0],
            'total': r[1],
            'arrests': r[2],
            'rate': r[3]
        }
        for r in rows
    ])
