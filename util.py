#Step 1: Importing the libraries
import re
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sb
import itertools
import random as rd
from collections import defaultdict
import ast
import networkx as nx
pd.options.mode.chained_assignment = None  # default='warn'
from textblob import TextBlob
from datetime import datetime
from datetime import timedelta

#Create emojis and num_emojis
def create_emojis(df):
    emoji_list = [':bowtie:', ':smile:', ':simple_smile:', ':laughing:', ':blush:', ':smiley:', ':relaxed:', ':smirk:', ':heart_eyes:', ':kissing_heart:', ':kissing_closed_eyes:', ':flushed:', ':relieved:', ':satisfied:', ':grin:', ':wink:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue_closed_eyes:', ':grinning:', ':kissing:', ':kissing_smiling_eyes:', ':stuck_out_tongue:', ':sleeping:', ':worried:', ':frowning:', ':anguished:', ':open_mouth:', ':grimacing:', ':confused:', ':hushed:', ':expressionless:', ':unamused:', ':sweat_smile:', ':sweat:', ':disappointed_relieved:', ':weary:', ':pensive:', ':disappointed:', ':confounded:', ':fearful:', ':cold_sweat:', ':persevere:', ':cry:', ':sob:', ':joy:', ':astonished:', ':scream:', ':neckbeard:', ':tired_face:', ':angry:', ':rage:', ':triumph:', ':sleepy:', ':yum:', ':mask:', ':sunglasses:', ':dizzy_face:', ':imp:', ':smiling_imp:', ':neutral_face:', ':no_mouth:', ':innocent:', ':alien:', ':yellow_heart:', ':blue_heart:', ':purple_heart:', ':heart:', ':green_heart:', ':broken_heart:', ':heartbeat:', ':heartpulse:', ':two_hearts:', ':revolving_hearts:', ':cupid:', ':sparkling_heart:', ':sparkles:', ':star:', ':star2:', ':dizzy:', ':boom:', ':collision:', ':anger:', ':exclamation:', ':question:', ':grey_exclamation:', ':grey_question:', ':zzz:', ':dash:', ':sweat_drops:', ':notes:', ':musical_note:', ':fire:', ':hankey:', ':poop:', ':shit:', ':+1:', ':thumbsup:', ':-1:', ':thumbsdown:', ':ok_hand:', ':punch:', ':facepunch:', ':fist:', ':v:', ':wave:', ':hand:', ':raised_hand:', ':open_hands:', ':point_up:', ':point_down:', ':point_left:', ':point_right:', ':raised_hands:', ':pray:', ':point_up_2:', ':clap:', ':muscle:', ':metal:', ':fu:', ':runner:', ':running:', ':couple:', ':family:', ':two_men_holding_hands:', ':two_women_holding_hands:', ':dancer:', ':dancers:', ':ok_woman:', ':no_good:', ':information_desk_person:', ':raising_hand:', ':bride_with_veil:', ':person_with_pouting_face:', ':person_frowning:', ':bow:', ':couplekiss:', ':couple_with_heart:', ':massage:', ':haircut:', ':nail_care:', ':boy:', ':girl:', ':woman:', ':man:', ':baby:', ':older_woman:', ':older_man:', ':person_with_blond_hair:', ':man_with_gua_pi_mao:', ':man_with_turban:', ':construction_worker:', ':cop:', ':angel:', ':princess:', ':smiley_cat:', ':smile_cat:', ':heart_eyes_cat:', ':kissing_cat:', ':smirk_cat:', ':scream_cat:', ':crying_cat_face:', ':joy_cat:', ':pouting_cat:', ':japanese_ogre:', ':japanese_goblin:', ':see_no_evil:', ':hear_no_evil:', ':speak_no_evil:', ':guardsman:', ':skull:', ':feet:', ':lips:', ':kiss:', ':droplet:', ':ear:', ':eyes:', ':nose:', ':tongue:', ':love_letter:', ':bust_in_silhouette:', ':busts_in_silhouette:', ':speech_balloon:', ':thought_balloon:', ':feelsgood:', ':finnadie:', ':goberserk:', ':godmode:', ':hurtrealbad:', ':rage1:', ':rage2:', ':rage3:', ':rage4:', ':suspect:', ':trollface:', ':sunny:', ':umbrella:', ':cloud:', ':snowflake:', ':snowman:', ':zap:', ':cyclone:', ':foggy:', ':ocean:', ':cat:', ':dog:', ':mouse:', ':hamster:', ':rabbit:', ':wolf:', ':frog:', ':tiger:', ':koala:', ':bear:', ':pig:', ':pig_nose:', ':cow:', ':boar:', ':monkey_face:', ':monkey:', ':horse:', ':racehorse:', ':camel:', ':sheep:', ':elephant:', ':panda_face:', ':snake:', ':bird:', ':baby_chick:', ':hatched_chick:', ':hatching_chick:', ':chicken:', ':penguin:', ':turtle:', ':bug:', ':honeybee:', ':ant:', ':beetle:', ':snail:', ':octopus:', ':tropical_fish:', ':fish:', ':whale:', ':whale2:', ':dolphin:', ':cow2:', ':ram:', ':rat:', ':water_buffalo:', ':tiger2:', ':rabbit2:', ':dragon:', ':goat:', ':rooster:', ':dog2:', ':pig2:', ':mouse2:', ':ox:', ':dragon_face:', ':blowfish:', ':crocodile:', ':dromedary_camel:', ':leopard:', ':cat2:', ':poodle:', ':paw_prints:', ':bouquet:', ':cherry_blossom:', ':tulip:', ':four_leaf_clover:', ':rose:', ':sunflower:', ':hibiscus:', ':maple_leaf:', ':leaves:', ':fallen_leaf:', ':herb:', ':mushroom:', ':cactus:', ':palm_tree:', ':evergreen_tree:', ':deciduous_tree:', ':chestnut:', ':seedling:', ':blossom:', ':ear_of_rice:', ':shell:', ':globe_with_meridians:', ':sun_with_face:', ':full_moon_with_face:', ':new_moon_with_face:', ':new_moon:', ':waxing_crescent_moon:', ':first_quarter_moon:', ':waxing_gibbous_moon:', ':full_moon:', ':waning_gibbous_moon:', ':last_quarter_moon:', ':waning_crescent_moon:', ':last_quarter_moon_with_face:', ':first_quarter_moon_with_face:', ':crescent_moon:', ':earth_africa:', ':earth_americas:', ':earth_asia:', ':volcano:', ':milky_way:', ':partly_sunny:', ':octocat:', ':squirrel:', ':bamboo:', ':gift_heart:', ':dolls:', ':school_satchel:', ':mortar_board:', ':flags:', ':fireworks:', ':sparkler:', ':wind_chime:', ':rice_scene:', ':jack_o_lantern:', ':ghost:', ':santa:', ':christmas_tree:', ':gift:', ':bell:', ':no_bell:', ':tanabata_tree:', ':tada:', ':confetti_ball:', ':balloon:', ':crystal_ball:', ':cd:', ':dvd:', ':floppy_disk:', ':camera:', ':video_camera:', ':movie_camera:', ':computer:', ':tv:', ':iphone:', ':phone:', ':telephone:', ':telephone_receiver:', ':pager:', ':fax:', ':minidisc:', ':vhs:', ':sound:', ':speaker:', ':mute:', ':loudspeaker:', ':mega:', ':hourglass:', ':hourglass_flowing_sand:', ':alarm_clock:', ':watch:', ':radio:', ':satellite:', ':loop:', ':mag:', ':mag_right:', ':unlock:', ':lock:', ':lock_with_ink_pen:', ':closed_lock_with_key:', ':key:', ':bulb:', ':flashlight:', ':high_brightness:', ':low_brightness:', ':electric_plug:', ':battery:', ':calling:', ':email:', ':mailbox:', ':postbox:', ':bath:', ':bathtub:', ':shower:', ':toilet:', ':wrench:', ':nut_and_bolt:', ':hammer:', ':seat:', ':moneybag:', ':yen:', ':dollar:', ':pound:', ':euro:', ':credit_card:', ':money_with_wings:', ':e-mail:', ':inbox_tray:', ':outbox_tray:', ':envelope:', ':incoming_envelope:', ':postal_horn:', ':mailbox_closed:', ':mailbox_with_mail:', ':mailbox_with_no_mail:', ':package:', ':door:', ':smoking:', ':bomb:', ':gun:', ':hocho:', ':pill:', ':syringe:', ':page_facing_up:', ':page_with_curl:', ':bookmark_tabs:', ':bar_chart:', ':chart_with_upwards_trend:', ':chart_with_downwards_trend:', ':scroll:', ':clipboard:', ':calendar:', ':date:', ':card_index:', ':file_folder:', ':open_file_folder:', ':scissors:', ':pushpin:', ':paperclip:', ':black_nib:', ':pencil2:', ':straight_ruler:', ':triangular_ruler:', ':closed_book:', ':green_book:', ':blue_book:', ':orange_book:', ':notebook:', ':notebook_with_decorative_cover:', ':ledger:', ':books:', ':bookmark:', ':name_badge:', ':microscope:', ':telescope:', ':newspaper:', ':football:', ':basketball:', ':soccer:', ':baseball:', ':tennis:', ':8ball:', ':rugby_football:', ':bowling:', ':golf:', ':mountain_bicyclist:', ':bicyclist:', ':horse_racing:', ':snowboarder:', ':swimmer:', ':surfer:', ':ski:', ':spades:', ':hearts:', ':clubs:', ':diamonds:', ':gem:', ':ring:', ':trophy:', ':musical_score:', ':musical_keyboard:', ':violin:', ':space_invader:', ':video_game:', ':black_joker:', ':flower_playing_cards:', ':game_die:', ':dart:', ':mahjong:', ':clapper:', ':memo:', ':pencil:', ':book:', ':art:', ':microphone:', ':headphones:', ':trumpet:', ':saxophone:', ':guitar:', ':shoe:', ':sandal:', ':high_heel:', ':lipstick:', ':boot:', ':shirt:', ':tshirt:', ':necktie:', ':womans_clothes:', ':dress:', ':running_shirt_with_sash:', ':jeans:', ':kimono:', ':bikini:', ':ribbon:', ':tophat:', ':crown:', ':womans_hat:', ':mans_shoe:', ':closed_umbrella:', ':briefcase:', ':handbag:', ':pouch:', ':purse:', ':eyeglasses:', ':fishing_pole_and_fish:', ':coffee:', ':tea:', ':sake:', ':baby_bottle:', ':beer:', ':beers:', ':cocktail:', ':tropical_drink:', ':wine_glass:', ':fork_and_knife:', ':pizza:', ':hamburger:', ':fries:', ':poultry_leg:', ':meat_on_bone:', ':spaghetti:', ':curry:', ':fried_shrimp:', ':bento:', ':sushi:', ':fish_cake:', ':rice_ball:', ':rice_cracker:', ':rice:', ':ramen:', ':stew:', ':oden:', ':dango:', ':egg:', ':bread:', ':doughnut:', ':custard:', ':icecream:', ':ice_cream:', ':shaved_ice:', ':birthday:', ':cake:', ':cookie:', ':chocolate_bar:', ':candy:', ':lollipop:', ':honey_pot:', ':apple:', ':green_apple:', ':tangerine:', ':lemon:', ':cherries:', ':grapes:', ':watermelon:', ':strawberry:', ':peach:', ':melon:', ':banana:', ':pear:', ':pineapple:', ':sweet_potato:', ':eggplant:', ':tomato:', ':corn:', ':house:', ':house_with_garden:', ':school:', ':office:', ':post_office:', ':hospital:', ':bank:', ':convenience_store:', ':love_hotel:', ':hotel:', ':wedding:', ':church:', ':department_store:', ':european_post_office:', ':city_sunrise:', ':city_sunset:', ':japanese_castle:', ':european_castle:', ':tent:', ':factory:', ':tokyo_tower:', ':japan:', ':mount_fuji:', ':sunrise_over_mountains:', ':sunrise:', ':stars:', ':statue_of_liberty:', ':bridge_at_night:', ':carousel_horse:', ':rainbow:', ':ferris_wheel:', ':fountain:', ':roller_coaster:', ':ship:', ':speedboat:', ':boat:', ':sailboat:', ':rowboat:', ':anchor:', ':rocket:', ':airplane:', ':helicopter:', ':steam_locomotive:', ':tram:', ':mountain_railway:', ':bike:', ':aerial_tramway:', ':suspension_railway:', ':mountain_cableway:', ':tractor:', ':blue_car:', ':oncoming_automobile:', ':car:', ':red_car:', ':taxi:', ':oncoming_taxi:', ':articulated_lorry:', ':bus:', ':oncoming_bus:', ':rotating_light:', ':police_car:', ':oncoming_police_car:', ':fire_engine:', ':ambulance:', ':minibus:', ':truck:', ':train:', ':station:', ':train2:', ':bullettrain_front:', ':bullettrain_side:', ':light_rail:', ':monorail:', ':railway_car:', ':trolleybus:', ':ticket:', ':fuelpump:', ':vertical_traffic_light:', ':traffic_light:', ':warning:', ':construction:', ':beginner:', ':atm:', ':slot_machine:', ':busstop:', ':barber:', ':hotsprings:', ':checkered_flag:', ':crossed_flags:', ':izakaya_lantern:', ':moyai:', ':circus_tent:', ':performing_arts:', ':round_pushpin:', ':triangular_flag_on_post:', ':jp:', ':kr:', ':cn:', ':us:', ':fr:', ':es:', ':it:', ':ru:', ':gb:', ':uk:', ':de:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:', ':1234:', ':zero:', ':hash:', ':symbols:', ':arrow_backward:', ':arrow_down:', ':arrow_forward:', ':arrow_left:', ':capital_abcd:', ':abcd:', ':abc:', ':arrow_lower_left:', ':arrow_lower_right:', ':arrow_right:', ':arrow_up:', ':arrow_upper_left:', ':arrow_upper_right:', ':arrow_double_down:', ':arrow_double_up:', ':arrow_down_small:', ':arrow_heading_down:', ':arrow_heading_up:', ':leftwards_arrow_with_hook:', ':arrow_right_hook:', ':left_right_arrow:', ':arrow_up_down:', ':arrow_up_small:', ':arrows_clockwise:', ':arrows_counterclockwise:', ':rewind:', ':fast_forward:', ':information_source:', ':ok:', ':twisted_rightwards_arrows:', ':repeat:', ':repeat_one:', ':new:', ':top:', ':up:', ':cool:', ':free:', ':ng:', ':cinema:', ':koko:', ':signal_strength:', ':u5272:', ':u5408:', ':u55b6:', ':u6307:', ':u6708:', ':u6709:', ':u6e80:', ':u7121:', ':u7533:', ':u7a7a:', ':u7981:', ':sa:', ':restroom:', ':mens:', ':womens:', ':baby_symbol:', ':no_smoking:', ':parking:', ':wheelchair:', ':metro:', ':baggage_claim:', ':accept:', ':wc:', ':potable_water:', ':put_litter_in_its_place:', ':secret:', ':congratulations:', ':m:', ':passport_control:', ':left_luggage:', ':customs:', ':ideograph_advantage:', ':cl:', ':sos:', ':id:', ':no_entry_sign:', ':underage:', ':no_mobile_phones:', ':do_not_litter:', ':non-potable_water:', ':no_bicycles:', ':no_pedestrians:', ':children_crossing:', ':no_entry:', ':eight_spoked_asterisk:', ':sparkle:', ':eight_pointed_black_star:', ':heart_decoration:', ':vs:', ':vibration_mode:', ':mobile_phone_off:', ':chart:', ':currency_exchange:', ':aries:', ':taurus:', ':gemini:', ':cancer:', ':leo:', ':virgo:', ':libra:', ':scorpius:', ':sagittarius:', ':capricorn:', ':aquarius:', ':pisces:', ':ophiuchus:', ':six_pointed_star:', ':negative_squared_cross_mark:', ':a:', ':b:', ':ab:', ':o2:', ':diamond_shape_with_a_dot_inside:', ':recycle:', ':end:', ':back:', ':on:', ':soon:', ':clock1:', ':clock130:', ':clock10:', ':clock1030:', ':clock11:', ':clock1130:', ':clock12:', ':clock1230:', ':clock2:', ':clock230:', ':clock3:', ':clock330:', ':clock4:', ':clock430:', ':clock5:', ':clock530:', ':clock6:', ':clock630:', ':clock7:', ':clock730:', ':clock8:', ':clock830:', ':clock9:', ':clock930:', ':heavy_dollar_sign:', ':copyright:', ':registered:', ':tm:', ':x:', ':heavy_exclamation_mark:', ':bangbang:', ':interrobang:', ':o:', ':heavy_multiplication_x:', ':heavy_plus_sign:', ':heavy_minus_sign:', ':heavy_division_sign:', ':white_flower:', ':100:', ':heavy_check_mark:', ':ballot_box_with_check:', ':radio_button:', ':link:', ':curly_loop:', ':wavy_dash:', ':part_alternation_mark:', ':trident:', ':black_small_square:', ':white_small_square:', ':black_medium_small_square:', ':white_medium_small_square:', ':black_medium_square:', ':white_medium_square:', ':black_large_square:', ':white_large_square:', ':white_check_mark:', ':black_square_button:', ':white_square_button:', ':black_circle:', ':white_circle:', ':red_circle:', ':large_blue_circle:', ':large_blue_diamond:', ':large_orange_diamond:', ':small_blue_diamond:', ':small_orange_diamond:', ':small_red_triangle:', ':small_red_triangle_down:', ':shipit:']
    
    df['emojis'] = str('nan')
    df['num_emojis'] = int(0)
    df['mesg_length'] = int(0)

    pattern = re.compile('\:[a-z]{1,25}\:')
    for index, value in df.message.iteritems():
        if (value is not np.nan):
            #Locate emoticons using regex
            #Forget regex - there are too many different types of emoji formats
            #OK - we need to use a combination of both because the list isn't exhaustive
            value_list_emojis = [word for word in str(value) if word in emoji_list]
            value_list_regex = re.findall(pattern, value)

            value_list = [x for x in value_list_regex if x not in value_list_emojis]

            df.set_value(index,'mesg_length', len(str(value)))

            if len(value_list) > 0:
                df.set_value(index,'emojis', ', '.join(value_list))
                df.set_value(index,'num_emojis', len(value_list))
    
    #Replace nans with numpy values            
    df['emojis'][df.num_emojis == 0] = np.nan
    
