import django.dispatch

parsed_hashtags = django.dispatch.Signal(providing_args=['hashtag_list'])