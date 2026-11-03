def validate_post(post):
    if isinstance(post,dict):
        if all(key in post for key in ("id", "userId", "title")):
            if isinstance(post["id"],int) and isinstance(post["userId"],int) and isinstance(post["title"],str):
                    return True
            else:
                    return False
    return False

def validate_posts(posts):
     if isinstance(posts,list):
        valid_post=0
        invalid_post=0
        for post in posts:
            checked=validate_post(post)
            if checked:
                valid_post+=1
            else:
                invalid_post+=1
        return valid_post, invalid_post

     else:
          return None

def filter_valid_posts(posts):
    if posts is not None:
        if posts:
            filter_posts=[]
            for post in posts:
                if validate_post(post):
                    filter_posts.append(post)
            return filter_posts
        else:
            print("Empty list")
    else:
        print("No  posts available to filter.")