'''
Checks whether it is public or private data
'''

def is_df_public(df):
    if 'from_user_id' in df.columns:
        return False
    else:
        return True
    
# Map userid to username

# TO-DO: aligning mapping of public df with this mapping

def map_userid_username(df):
    '''
    Takes dataframe and maps username to userid
    Input:
        - Dataframe
    Output:
        - Dictionary (defaultdict) of structure userid:username (key:value)
    '''
    
    dict_userid_username = defaultdict(set)
    group_userid_username = pd.DataFrame(df.groupby(['userid','username']).size().reset_index())
    for row in range(0, len(group_userid_username)):
        dict_userid_username[group_userid_username.loc[row,'userid']] = group_userid_username.loc[row,'username']
    return dict_userid_username

# Replace userid by username

def replace_userid(df, df_ref):
    userid_username = map_userid_username(df_ref)
    for userid in userid_username.keys():
        df['from_user_id'].replace(to_replace=userid, value=userid_username[userid], inplace=True, regex=True)
        df['chat_members'].replace(to_replace=userid, value=userid_username[userid], inplace=True, regex=True)
    return df

# Convert chat_members entries (strings) to sets
def preprocess_chat_members(df):
    try:
        for row in range(0, len(df)):
            df.set_value(row, 'chat_members', list(ast.literal_eval(df.loc[row, 'chat_members'])))
        
    except(AttributeError):
        print('Error: No column named "chat_members" in DataFrame.')
        
