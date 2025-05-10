from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('type_hour_bar', __name__)

@bp.route('/api/type_hour_bar')
def type_hour_bar():
    conn = get_connection()
    cur = conn.cursor()

    # 仅取出现次数最多的前 5 类犯罪
    cur.execute("""
        WITH TopTypes AS (
            SELECT Primary_Type
            FROM ChicagoCrime
            GROUP BY Primary_Type
            ORDER BY COUNT(*) DESC
            LIMIT 5
        )
        SELECT Primary_Type, EXTRACT(HOUR FROM Date) AS Hour, COUNT(*) AS Crimes
        FROM ChicagoCrime
        WHERE Primary_Type IN (SELECT Primary_Type FROM TopTypes)
        GROUP BY Primary_Type, Hour
        ORDER BY Hour, Primary_Type;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = {}
    for primary_type, hour, crimes in rows:
        hour = int(hour)
        if hour not in result:
            result[hour] = {}
        result[hour][primary_type] = crimes

    # 统一输出格式：每小时一个对象，包含不同类型的数量（没有的为 0）
    hours = list(range(24))
    types = list(set([row[0] for row in rows]))
    formatted = []
    for h in hours:
        obj = {"hour": h}
        for t in types:
            obj[t] = result.get(h, {}).get(t, 0)
        formatted.append(obj)

    return jsonify(formatted)
