import requests, json, secret_stuff

def check_latest_version(current_version):
    repo_owner = "TTVMrGeo"
    repo_name = "Streamdeck-App"
    
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release['tag_name']
        
        if latest_version != current_version:
            print(f"New version available: {latest_version} (Current: {current_version})")
            return False
        print("You have the latest version!")
        return True
    except Exception as e:
        print(f"Error checking version: {e}")
        return False

# Example usage
check_latest_version("v1.0.0")