def preprocess_time(df):
    df.timestamp = pd.to_datetime(df.timestamp, yearfirst=True)
    #if is_df_public(df) == True:
    #    df.timestamp = df.timestamp + timedelta(hours = 8)
    df = df.sort_values(['timestamp'])

    #Let's keep the 2016 data only as there are some 2015 outliers
    if 'year' in df.columns:
        df = df[df.timestamp.dt.year == 2016]
    
    return df

def remove_infrequent(df, threshold):
    '''
    Given a threshold number of messages, this function calculates the loss of data resulting
    from removing users who have written fewer than this number of messages, and then returns
    the truncated dataframe if the users chooses to proceed.
    
    Input:
        - df: the dataframe
        - threshold: minimum number of messages per user to keep that user in the dataframe
        
    Output:
        - df: the truncated dataframe
    '''
    
    if 'from_user_id' in df.columns:
        user_col = 'from_user_id'
    else:
        user_col = 'username'
    
    num_data = len(df)
    
    user_list = list(df[user_col].unique())
    num_users = len(user_list)
    frequent_user_list = []
    for user in user_list:
        if len(df.loc[df[user_col] == user]) > threshold-1:
            frequent_user_list.append(user)
    
    df_new = df.loc[df[user_col].isin(frequent_user_list)].reset_index()
    new_num_data = len(df_new)
    new_num_users = len(df_new[user_col].unique())
    lost_data = 1 - (new_num_data/num_data)
    lost_users = 1 - (new_num_users/num_users)
    
    print("Losing {0:.2f}% of data and {1:.2f}% of users by removing infrequent users. Proceed? ('y' or 'n')".\
          format(lost_data*100, lost_users*100))
    
    #decision = input()
    decision = 'y'
    
    if decision == 'y':
        df = df_new
    
    return df

