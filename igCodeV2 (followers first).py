import os
import re
import time
import webbrowser
import ast

def get_txt_file():
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    if not txt_files:
        print("No .txt file found in the current directory.")
        exit()
    elif len(txt_files) > 1:
        print("Multiple .txt files found. Please ensure only one .txt file is present.")
        exit()
    return txt_files[0]

def is_date_line(line):
    return bool(re.search(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2}, \d{4}', line))

def extract_lists_from_bracketed_file(text):
    """Extract two lists (followers, following) from bracketed file format"""
    list_blocks = re.findall(r'\[(.*?)\]', text, re.DOTALL)
    if len(list_blocks) < 2:
        raise ValueError("Could not find two complete lists in bracketed format.")

    followers = ast.literal_eval(f"[{list_blocks[0]}]")
    following = ast.literal_eval(f"[{list_blocks[1]}]")
    return followers, following

def stage_1_cleaning(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        raw = file.read()

    if raw.strip().startswith('['):
        # Bracketed format
        followers, following = extract_lists_from_bracketed_file(raw)
    else:
        # Legacy format with headers
        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        clean_lines = [
            line for line in lines
            if line.lower() != "instagram"
            and line != "Profiles that you choose to see content from"
            and not is_date_line(line)
        ]
        try:
            idx_followers = clean_lines.index("Followers")
            idx_following = clean_lines.index("Following", idx_followers + 1)
        except ValueError:
            print("Could not find both 'Followers' and 'Following' headers.")
            exit()
        followers = clean_lines[idx_followers + 1:idx_following]
        following = clean_lines[idx_following + 1:]

    # Deduplicate & sort
    followers = sorted(set(followers))
    following = sorted(set(following))

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Followers\n")
        file.write('\n'.join(followers) + '\n\n')
        file.write("Following\n")
        file.write('\n'.join(following) + '\n')

    print("Stage 1 Complete ✅")
    print(f"Followers count: {len(followers)}")
    print(f"Following count: {len(following)}")
    input("Press Enter to continue to Stage 2 (Comparing)...")
    return followers, following

def stage_2_comparing(filename, followers, following):
    not_following_back = sorted(set(following) - set(followers))

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(not_following_back) + '\n')

    print("Stage 2 Complete ✅")
    print(f"Users not following back: {len(not_following_back)}")
    input("Press Enter to continue to Stage 3 (Finalising)...")
    return not_following_back

def stage_3_finalising(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        users = [line.strip() for line in file if line.strip()]

    links = [f"https://www.instagram.com/{user}/" for user in users]

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(links) + '\n')

    print("Stage 3 Complete ✅")
    print("All usernames converted to Instagram profile links.")
    input("Press Enter to continue to Stage 4 (Open Links)...")

def stage_4_open_links(filename, batch_size=20):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    for i in range(0, len(links), batch_size):
        batch = links[i:i + batch_size]
        print(f"\nOpening batch {i // batch_size + 1} ({len(batch)} links)...")
        for link in batch:
            webbrowser.open_new_tab(link)
        input("Press Enter to open the next batch...")

    print("\nStage 4 Complete ✅ All links opened.")

def main():
    filename = get_txt_file()
    followers, following = stage_1_cleaning(filename)
    users_to_check = stage_2_comparing(filename, followers, following)
    stage_3_finalising(filename)
    stage_4_open_links(filename)

if __name__ == "__main__":
    main()
