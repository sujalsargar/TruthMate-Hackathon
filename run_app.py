import subprocess
import sys
import os
import time
import webbrowser

def run_truthmate():
    """Run both frontend and backend together"""
    
    # Get absolute paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_path = os.path.join(current_dir, "truthmate-backend")
    frontend_path = os.path.join(current_dir, "truthmate-frontend")
    venv_python = os.path.join(backend_path, "venv", "Scripts", "python.exe")
    
    print("=" * 60)
    print("🚀 Starting TruthMate Application...")
    print("=" * 60)
    print(f"📂 Current directory: {current_dir}")
    print(f"📂 Backend path: {backend_path}")
    print(f"📂 Frontend path: {frontend_path}")
    print("=" * 60)
    
    # Check backend exists
    if not os.path.exists(backend_path):
        print(f"❌ Error: Backend folder not found at: {backend_path}")
        print("Please create truthmate-backend folder")
        return
    
    # Check frontend exists
    if not os.path.exists(frontend_path):
        print(f"❌ Error: Frontend folder not found at: {frontend_path}")
        print("Creating frontend folder...")
        try:
            os.makedirs(frontend_path, exist_ok=True)
            print(f"✅ Created: {frontend_path}")
            print("⚠️  Please add index.html to truthmate-frontend folder")
            return
        except Exception as e:
            print(f"❌ Could not create folder: {e}")
            return
    
    # Check index.html exists
    index_path = os.path.join(frontend_path, "index.html")
    if not os.path.exists(index_path):
        print(f"❌ Error: index.html not found at: {index_path}")
        print("⚠️  Please create index.html in truthmate-frontend folder")
        return
    
    try:
        # Start backend
        print("\n📦 Starting Backend on http://localhost:5000...")
        backend_process = subprocess.Popen(
            [str(venv_python), "app.py"],
            cwd=str(backend_path),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        
        # Wait for backend to start
        time.sleep(3)
        
        # Start frontend
        print("🌐 Starting Frontend on http://localhost:8000...")
        frontend_process = subprocess.Popen(
            [sys.executable, "-m", "http.server", "8000"],
            cwd=str(frontend_path),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        
        print("\n" + "=" * 60)
        print("✅ TruthMate is now running!")
        print("=" * 60)
        print("📱 Frontend: http://localhost:8000")
        print("🔌 Backend:  http://localhost:5000")
        print("💾 Database: truthmate-backend/truthmate.db (auto-created)")
        print("\n⚠️  Close both console windows to stop")
        print("=" * 60 + "\n")
        
        # Open browser
        time.sleep(2)
        webbrowser.open("http://localhost:8000")
        
        print("✅ Browser opened automatically!")
        print("✅ Check the new console windows for logs")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    run_truthmate()