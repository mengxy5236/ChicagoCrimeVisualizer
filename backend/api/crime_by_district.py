from flask import Blueprint, jsonify
from db import get_connection

bp = Blueprint('crime_by_district', __name__)

@bp.route('/api/crime_by_district', methods=['GET'])
def crime_by_district():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT District,
        ROUND(SUM(CASE WHEN Arrest THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Arrest_Rate
    FROM ChicagoCrime
    GROUP BY District
    ORDER BY Arrest_Rate DESC
    LIMIT 5;
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Prepare the response data
    data = [{'district': row[0], 'arrest_rate': row[1]} for row in result]
    
    cursor.close()
    conn.close()
    
    return jsonify(data)
