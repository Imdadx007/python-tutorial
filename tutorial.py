import json

import json

# GitHub profile setup script by Imdadullah

def get_skills():
    skills_input = input("Skills (comma-separated): ")
    return [s.strip() for s in skills_input.split(',') if s.strip()]

def save_json(data):
    try:
        with open('github_profile.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("\n✓ Data saved to github_profile.json")
    except Exception as e:
        print(f"\n✗ Error saving JSON: {e}")

def save_readme(data):
    try:
        with open('PROFILE.md', 'w') as f:
            f.write(f"# {data['full_name']}\n\n")
            f.write(f"**Username:** {data['username']}\n\n")
            f.write(f"**Bio:** {data['bio']}\n\n")
            f.write("## Skills\n")
            for skill in data['skills']:
                f.write(f"- {skill}\n")
            f.write(f"\nProjects: {data['projects']}\n")
        print("✓ PROFILE.md generated")
    except Exception as e:
        print(f"✗ Error creating README: {e}")

def main():
    print("=" * 45)
    print("GitHub Profile Setup Script")
    print("=" * 45)

    user_info = {}

    user_info['username'] = input("GitHub username: ")
    user_info['full_name'] = input("Full name: ")
    user_info['email'] = input("Email: ")
    user_info['bio'] = input("Bio: ")
    user_info['skills'] = get_skills()
    user_info['projects'] = input("Number of projects: ")
    user_info['repository'] = "python-tutorial"

    print("\n--- Profile Preview ---")
    print(f"Name: {user_info['full_name']}")
    print(f"Bio: {user_info['bio']}")
    print(f"Skills: {', '.join(user_info['skills'])}")

    save_json(user_info)
    save_readme(user_info)

if __name__ == "__main__":
    main()