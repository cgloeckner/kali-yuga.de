<!-- Copyright (c) 2023 Kali Yuga //-->

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="static/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" type="text/css" href="/static/normalize.css">
    <link rel="stylesheet" type="text/css" href="/static/layout.css">
    <script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
    <script src="/static/navigation.js"></script>
    <script src="/static/collapse.js"></script>
    <title>Kali Yuga</title>
</head>

<body>
    <div class="navigation">
        <div class="icon">&#x2261;</div>
        <div class="title"></div>
        <div class="elements">
            <span onClick="loadContent('home')">Start</span>
            <span onClick="loadContent('band')">Band</span>
            <span onClick="loadContent('gigs')">Gigs</span>
            <span onClick="loadContent('merch')">Merch</span>
            <span onClick="loadContent('contact')">Kontakt</span>
            <span onClick="loadContent('imprint')">Impressum</span>
        </div>
    </div>

    <div id="content">
