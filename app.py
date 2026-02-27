from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
# เปิดใช้งาน CORS เพื่อให้หน้าเว็บ HTML เรียกใช้ API นี้ได้
CORS(app)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'car_project',
    'charset': 'utf8mb4'
}

@app.route('/api/search', methods=['GET'])
def search_cars():
    search_term = request.args.get('search', '')
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # ค้นหาจากยี่ห้อ รุ่น หรือคำรวม
        sql = """
            SELECT * FROM cars 
            WHERE CONCAT(brand, ' ', model) LIKE %s 
            OR brand LIKE %s 
            OR model LIKE %s
        """
        wildcard = f"%{search_term}%"
        cursor.execute(sql, (wildcard, wildcard, wildcard))
        results = cursor.fetchall()
        
        conn.close()
        
        # *** จุดที่แก้ไข ***
        # แปลงข้อมูลทศนิยม (Decimal) เป็นตัวเลข (Float) ให้ Python เข้าใจ
        for row in results:
            row['price'] = float(row['price']) if row['price'] is not None else 0
            row['type'] = row['car_type'] # แปลงชื่อตัวแปรให้ตรงกับที่ JS ใช้
            
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Server is running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)