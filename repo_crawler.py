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
    print(config_data)

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

if __name__ == '__main__':
    read_config_file('config.json')