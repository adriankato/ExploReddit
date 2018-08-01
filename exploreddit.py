import praw

DISCOVERED_SUBREDDIT = []


# Insert OAuth2 credentials
reddit = praw.Reddit(client_id="",
                    client_secret="M",
                    username="",
                    password="",
                    user_agent="")

def main(): 
    while True:
        #Return a random subreddit
        randomsub = str(reddit.random_subreddit(nsfw=False))
        subreddit = reddit.subreddit(randomsub)
        submissions = subreddit.hot(limit=25)
    
        if str(subreddit).lower() not in DISCOVERED_SUBREDDIT:
            # Make sure you don't visit the same subreddit
            DISCOVERED_SUBREDDIT.append(str(subreddit).lower())
            print(10*'=')
            print("Subreddit Title: ", str(subreddit))
            userInputSubreddit = input("Would you like to explore this subreddit? [y/n]: ")
            if userInputSubreddit == 'y':
                displaySubmissions(submissions)
            elif userInputSubreddit == 'n':
                print("Smart choice. Spend your time wisely.")
            else:
                print("Invalid input")
        else:
            print("Stumbled on discovered content.")
        
        
        userInputLoop = input("\nWould you like to continue your voyage through the depths of reddit? [y/n]: ")
        if userInputLoop == 'y':
            continue
        else:
            break

def displaySubmissions(submissions):
    # Run through the submissions in the newly discovered subreddit
    for submission in submissions:
        # Make sure the submission isn't stickied/pinned        
        if not submission.stickied:
            print("\nSubmission Title: {}, Upvotes: {}".format(submission.title, submission.ups))
            userInputComment = input("Would you like to see the comments? [y/n]: ")
            if userInputComment == 'y':
                displayComments(submission)
            else:
                print("You dodged a bullet.")
            
            userInputSubmission = input("\nWould you like to see the next submission? [y/n]: ")
            if userInputSubmission == 'y':
                continue
            else:
                break
        else:
            continue

def displayComments(submission):
    # Run through the comments
    for comment in submission.comments.list():
        print(10*'-')
        print("Parent ID: ", comment.parent())
        print("Comment ID: ", comment.id)
        print("Upvotes: ", comment.score)
        print("Comment: ", comment.body)

if __name__ == '__main__':
    main()