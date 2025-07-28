def update_checker():
    from secret_stuff import OWNER, REPO, GITHUB_TOKEN, VERSION
    import requests, os

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    def check_latest_github_version(current_version):
        try:
            response = requests.get(url)
            response.raise_for_status()
            latest_release = response.json()
            latest_version = latest_release['tag_name']
            
            if latest_version != current_version:
                print(f"New version available: {latest_version} (Current: {current_version})")
                update = input("Should I update it for you? (Y/N)")
                if update == "Y" or update == "y":
                    try:
                        os.system('git pull master master')
                    except Exception as e:
                        return f"Eroor: {e}"
                else:
                    return("Ok :/")

            print("You have the latest version!")
            return True
        except Exception as e:
            print(f"Error checking version: {e}")
            return False
        
    print(check_latest_github_version(VERSION))

print(update_checker())