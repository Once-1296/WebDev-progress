from fastapi import FastAPI
import requests

app = FastAPI()

header = {"User-Agent": "Web Agent", "Content-Type": "application/json"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/leetcode_profile/{username}")
async def get_profile_stats(username: str):
    api_url = "https://leetcode.com/graphql"
    data = {
        "query": "\n    query userPublicProfile($username: String!) {\n  matchedUser(username: $username) {\n    contestBadge {\n      name\n      expired\n      hoverText\n      icon\n    }\n    username\n    githubUrl\n    twitterUrl\n    linkedinUrl\n    profile {\n      ranking\n      userAvatar\n      realName\n      aboutMe\n      school\n      websites\n      countryName\n      company\n      jobTitle\n      skillTags\n      postViewCount\n      postViewCountDiff\n      reputation\n      reputationDiff\n      solutionCount\n      solutionCountDiff\n      categoryDiscussCount\n      categoryDiscussCountDiff\n    }\n  }\n}\n    ",
        "variables": {"username": username},
        "operationName": "userPublicProfile",
    }
    response = requests.post(api_url, headers=header, json=data).json()
    #print(response)
    return response


@app.get("/leetcode_contest_stats/{username}")
async def get_contest_stats(username: str):
    api_url = "https://leetcode.com/graphql"
    data = {
        "query": "\n  query userContestRankingInfo($username: String!) {\n  userContestRanking(username: $username) {\n    attendedContestsCount\n    rating\n    globalRanking\n    totalParticipants\n    topPercentage\n    badge {\n      name\n    }\n  }\n  userContestRankingHistory(username: $username) {\n    attended\n    trendDirection\n    problemsSolved\n    totalProblems\n    finishTimeInSeconds\n    rating\n    ranking\n    contest {\n      title\n      startTime\n    }\n  }\n}\n    ",
        "variables": {"username": username},
        "operationName": "userContestRankingInfo",
    }
    response = requests.post(api_url, headers=header, json=data).json()
    #print(response)
    return response
