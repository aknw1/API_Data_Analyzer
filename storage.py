import json,csv

def save_posts(posts,filename):
    try:
        with open(filename,"w", encoding='utf-8'
                  ) as file:
            json.dump(posts,file,indent=4)
            return True
    except (OSError, TypeError, ValueError) as error:
        print(f"Could not save posts: {error}")
        return False
    
def save_posts_csv(posts, filename,header_posts):
    try:
        with open(filename,"w",newline="", encoding='utf-8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=header_posts, delimiter=';' ,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(posts)
    
    except (OSError, ValueError, TypeError) as error:
        print(f"Could not save CSV: {error}")
        return False

    return True