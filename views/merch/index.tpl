%include('header')

<img class="title" src="/content/titles/merch.jpg" />

<div class="merch">

<h1 class="shifted">Merchandise</h1>

<p class="center">Anfragen / Bestellungen an: <a href="mailto:{{email}}">{{email}}</a></p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
