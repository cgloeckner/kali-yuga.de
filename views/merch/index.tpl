%description = 'CDs, T-Shirts und mehr hält die Geraer Death Metal Band KALI YUGA für den geneigten Fan bereit. Anfragen an ' + merch_email
%include('header', module_name='merch')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/merch.jpg')}}">

<div class="merch">

<h1 class="shifted">{{module_title}}</h1>

<p class="center card">Merch könnt ihr bei unseren Konzerten oder per Post erhalten.<br>
    Alle Preise inkl. MwSt., ggf. zzgl. Versandkosten.<br>
    <br>
    Alle CDs sind außerdem digital verfügbar
    <a class="listen" href="https://open.spotify.com/intl-de/artist/0DhRXdfjAaiKLTZ2vYYbtI" target="_blank">
        <img class="icon" alt="Spotify Link" src="https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico">
    </a>
    <br>
    <br>
    <b>Anfragen / Bestellungen an:</b><br>
    <a href="mailto:{{merch_email}}">{{merch_email}}</a>
</p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
