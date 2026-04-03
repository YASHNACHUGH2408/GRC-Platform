from app import create_app
from background_simulator import start_bot_thread # <--- Import kiya

app = create_app()

if __name__ == '__main__':
    # Bot start kar diya bhai!
    start_bot_thread()
    
    # Flask server start
    print("✅ GRC Platform started with Auto-Simulation...")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)