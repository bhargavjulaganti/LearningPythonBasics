from requests_html import HTMLSession

# create the session
session = HTMLSession()

# define our URL
url = 'https://www.youtube.com/c/vahrehvah/videos'

# use the session to get the data
r = session.get(url)

i = 1
while i < 10:
  print(i)

  r.html.render(sleep=1, keep_page=True, scrolldown=i)

  videos = r.html.find('#video-title')

  for item in videos:
      video = {
          'title': item.text,
          'link': item.absolute_links
      }
      print(video)
  i += 1


# Run below command if the chrome driver does not start

# bash /Applications/Python*/Install\ Certificates.command
#  -- pip install --upgrade certifi

