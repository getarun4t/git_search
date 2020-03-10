#Page for Gist details, create and update

class details():
    description = "gist[description]"
    filename = "gist[contents][][name]"
    create = "//button[contains(.,'Create public gist')]"
    update = "//button[contains(.,'Update public gist')]"
    update_secret = "//button[@type='submit'][contains(.,'Update secret gist')]"
    code = "CodeMirror-code"
    private_create = "//button[contains(.,'Create secret gist')]"
