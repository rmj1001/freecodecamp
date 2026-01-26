** start of main.py **

def add_setting(settings, new):
    key, value = (item.lower() for item in new)
    
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new):
    key, value = (item.lower() for item in new)

    if key not in settings.keys():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    key = key.lower()

    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    string = "Current User Settings:\n"

    for key in settings:
        string += f"{key.title()}: {settings[key]}\n"
    
    return string

    
test_settings = {
    "brightness": 80,
    "volume": 57,
    "screen_mode": "dark",
    "theme": "dark"
}


** end of main.py **

