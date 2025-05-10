from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint("crime_by_month", __name__)

# 犯罪月份分布柱形图(全部犯罪)

@bp.route("/api/crime_by_month")
def crime_by_month():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT EXTRACT(MONTH FROM Date) AS Month, COUNT(*) AS Crimes
        FROM ChicagoCrime
        GROUP BY Month
        ORDER BY Crimes DESC;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    data = [{"month": int(row[0]), "count": row[1]} for row in rows]
    return jsonify(data)
