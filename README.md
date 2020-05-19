# Github Repository Crawler


Searches all pull requests within a Github organization and returns links for all open pull requests.

## Requirements

You will need to install PyGitHub

```bash
$ pip install PyGithub
```

## Configuration

Use the attached *sample_config.json* as reference. You will need to rename it as *config.json*. In order for *repo_crawler.py* to use your Github credentials, you will need to create a personal access token. The instructions to create one are listed [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

Copy your token and paste it as the value for *access_token* in *config.json*.

If you organization has many repositories you can use the value of *repo_filter* in *config.json* to limit results to those repositories whose URL contains that particular string.

**NOTE: If you don't need to filter by repository name, delete the *filters* section in *config.json*.**

## How to run

With *config.json* in the same directory, run *repo_crawler.py*. At the end, it will launch a web browser to open *pending_review.html*. 
