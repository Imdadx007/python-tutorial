import json

# GitHub profile setup script by Imdadullah
# This script creates and manages my GitHub profile details

def main():
    print("=" * 45)
    print("My GitHub Profile Setup")
    print("=" * 45)
    print()
    
    # Get user input
    user_info = {}
    
    user_info['username'] = input("GitHub username: ")
    user_info['full_name'] = input("Full name: ")
    user_info['email'] = input("Email: ")
    user_info['bio'] = input("Bio: ")
    skills_input = input("Skills (comma-separated): ")
    user_info['skills'] = [s.strip() for s in skills_input.split(',')]
    user_info['projects'] = input("Number of projects: ")
    user_info['repository'] = "python-tutorial"
    
    # Show what we got
    print("\n" + "-" * 45)
    print("Profile Details")
    print("-" * 45)
    print(f"Username: {user_info['username']}")
    print(f"Name: {user_info['full_name']}")
    print(f"Email: {user_info['email']}")
    print(f"Bio: {user_info['bio']}")
    print(f"Skills: {', '.join(user_info['skills'])}")
    print(f"Projects: {user_info['projects']}")
    print(f"Repository: {user_info['repository']}")
    
    # Save it to file
    try:
        with open('github_profile.json', 'w') as f:
            json.dump(user_info, f, indent=4)
        print("\n✓ Saved to github_profile.json")
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")

if __name__ == "__main__":
    main()