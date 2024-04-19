# import pandas as pd
# from pydriller import Repository
#
#
# def get_commits_from_excel(file_path, repo_url, project_path):
#     # Read the Excel file into a pandas DataFrame
#     df = pd.read_excel(file_path)
#
#     commits_list = []
#     for index, row in df.iterrows():
#         commit_hash = row['Commit Hash']
#
#         # Fetch commit information using PyDriller with project path restriction
#         for commit in Repository(repo_url, path=project_path).traverse_commits():
#             if commit.hash == commit_hash:
#                 commit_info = {
#                     'Hash': commit.hash,
#                     'Author': commit.author.name,
#                     'Message': commit.msg,
#                     'Timestamp': commit.author_date
#                 }
#                 commits_list.append(commit_info)
#                 break
#     commits_df = pd.DataFrame(commits_list)
#     return commits_df
#
#
# if __name__ == "__main__":
#     file_path = "Issues_assignment1.xlsx"
#     repo_url = "https://github.com/apache/hadoop"
#     project_path = "tree/trunk/hadoop-common-project"
#     commits_df = get_commits_from_excel(file_path, repo_url, project_path)
#     #print(f"Number of commits found: {len(commits_df)}")
#     #print(commits_df.head())  # Print the first few rows of the DataFrame

from pydriller import Repository
from datetime import datetime, timedelta

def analyze_repository(repo_path):
    print("Analyzing repository: start")
    # Use PyDriller to iterate over all commits in the repository

    one_month_ago = datetime.now() - timedelta(days=1)

    for commit in Repository(repo_path, since=one_month_ago, num_workers=4, only_commits=["HADOOP-9976"]).traverse_commits():
        print(f"Commit hash: {commit.hash}")
        print(f"Author: {commit.author.name} <{commit.author.email}>")
        print(f"Date: {commit.committer_date}")
        print(f"Message: {commit.msg}")
        print(f"Files modified:")
        for modified_file in commit.modified_files:
            print(f"\t- {modified_file.filename}")

    print("Analyzing repository: end")

if __name__ == "__main__":
    repository_path = "https://github.com/apache/hadoop"
    analyze_repository(repository_path)