#Perform Sentiment Analysis
def sent_analysis(df):
    df["mesg_sentiment"] = float(0)
    df["mesg_sentiment_cat"] = int(0)
    for index, value in df.message.iteritems():
        text_blob = TextBlob(str(value))
        sentiment_value = text_blob.sentiment[0]
        df.set_value(index,'mesg_sentiment', sentiment_value)
        if sentiment_value >= 0:
            df.set_value(index,'mesg_sentiment_cat', int(1))
            
def get_relationship_private(user_x, user_y, df):
    '''
    This implementation gives the exact same results as the one commented out, but returns
    results in a fraction of a second, versus 20 second waiting time for the below code.
    '''
    def x_fn(name):
        return user_x == name
    def y_fn(name):
        return user_y == name
    
    from_msg_1 = df.from_user_id.apply(x_fn)
    from_msg_2 = df.member_0.apply(y_fn) | \
        df.member_1.apply(y_fn) | \
        df.member_2.apply(y_fn) | \
        df.member_3.apply(y_fn) | \
        df.member_4.apply(y_fn) | \
        df.member_5.apply(y_fn) | \
        df.member_6.apply(y_fn)
        
    to_msg_1 = df.from_user_id.apply(y_fn)
    to_msg_2 = df.member_0.apply(x_fn) | \
        df.member_1.apply(x_fn) | \
        df.member_2.apply(x_fn) | \
        df.member_3.apply(x_fn) | \
        df.member_4.apply(x_fn) | \
        df.member_5.apply(x_fn) | \
        df.member_6.apply(x_fn)
    
    x_msg = df.member_0.apply(x_fn) | \
        df.member_1.apply(x_fn) | \
        df.member_2.apply(x_fn) | \
        df.member_3.apply(x_fn) | \
        df.member_4.apply(x_fn) | \
        df.member_5.apply(x_fn) | \
        df.member_6.apply(x_fn)
        
    y_msg = df.member_0.apply(y_fn) | \
        df.member_1.apply(y_fn) | \
        df.member_2.apply(y_fn) | \
        df.member_3.apply(y_fn) | \
        df.member_4.apply(y_fn) | \
        df.member_5.apply(y_fn) | \
        df.member_6.apply(y_fn)
    
    from_msg = (from_msg_1 & from_msg_2)
    from_msg_count = from_msg.sum()
    
    to_msg = (to_msg_1 & to_msg_2)
    to_msg_count = to_msg.sum()
    
    x_msg_count = x_msg.sum()
    y_msg_count = y_msg.sum()
    
    from_sent_ratio = (from_msg * df.mesg_sentiment).sum() / max(1, from_msg_count)
    to_sent_ratio = (to_msg * df.mesg_sentiment).sum() / max(1, to_msg_count)

    return from_msg_count, from_sent_ratio, to_msg_count, to_sent_ratio, x_msg_count, y_msg_count

