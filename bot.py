def run():
    # Import the requests module for send a PUT request
    import requests
    # Import the base64 module for encoding a file to base64
    import base64     githubAPIURL = "https://api.github.com/repos/testmonlau02/test/contents/my-local-image"
    # Replace "bracketcounters" with your username, replace "test-repo" with your repository name and replace "new-image.png" with the filename you want to upload from local to GitHub.     # Paste your API token here
    githubToken = "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" 
    with open("my-local-image.jpg", "rb") as f:
        # Encoding "my-local-image.jpg" to base64 format
        encodedData = base64.b64encode(f.read())         headers = {
            "Authorization": f'''Bearer {githubToken}''',
            "Content-type": "application/vnd.github+json"
        }
        data = {
            "message": "My commit message", # Put your commit message here.
            "content": encodedData.decode("utf-8")
        }         r = requests.put(githubAPIURL, headers=headers, json=data)
        print(r.text) # Printing the response
    exit()
