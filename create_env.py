import os

def create_env_file():
    print("--- Environment Variable Setup ---")
    print("Please enter the values for the following variables.\n")

    # လိုအပ်သော Variable များ စာရင်း
    variables = [
        "API_ID",
        "API_HASH",
        "BOT_TOKEN",
        "MONGO_DB_URI",
        "OWNER_ID",
        "STRING_SESSION",
        "LOGGER_ID",
        "HEROKU_APP_NAME",
        "HEROKU_API_KEY",
        "UPSTREAM_REPO",
        "UPSTREAM_BRANCH",
        "GIT_TOKEN",
        "SUPPORT_CHANNEL",
        "SUPPORT_CHAT"
    ]

    env_content = ""

    for var in variables:
        value = input(f"Enter {var}: ").strip()
        # Value မထည့်ခဲ့ရင် အလွတ်ထားခဲ့မည် (သို့) Default ပေးနိုင်သည်
        env_content += f"{var}={value}\n"

    # .env ဖိုင်သို့ သိမ်းဆည်းခြင်း
    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        print("\n✅ .env file created successfully!")
        print("You can now start your bot.")
    except Exception as e:
        print(f"\n❌ Error creating .env file: {e}")

if __name__ == "__main__":
    create_env_file()
