""" this module tests reminders using the various oauth tokens for slack """
import slack
import json

def get_all_users(client):
    users = client.users_list().data['members']
    users_by_name = {}
    for user in users:
        users_by_name[user['name']] = user['id']
    return users_by_name


def get_all_channels(client):
    channels = client.channels_list().data['channels']
    channels_by_name = {}
    for channel in channels:
        channels_by_name[channel['name']] = channel['id']
    return channels_by_name


def main():
    with open('auth.json') as fp:
        config = json.load(fp)
    user_client = slack.WebClient(token=config['user_token'])
    bot_client = slack.WebClient(token=config['bot_token'])

    users = get_all_users(bot_client)
    channels = get_all_channels(user_client)

    messages = user_client.channels_history(channel=channels['n-seattle-nerds'])

    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
