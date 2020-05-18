'''
Developed by ldconejo
'''
from github import Github
import json

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
    access_token= config_data['user_credentials']['access_token']
    organization = config_data['organization']['name']
    return access_token, organization

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
    logged_org.login
    return logged_org

def get_all_repos(logged_org):
    '''
    Gets a list of all repositories under an organization
    '''
    return logged_org.get_repos()

def get_open_pull_requests(repo):
    '''
    Returns a list of links to open pull requests for a given repository
    '''
    open_pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pull in open_pulls:
        print(pull.html_url)


def create_html(list_of_links):
    '''
    creates and opens a webpage with a list of links 
    '''
    pass

def main():
    '''
    Main execution code
    '''
    configuration_data = read_config_file('config.json')
    access_token, organization = process_config_data(configuration_data)
    logged_user = log_into_github(access_token)
    logged_org = log_into_org(logged_user, organization)
    org_repos = get_all_repos(logged_org)
    for repo in org_repos:
        get_open_pull_requests(repo)


if __name__ == '__main__':
    main()
    