def get_relationship_message(user_x, user_y, df):
    a, _, b, _, c, d = get_relationship_private(user_x, user_y, df)
    return (a+b) / max(1,(c+d))

def plot_user_matrix(user_list, df):
    size = len(user_list)
    user_dict = {}
    for i in range(len(user_list)):
        user_dict[i] = user_list[i]
    matrix = np.zeros([size, size])
    for i in range(size):
        for j in range(i):
            matrix[i,j] = get_relationship_message(user_dict[i], user_dict[j], df)
    ax = sb.heatmap(matrix, xticklabels=user_list, cmap='PuBu')
    ax.set_yticklabels(user_list[::-1], rotation=0)
    ax.set_title('Mutual connectedness via private slack messages')
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([0, np.max(matrix)])
    cbar.set_ticklabels(['Not very connected', 'Very connected'])
    return matrix

def get_relationship_sentiment(user_x, user_y, df):
    _, a, _, b, _, _ = get_relationship_private(user_x, user_y, df)
    return a, b

def plot_sentiment_matrix(user_list, df):
    size = len(user_list)
    user_dict = {}
    for i in range(len(user_list)):
        user_dict[i] = user_list[i]
    matrix = np.zeros([size, size])
    for i in range(size):
        for j in range(i):
            matrix[i,j], matrix[j,i] = get_relationship_sentiment(user_dict[i], user_dict[j], df)
    ax = sb.heatmap(matrix, xticklabels=user_list, cmap="RdYlGn")
    ax.set_yticklabels(user_list[::-1], rotation=0)
    ax.set_title('Sentiment via private slack messages')
    ax.set(xlabel='Sentiment recipient', ylabel='Sentiment giver')
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([np.min(matrix), np.max(matrix)])
    cbar.set_ticklabels(['Negative sentiment', 'Positive sentiment'])
    return matrix

