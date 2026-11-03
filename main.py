from api  import fetch_posts
from validation import  validate_posts,filter_valid_posts
from analyzer import analyze_posts
from storage import save_posts,save_posts_csv
def main():
    result=fetch_posts()
    posts_header=["id","userId","title"]

    if result is not None:
        filter_posts=filter_valid_posts(result)
        
        if filter_posts:
            print(f"Posts retrieved: {len(result)}")
            valid_count,invalid_count=validate_posts(result)
            print(f"Valid posts: {valid_count}")
            print(f"Invalid posts: {invalid_count}")
            analysis=analyze_posts(filter_posts)
            if analysis is not None:
                print(f"Total Posts: {analysis['total_posts']}")
                print(f"User Counts: {analysis['user_counts']}")
                print(f"Most Active User: {analysis['most_active_user']}")
                save_posts_status=save_posts(filter_posts,'posts.json')
                print(f"were posts saved: {save_posts_status}")
                csv_status=save_posts_csv(filter_posts,"posts.csv",posts_header)
                print(f"CSV saved successfully: {csv_status}")
                report={
                    "total_retrieved": len(result),
                    "valid_posts": valid_count,
                    "invalid_posts": invalid_count,
                    "analysis": analysis
                    }
                report_status = save_posts(report, "report.json")
                print(f"Report saved successfully: {report_status}")
        else:
            print("Empty list")

if __name__=="__main__":
    main()