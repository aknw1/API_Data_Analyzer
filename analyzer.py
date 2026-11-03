def analyze_posts(posts):
 if posts:
     counter={}

     for post in posts:
         user_id=post["userId"]
         if user_id in counter:
             counter[user_id]+=1
         else:
             counter[user_id] = 1
     most_active_user = max(counter, key=counter.get)

     return {
    "total_posts": len(posts),
    "user_counts": counter,
    "most_active_user": most_active_user
    }

 else:
     return None