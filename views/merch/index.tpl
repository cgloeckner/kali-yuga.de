%include('header')

<div class="merch">

<h1>Merchandise</h1>

<p class="center">Anfragen / Bestellungen an: <a href="mailto:merch@kali-yuga.de">merch@kali-yuga.de</a></p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
