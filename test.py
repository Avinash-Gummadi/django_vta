from youtube_search import YoutubeSearch
results = YoutubeSearch('machinelearning', max_results=1).to_dict()
print(results)
print(results[0]['id'])
