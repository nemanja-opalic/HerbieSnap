from mastodon import Mastodon, StreamListener
import time
from playwright.sync_api import sync_playwright

mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
    api_base_url=os.getenv("MASTODON_BASE_URL") 
)



def is_follower(user_id):
    """
    Vraća True ako korisnik sa user_id prati tvoj nalog, False inače.
    Paginacija je uključena, radi i sa velikim brojem pratilaca.
    """
    try:
        max_id = None
        while True:
            followers = mastodon.account_followers(mastodon.me()['id'], max_id=max_id, limit=80)
            if not followers:
                break
            if any(f['id'] == user_id for f in followers):
                return True
            max_id = followers[-1]['id']  # sledeća stranica
        return False
    except Exception as e:
        print("Greška pri dohvatanju followers:", e)
        return False

processed_statuses = set()


class MentionListener(StreamListener):
    def on_notification(self, notification):
        if notification['type'] != 'mention':
            return

        status = notification['status']
        status_id = status['id']

        
        if status_id in processed_statuses:
            return
        
        processed_statuses.add(status_id)

        user_id = status['account']['id']

        
        if not is_follower(user_id):
                
                return
        
       
        reply_to_id = status['in_reply_to_id']
        
        if reply_to_id != None:
                parent_status = mastodon.status(status['in_reply_to_id'])
                parent_url = parent_status['url']
                
                with sync_playwright() as p:
                     browser = p.chromium.launch(headless=True)
                     page = browser.new_page()
                     page.goto(parent_url)
                     time.sleep(7)
                     page.screenshot(path="example.png")
                     browser.close()
                     mastodon.status_post(
                         status=f"@{status['account']['acct']} Here is your screenshot and toot's URL:{parent_url}",
                         visibility="direct",
                         media_ids=[mastodon.media_post("example.png")]
                     )
        else:
               print("Nista")
           
            
            
mastodon.stream_user(MentionListener())




