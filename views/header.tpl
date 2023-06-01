<!-- Copyright (c) 2023 Kali Yuga //-->

<!DOCTYPE html>
<html lang="de" style="background-image: url('{{get_static_url('/content/background.jpg')}}');">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/content/kali_icon.png" type="image/x-icon">

%for css in ['normalize', 'layout', 'navigation', 'feed', 'releases', 'lineup', 'gigs', 'gallery', 'merch', 'impressum']:
    %url = get_static_url('/' + css + '.css')
    <link rel="stylesheet" type="text/css" href="{{url}}">
%end

    <script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
    <script src="{{get_static_url('/collapse.js')}}"></script>

    <title>Kali Yuga</title>
    <meta name="description" content="KALI YUGA ist eine Melodic-Death-Metal-Band aus Gera. Eik Halle (Gitarre), Michael Albert (Gitarre), Jan Koch (Bass), Christian Glöckner (Gesang) und Jean-Peer Krutz (Schlagzeug) bilden das Line-Up.">
    <meta name="keywords" content="">
    <meta name="format-detection" content="telephone=yes">
</head>

<body>
%include('navigation')

    <div id="content">