def null_conversion(username):
    '''
    Generates a fullname from a username
    Input:
        - username: string  
    Output:
        - fullname: string
    '''
    names = [name.title() for name in username.split('.')]
    fullname = ' '.join(names)
    return fullname


def create_fullname_username_map(df):
    '''
    Creates a dictionary that maps each fullname to a unique username, based on the most
    recent username in usage.
    
    Input:
        - df: the dataframe, with date conversion already applied
        
    Output:
        - single_name_mapping: a dictionary that maps each fullname to a unique username,
        based on the mostrecent username in usage.
    '''
    multiple_name_mapping = {}
    for fullname in df.fullname.unique():
        list_of_usernames = list(df.loc[df.fullname == fullname,('username')].unique())
        dict_of_usernames = {}
        for username in list_of_usernames:
            maximum_date = df.loc[df.username == username,'timestamp'].max()
            dict_of_usernames[username] = maximum_date
        multiple_name_mapping[fullname] = dict_of_usernames
    
    single_name_mapping = {}
    for fullname, username_dict in multiple_name_mapping.items():
        latest_username = max(username_dict.keys(), key=lambda k: username_dict[k])
        single_name_mapping[fullname] = latest_username

    new_name_mapping = {}
    for fullname, username_dict in multiple_name_mapping.items():
        latest_username = max(username_dict.keys(), key=lambda k: username_dict[k])
        new_name_mapping[latest_username] = list(username_dict.keys())
    return single_name_mapping, new_name_mapping



def merge_usernames(fullname, mapping):
    '''
    Applies the mapping to individual users.
    Input:
        - fullname: string
    Output:
        - merged_username: string
    '''
    merged_username = mapping[fullname]
    return merged_username



def remove_msg(df):
    df = df.loc[df.message.str.contains('has renamed the channel from') == False]
    df = df.loc[df.message.str.contains('uploaded a file:') == False]



#Create num_mentions

def create_num_mentions(df):
    try:
        df['num_mentions'] = int(0)
        for index, value in df.mentions.iteritems():
            if (value is not np.nan):
                value_list = str(value).split(',')
                df.set_value(index,'num_mentions', len(value_list))
    except(AttributeError):
        if 'mentions' not in df.columns:
            print('Error: DataFrame does not have a column named "mentions".')



# TO-DO: Extend to conversation partner search

def channel_search(df, search_term):
    '''
    Returns all channel names that include a given string
    
    Input:
        - search_term: string
        
    Output:
        - search_results: a list of channel names
    '''
    all_channels = list(df.channel.unique())
    
    search_results = []
    for channel in all_channels:
        if search_term.lower() in channel:
            search_results.append(channel)
            
    return search_results


def calc_obj_preprocessing(df, obj_name, obj_type, start_month, end_month, year=2016):
    '''
    Preprocesses data for object calculation.
    
    Input:
        - obj_name: unique username of user or unique channel name
                    IF 'all' USED AS obj_name THEN TOTALS ACROSS ALL USERS/CHANNELS ARE COMPUTED
        - obj_type: 'user' for a user, 'channel' for a channel
        - start_month: begin of calculation (e.g. 1 for January)
        - end_month: end of calculation (e.g. 12 for December)
        - year: year of calculation (e.g. 2016)
        
    Output:
        - df_obj_months: preprocessed pandas data frame including specified time frame and objects
    '''
    
    if is_df_public(df) == False:
        if 'channel' in obj_type:
            raise TypeError('DataFrame is private - setting "channel" not appropriate!')
        else:
            user_col = 'from_user_id'
    else:
        user_col = 'username'
        

    if obj_name == 'all':
        df_obj = df.loc[:]
    elif obj_type == 'user':
        df_obj = df.loc[df[user_col] == obj_name]
    elif obj_type == 'channel':
        df_obj = df.loc[df.channel == obj_name]
            
    # Preprocessing formats
    df_obj['year'] = df_obj['timestamp'].dt.year
    df_obj['hour'] = pd.DatetimeIndex(df_obj['timestamp']).round('1h')
    df_obj['hour'] = df_obj['hour'].dt.hour
    if is_df_public(df) == True:
        months = [month for month in range(start_month, end_month+1)]
        df_obj['month'] = df_obj[df_obj['year']==year]['timestamp'].dt.month
    else:
        months = [12,1]
        df_obj['month'] = df_obj['timestamp'].dt.month
    
    # Filter by months
    df_obj_months = df_obj.loc[df_obj['month'].isin(months)]
    
    return df_obj_months




