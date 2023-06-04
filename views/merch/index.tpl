%description = 'CDs, T-Shirts und mehr hält die Geraer Death Metal Band KALI YUGA für den geneigten Fan bereit. Anfragen an ' + merch_email
%include('header', module_name='merch')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/merch.jpg')}}">

<div class="merch">

<h1 class="shifted">{{module_title}}</h1>

<p class="center">Anfragen / Bestellungen an: <a href="mailto:{{merch_email}}">{{merch_email}}</a></p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
