from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint("case_resolution_time_by_year", __name__)

@bp.route("/api/case_resolution_time_by_year")
def case_resolution_time_by_year():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Year, 
               ROUND(AVG(EXTRACT(EPOCH FROM (Updated_On - Date))/86400), 2) AS Avg_Days
        FROM ChicagoCrime
        GROUP BY Year
        ORDER BY Year;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    data = [{"year": int(r[0]), "avg_days": float(r[1])} for r in rows]
    return jsonify(data)
