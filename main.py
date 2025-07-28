from github import Github
import secret_stuff as s

def check_latest_github_version(current_version, token=None):
    try:
        g = Github(token) if token else Github()
        repo = g.get_repo(f"TTVMrGeo/Streamdeck-App")
        latest_release = repo.get_latest_release()
        print("a")
        
        if latest_release.tag_name != current_version:
            print(f"Update available: {latest_release.tag_name}")
            return False
        print("You're up to date!")
        return True
    except Exception as e:
        print(f"Error checking version: {e}")
        return False
    
print(check_latest_github_version("v0.0.1", token=s.GITHUB_TOKEN))