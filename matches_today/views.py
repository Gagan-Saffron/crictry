from django.shortcuts import render

from datetime import date
import requests
import json

#all api calls here

def get_matches():
	print("-----Getting matches(matchlist api)-----")

	match_api_response=requests.get('https://cricapi.com/api/matches/',params={'apikey':'fDqh47WvCaSbk0C71pqZa4oEGcm2'})
	match_json_response = match_api_response.json()

	print("Processing for today's matches.....")
	
	today=date.today().strftime('%Y-%m-%d')
	matchlist=[]
	for match in match_json_response['matches']:
		
		match['team1'] = match['team-1']
		match['team2'] = match['team-2']

		match_date = match['date'].split('T')[0]

		if match_date == today:
			print(f"appending match id:{match['unique_id']} ---- {match['team-1']} vs {match['team-2']}")
			data = {
				'unique_id':match['unique_id'],
				'team1':match['team-1'],
				'team2':match['team-2'],}
			matchlist.append(data) 

	print("-----Match list extracted-----",end='\n\n')
	return matchlist,match_json_response['matches']

def get_score(match_id):
	print("-----Getting match score(Score api)-----")

	score_api_response = requests.get("https://cricapi.com/api/cricketScore/", params={'unique_id':str(match_id), 'apikey':'fDqh47WvCaSbk0C71pqZa4oEGcm2'})
	score_json_response = score_api_response.json()

	print(score_json_response['score'])
	print("-----Match score extracted-----")
	return score_json_response['score']


# Create your views here.


def home_view(request):

	matches,all_matches=get_matches()
	context={
	'matches':matches,
	'all_matches':all_matches,}

	return render(request,'homepage.html',context)

def score_view(request,unique_id):

	score = get_score(unique_id)

	context = {'score':score}

	return render(request,'scorepage.html',context)