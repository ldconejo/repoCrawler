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
    org = logged_user.get_organization(organization)
    org.login
    for pull in org.get_repos():
        print(pull.name)



def get_all_repos(organization):
    '''
    Gets a list of all repositories under an organization
    '''
    pass

def get_open_pull_requests(repo):
    '''
    Returns a list of links to open pull requests for a given repository
    '''
    pass

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
    log_into_org(logged_user, organization)


if __name__ == '__main__':
    main()
    