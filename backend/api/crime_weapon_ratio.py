from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('api_crime_weapon_ratio', __name__)

# 犯罪类型与武器使用比例柱形图(全部犯罪)

@bp.route('/api/crime_weapon_ratio')
def get_crime_weapon_ratio():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            Primary_Type,
            COUNT(*) AS Total_Crimes,
            SUM(CASE WHEN Description ILIKE '%WEAPON%' THEN 1 ELSE 0 END) AS Weapon_Crimes,
            ROUND(SUM(CASE WHEN Description ILIKE '%WEAPON%' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Weapon_Percentage
        FROM ChicagoCrime
        GROUP BY Primary_Type
        HAVING COUNT(*) > 1000
        ORDER BY Weapon_Percentage DESC
        LIMIT 5;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {
            'type': r[0],
            'total': r[1],
            'weapon_crimes': r[2],
            'weapon_percentage': r[3]
        } for r in rows
    ])
