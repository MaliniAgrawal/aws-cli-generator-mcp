import requests

def generate_cli_command(input_text):
    url = "http://localhost:5000/mcp/generate-cli"
    payload = {"input": input_text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["command"], data["explanation"]
    else:
        return None, response.text

def main():
    print("🧠 MCP CLI Generator (Local Interactive)")
    try:
        total = int(input("How many AWS CLI commands do you want to generate? "))
    except ValueError:
        print("❌ Invalid number. Exiting.")
        return

    for i in range(total):
        print(f"\n[{i+1}/{total}] Describe your AWS task (natural language):")
        user_input = input("➤ ").strip()
        if not user_input:
            print("⚠️ Skipping empty input.")
            continue

        cli, explanation = generate_cli_command(user_input)
        if cli:
            print("✅ CLI Command:", cli)
            print("💡 Explanation:", explanation)
        else:
            print("❌ Error:", explanation)

    print("\n🎉 Done! Thank you for using MCP CLI Generator.")

if __name__ == "__main__":
    main()
