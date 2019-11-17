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
    import pdb; pdb.set_trace()

    #result = user_client.reminders_add(user=users['thecbsnetwork'],
                                       #text='eat yer veggies',
                                       #time='1 minute')

    # can only send to channels which are public, unless maybe we can
    # do it if the bot is invited to the private channel? may need
    # groups:read permission?
    result = user_client.reminders_add(channel=channels['automaters'],
                                       text='eat yer veggies',
                                       time='1 minute')
    print(result.data)


if __name__ == '__main__':
    main()
