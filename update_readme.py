import feedparser
import os

# Your Medium RSS feed URL
feed_url = 'https://medium.com/feed/@vaniwalvekar'

def fetch_medium_posts(feed_url):
    try:
        feed = feedparser.parse(feed_url)
        posts = []
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            posts.append(f'- [{title}]({link})')
        return posts
    except Exception as e:
        print(f"Error fetching Medium posts: {e}")
        return []

def update_readme(posts):
    readme_path = 'README.md'
    if not os.path.exists(readme_path):
        print(f"{readme_path} does not exist.")
        return
    
    try:
        with open(readme_path, 'r') as file:
            content = file.read()
        
        # Find the placeholder and replace it with the latest posts
        start_index = content.find('<!-- BLOG-POST-LIST:START -->')
        end_index = content.find('<!-- BLOG-POST-LIST:END -->')
        
        if start_index != -1 and end_index != -1:
            new_content = (
                content[:start_index + len('<!-- BLOG-POST-LIST:START -->')] + '\n' +
                '\n'.join(posts) + '\n' +
                content[end_index:]
            )
            with open(readme_path, 'w') as file:
                file.write(new_content)
            print("README.md updated successfully.")
        else:
            print('Placeholder not found in README.md')
    except Exception as e:
        print(f"Error updating README.md: {e}")

if __name__ == '__main__':
    posts = fetch_medium_posts(feed_url)
    if posts:
        update_readme(posts)
    else:
        print("No posts to update.")
