<!-- Copyright (c) 2023 Kali Yuga //-->

<!DOCTYPE html>
<html lang="de" style="background-image: url('{{get_static_url('/content/background.jpg')}}');">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="{{get_static_url('/content/kali_icon.png')}}" type="image/x-icon">
    <link rel="apple-touch-icon" href="{{get_static_url('/content/apple-touch-icon.png')}}">

%for css in ['normalize', 'layout', 'navigation', module_name]:
    %url = get_static_url('/' + css + '.css')
    <link rel="stylesheet" type="text/css" href="{{url}}">
%end

    <script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
    <script src="{{get_static_url('/collapse.js')}}"></script>

%title = ['KALI YUGA']
%if module_name in ['feed', 'impressum', 'contact']:
    %title.append('Death Metal')
%else:
    %title.append(module_title)
%end
%title.append('Official Homepage')
%title = ' - '.join(title)
    <title>{{title}}</title>
%url = '' if module_name == 'feed' else module_name
    <link rel="canonical" href="https://www.kali-yuga.de/{{url}}">
    <meta charset="utf-8">
    <meta name="title" content="{{title}}">
    <meta name="description" content="{{description}}">
    <meta name="keywords" content="Kali Yuga, Kaliyuga, Kali-Yuga, Death Metal, Melodic Death Metal, Band, Gera">
    <meta http-equiv="content-language" content="de">
    <meta name="robots" content="index,follow">
    <meta property="og:title" content="{{title}}">
    <meta property="og:site_name" content="{{title}}">
    <meta property="og:description" content="{{description}}">
    <meta property="og:url" content="https://www.kali-yuga.de">
    <meta name="HandheldFriendly" content="true">
    <meta name="format-detection" content="telephone=yes">
</head>

<body>
%include('navigation')

    <div id="content">
