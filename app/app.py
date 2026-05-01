from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# In-memory storage (we'll add a real DB later)
expenses = []

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "fintrack-api",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "endpoints": ["/health", "/expenses"]
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify({"expenses": expenses, "count": len(expenses)}), 200

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or 'amount' not in data or 'description' not in data:
        return jsonify({"error": "amount and description required"}), 400
    expense = {
        "id": len(expenses) + 1,
        "amount": data['amount'],
        "description": data['description'],
        "category": data.get('category', 'uncategorised'),
        "timestamp": datetime.utcnow().isoformat()
    }
    expenses.append(expense)
    return jsonify(expense), 201

@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    global expenses
    expenses = [e for e in expenses if e['id'] != expense_id]
    return jsonify({"message": "deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)