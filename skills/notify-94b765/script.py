import os
import json
import sys

def main():
    try:
        inputs = os.environ.get("INPUT_JSON")
        if inputs:
            data = json.loads(inputs)
        else:
            data = {
                "message": os.environ.get("INPUT_MESSAGE", "")
            }
        
        print(json.dumps({"status": "notified", "message": data.get("message")}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
