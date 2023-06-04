%include('header', module_css='merch')

<img class="title" src="{{get_static_url('/content/titles/merch.jpg')}}">

<div class="merch">

<h1 class="shifted">Merchandise</h1>

<p class="center">Anfragen / Bestellungen an: <a href="mailto:{{merch_email}}">{{merch_email}}</a></p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