def calc_obj_month(df, obj_name, obj_type, start_month, end_month, year=2016):
    '''
    Calculates metrics for a specified object in a defined time frame
    
    Input:
        - obj_name: unique username of user or unique channel name
                    IF 'all' USED AS obj_name THEN TOTALS ACROSS ALL USERS/CHANNELS ARE COMPUTED
        - obj_type: 'user' for a user, 'channel' for a channel
        - start_month: begin of calculation (e.g. 1 for January)
        - end_month: end of calculation (e.g. 12 for December)
        - year: year of calculation (e.g. 2016)
        
    Output:
        - df_obj_kpi_month: pandas data frame including all computed KPIs per month
    '''
    
    # Load preprocessed data
    df_obj_months = calc_obj_preprocessing(df, obj_name, obj_type, start_month, end_month, year)
    
    # Calculating KPIs
    if is_df_public(df) == True:
        months = [month for month in range(start_month, end_month+1)]
    else:
        months = [12,1]
    
    if is_df_public(df) == False:
        cols = ['month','emojis_per_msg', 'sentiment_mean', 'msg_length', 'msg_count']
    else:
        cols = ['month','mentions_sum','emojis_per_msg', 'sentiment_mean', 'msg_length', 'msg_count']    
    
    df_obj_kpi_month = pd.DataFrame(index=months, columns=cols)
    
    index = 0
    for month in months:
        kpi_list = []
        df_obj_month = df_obj_months.loc[df_obj_months['month'] == month]
        obj_msg_number = df_obj_month['message'].count()
        obj_sentiment = df_obj_month['mesg_sentiment'].mean()
        obj_msg_length = df_obj_month['mesg_length'].mean()
        obj_emojis = df_obj_month['num_emojis'].sum() / max(1, obj_msg_number)
        if is_df_public(df) == True:
            obj_mentions = df_obj_month['num_mentions'].sum()
        
        if obj_msg_number > 0:
            if is_df_public(df) == True:
                kpi_list.extend([int(month), int(obj_mentions), float(obj_emojis), float(obj_sentiment), float(obj_msg_length), int(obj_msg_number)])
            else:
                kpi_list.extend([int(month), float(obj_emojis), float(obj_sentiment), float(obj_msg_length), int(obj_msg_number)])

        else:
            if is_df_public(df) == True:
                kpi_list.extend([month, 0, 0, 0, 0, 0])
            else:
                kpi_list.extend([month, 0, 0, 0, 0])
        
        for i in range(0,len(kpi_list)):
            df_obj_kpi_month.iloc[index,i] = kpi_list[i] 
        
        index += 1
        
    return df_obj_kpi_month #return DF with KPIs of obj for each month



def calc_obj_activity(df, obj_name, obj_type, start_month, end_month, year=2016):
    '''
    Calculates activity of objects for a defined time frame in months
    
    Input:
        - obj_name: unique username of user or unique channel name
                    IF 'all' USED AS obj_name THEN TOTALS ACROSS ALL USERS/CHANNELS ARE COMPUTED
        - obj_type: 'user' for a user, 'channel' for a channel
        - start_month: begin of calculation (e.g. 1 for January)
        - end_month: end of calculation (e.g. 12 for December)
        - year: year of calculation (e.g. 2016)
        
    Output:
        - df_obj_activity: pandas data frame including normalized average activity time for selected time frame
    '''
    
    # Load preprocessed data
    df_obj_months = calc_obj_preprocessing(df, obj_name, obj_type, start_month, end_month, year)
    
    # Calculate activity per hour and extract index
    obj_activity = list(df_obj_months['hour'].value_counts(normalize=True)) # getting normalized value_counts
    index = df_obj_months['hour'].value_counts(normalize=True).index.tolist() # extracting index of series(hours)
    obj_activity = [obj_activity for (index, obj_activity) in sorted(zip(index, obj_activity))] # sorting value_counts by index(hour)
    hours_real = sorted(index)
    hours_range = [x for x in range(0,25)]
    
    if is_df_public(df) == False:
        hours_real = hours_real[1:]
        hours_real.append(24)
        obj_activity_last = obj_activity[-1]
        obj_activity = obj_activity[1:]
        obj_activity.append(obj_activity_last)
    
    # Merge into data frame
    df_obj_activity = pd.DataFrame(index = hours_range, columns=['activity_mean'])
    
    count = 0
    for i in range(min(hours_range), max(hours_range)+1):
        if i in hours_real:
            df_obj_activity.loc[i, 'activity_mean'] = obj_activity[count]
            count += 1
        else:
            df_obj_activity.loc[i, 'activity_mean'] = 0
        
    return df_obj_activity


def plot_time(df, start_date='2016-01-01', end_date='2016-12-31'):
    #Plot hours with time
    fig = plt.figure(figsize=(16, 6))
    plt.plot([dt.date() for dt in df.timestamp],
               [dt.hour + dt.minute/60. for dt in df.timestamp],
               '.', markersize=8, alpha=0.5)
    plt.xlim([start_date, end_date])
    plt.ylim([0, 24])
    plt.show()

