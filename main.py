from googleapiclient.discovery import build

from datetime import datetime, timedelta

api_key = 'AIzaSyBzSpduNBLfFRRRjbprkBaXWO_Ae8JjliQ'

youtube = build('youtube', 'v3', developerKey=api_key)

lastweek = datetime.now() - timedelta(days=7)
lastweek = lastweek.isoformat()


myChannels = [
    ['Seth Meyers', 'UCVTyTA7-g9nopHeHbeuvpRA'],
    ['Sarah Z', 'UCK-GxvzttTnNhq3JPYpXhqg'],
    ['Vihart', 'UCOGeU-1Fig3rrDjhm9Zs_wg'],
    ['Soon By You', 'UCuMGWHFZ2BmJmjisxc4WoLw'],
    ['Rational Animations', 'UCgqt1RE0k0MIr0LoyJRy2lg'],
    ['Joseph Corella', 'UC5c9Z3QsloqOsb5HS_R5RrA'],
    ['Avital Macales', 'UCaYh0q26GFn11Up6MhYDBow'],
    ['Captain Disillusion', 'UCEOXxzW2vU0P-0THehuIIeg'],
    ['John Oliver', 'UC3XTzVzaHQEd30rQbuvCtTQ'],
    ['Youngrizzze', 'UCFO7t_D3GnycNhIGixJUKPQ'],
    ['Jacob Collier', 'UCtmY49Zn4l0RMJnTWfV7Wsg'],
    ['Awkward Puppets', 'UCQG4cX86zZ51IU2cerZgPSA'],
    ['Unnecessary Inventions', 'UCB4NFn-8oipHct0IfAQBQrQ']
]

# gets all video IDs
videoIDs, videoLinks = [], []
for x in myChannels:

    # gets upload playlist from channel
    channelsListRequest = youtube.channels().list(part=['contentDetails'], id=x[1])
    channelsListResponse = channelsListRequest.execute()
    uploadsListId = channelsListResponse['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # get videos from playlist
    playlistItemsListRequest = youtube.playlistItems().list\
        (part=['snippet', 'contentDetails'], playlistId=uploadsListId, maxResults=20)
    playlistItemsListResponse = playlistItemsListRequest.execute()
    count = 0
    while count < 20:
        y = playlistItemsListResponse['items'][count]
        published = y['contentDetails']['videoPublishedAt']
        if published < lastweek:
            break
        url = "https://www.youtube.com/watch?v=" + y['contentDetails']['videoId']
        title = y['snippet']['title'] + "_" + y['snippet']['channelTitle'] + "_" + published
        videoIDs.append([url, title])
        videoLinks.append(url)
        count += 1

print(videoIDs)
print(videoLinks)
