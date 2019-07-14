def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', fields='physics')
print(user_profile)

user_profile = build_profile('ahmad', 'irfan', job='python developer', age=32)
print(user_profile)

user_profile = build_profile('ahmad', 'ikram', location='kuantan', fields='engineering', martial_status='married')
print(user_profile)