def plot_compare_objs(df, objs, start_month, end_month, year=2016):
    '''
    Plots metrics for 2 specified objects in a defined time frame by laying two plots on top of each other
    
    Input:
        - objs: list of lists. Each second-level list is of the form [obj_name, obj_type]
        as specified in previously defined functions
                 IF 'all' USED AS ONE OF THE obj_name's THEN TOTALS ACROSS ALL USERS 
                 ARE COMPUTED, and the object should be ['all', None]
        - start_month: begin of calculation (e.g. 1 for January)
        - end_month: end of calculation (e.g. 12 for December)
        - year: year of calculation (e.g. 2016)
    '''
    
    if is_df_public(df) == False:
        print('Since data is only available from mid December 2016 to mid January 2017, the whole time frame will be plotted.')
        start_month = 12
        end_month = 1
    
    # Run and store calculations
    list_df_objs = [calc_obj_month(df, obj[0], obj[1], start_month, end_month, year=2016) for obj in objs]

    # Compute random color for each obj
    cmap = plt.get_cmap('jet')
    colors = cmap(np.linspace(0, 0.3, len(objs)))
    
    # Setup plot structure
    fig, axs = plt.subplots(3,2, figsize=(11, 14), facecolor='w', edgecolor='k')
    axs = axs.ravel()
    
    # Plotting
    obj_count = 0

    for obj in objs:
        try:
            axs[0].plot(calc_obj_activity(df, obj[0], obj[1], start_month, end_month, year), color=colors[obj_count], alpha=0.5)
        except: None
        obj_count += 1
    if is_df_public(df) == False:
        axs[0].set_xlim([1,24])
        axs[0].xaxis.set_ticks(np.arange(1, 25, 1))
    else:   
        axs[0].set_xlim([9,21])
        axs[0].xaxis.set_ticks(np.arange(8, 23, 1))
    axs[0].set_title(str('activity_mean'))
    axs[0].set_xlabel('Time (hours)')
    axs[0].legend(labels=[obj[0] for obj in objs], loc=2)

    
    for i in range(1, len(list_df_objs[0].columns)):
        obj = 0
        for df_obj in list_df_objs:
            axs[i].plot(df_obj['month'], df_obj[df_obj.columns[i]], color=colors[obj], alpha=0.5)
            obj += 1
        axs[i].set_title(str(list_df_objs[0].columns[i]))
        axs[i].set_xlabel('Months')
        axs[i].set_xlim([start_month,end_month])
        if is_df_public(df) == False:
            axs[i].xaxis.set_ticks((0,1))
        axs[i].xaxis.set_ticks(np.arange(start_month, end_month+1, 1))
        axs[i].legend(labels=[obj[0] for obj in objs], loc=2)
    
    if is_df_public(df) == False:
        fig.delaxes(axs[5])
    plt.tight_layout()
    plt.show()

def plot_user_connectedness_graph(user_matrix, user_list):
    fig = plt.figure(figsize=[8, 8])
    labels = {}
    for i, user in enumerate(user_list):
        labels[i] = user
    G = nx.from_numpy_matrix(user_matrix)
    G = nx.relabel_nodes(G, labels)
    pos = nx.circular_layout(G)
    edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())
    Edges = nx.draw_networkx_edges(G, pos, node_color='w', node_shape='o', node_size=[4000], edgelist=edges, edge_color=weights, width=3.0, edge_cmap=plt.cm.Blues, font_size=12)
    Labels = nx.draw_networkx_labels(G, pos, node_color='w', node_shape='o', node_size=[4000], edgelist=edges, edge_color=weights, width=3.0, edge_cmap=plt.cm.Blues, font_size=12)
    nodes = nx.draw_networkx_nodes(G, pos, node_color='w', node_shape='o', node_size=[4000], edgelist=edges, edge_color=weights, width=3.0, edge_cmap=plt.cm.Blues, font_size=12)
    nodes.set_edgecolor('w')
    nodes.set_sizes([2000])
    plt.axis('off')
    plt.title('Mutual connectedness as a graph')
    plt.show()

def plot_individual_user_time(df, username, max_ylim = 0.2):
    #Histogram of time of day
    fig = plt.figure(figsize=(20,6))

    ax = plt.subplot(1,2,1)
    ax.set_ylim(0,max_ylim)
    ax.set_xlim(0,24)
    plt.hist([dt.hour + dt.minute/60. for dt in df.timestamp[df.username==username]], normed=True)
    plt.title('Message Proportion Time Distribution')
    plt.xlabel('Hour')
    plt.ylabel('Message Count')

    ax = plt.subplot(1,2,2)
    ax.set_ylim(0,max_ylim)
    ax.set_xlim(0,24)
    plt.hist([dt.hour + dt.minute/60. for dt in df.timestamp[df.username==username][df.mesg_sentiment_cat == 0]], normed=True)
    plt.title('Negative Message Proportion Time Distribution')
    plt.xlabel('Hour')
    plt.ylabel('Message Count')

    plt.show()