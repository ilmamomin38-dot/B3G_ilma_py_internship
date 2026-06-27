default_setting={
    "theme": "light",
    "language": "English",
    "notifications":True
}

user_settings={
    "theme": "dark",
    "notificatins":False
}

final_settings=default_setting.copy()
final_settings.update(user_settings)

print("Final settings:")
print(final_settings)
