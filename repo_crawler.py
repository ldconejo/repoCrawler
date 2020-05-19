'''
Developed by ldconejo
'''
import json
import webbrowser
import os
from github import Github

def read_config_file(filename):
    '''
    Loads configuration parameters, including passwords
    '''
    with open(filename) as config_file:
        config_data = json.load(config_file)
    return config_data

def process_config_data(config_data):
    '''
    Returns username, password and organization
    '''
    access_token = config_data['user_credentials']['access_token']
    organization = config_data['organization']['name']

    # Check for optional filters
    if 'filters'in config_data:
        repo_filter = config_data['filters']['repo_filter']
    else:
        repo_filter = None

    return access_token, organization, repo_filter

def log_into_github(access_token):
    '''
    Uses access token to log into Github
    '''
    logged_user = Github(access_token)
    return logged_user

def log_into_org(logged_user, organization):
    '''
    Logs into an organization with the existing user
    '''
    logged_org = logged_user.get_organization(organization)
    return logged_org

def get_all_repos(logged_org):
    '''
    Gets a list of all repositories under an organization
    '''
    return logged_org.get_repos()

def get_open_pull_requests(repo, repo_filter):
    '''
    Returns a list of links to open pull requests for a given repository
    '''
    list_of_open_pull_requests = []
    open_pulls = repo.get_pulls(state='open', sort='created', base='master')

    if not repo_filter:
        for pull in open_pulls:
            list_of_open_pull_requests.append(pull.html_url)
    else:
        for pull in open_pulls:
            if repo_filter in pull.html_url:
                list_of_open_pull_requests.append(pull.html_url)
    return list_of_open_pull_requests



def create_html(list_of_links, filename):
    '''
    creates and opens a webpage with a list of links
    '''
    with open(filename, 'w') as output_file:
        header = """<html>
        <head>Open pull requests</head>
        <body>"""
        footer = """</body>
        </html>"""
        output_file.write(header)

        for link in list_of_links:
            new_link = f"<p><a href=\"{link}\">{link}</a></p>"
            output_file.write(new_link)

        output_file.write(footer)
        webbrowser.open('file://' + os.path.realpath(filename))

def main():
    '''
    Main execution code
    '''
    configuration_data = read_config_file('config.json')
    access_token, organization, repo_filter = process_config_data(configuration_data)
    logged_user = log_into_github(access_token)
    logged_org = log_into_org(logged_user, organization)
    org_repos = get_all_repos(logged_org)
    full_list = []
    repo_counter = 1
    for repo in org_repos:
        print(f"Working on repository #{repo_counter}")
        full_list.extend(get_open_pull_requests(repo, repo_filter))
        repo_counter += 1
    create_html(full_list, 'pending_review.html')

if __name__ == '__main__':
    main()
